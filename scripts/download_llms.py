#!/usr/bin/env python3
import argparse
import re
import shutil
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import List, Optional, Tuple

URL_RE = re.compile(r'\((https?://[^)\s]+)(?:\s+"[^"]*")?\)')


def extract_urls(text: str) -> List[str]:
    return URL_RE.findall(text)


def url_to_filename(url: str) -> Optional[str]:
    path = urllib.parse.urlparse(url).path
    name = Path(path).name
    return name or None


def download(url: str, dest: Path) -> None:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "neon-llms-downloader/1.0"},
    )
    tmp_path = dest.with_name(dest.name + ".part")
    try:
        with urllib.request.urlopen(req) as response, open(tmp_path, "wb") as handle:
            shutil.copyfileobj(response, handle)
        tmp_path.replace(dest)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Download files referenced in neon/llms.txt into neon/docs.",
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=None,
        help="Path to llms.txt (default: neon/llms.txt alongside this script).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Destination directory (default: neon/docs alongside this script).",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip files that already exist in the output directory.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print each downloaded file.",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    input_path = args.input or (script_dir / "llms.txt")
    output_dir = args.output_dir or (script_dir / "docs")

    try:
        text = input_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1

    urls = extract_urls(text)
    unique_urls = list(dict.fromkeys(urls))

    output_dir.mkdir(parents=True, exist_ok=True)

    skipped_no_name: List[str] = []
    skipped_existing: List[str] = []
    failures: List[Tuple[str, str]] = []
    downloaded = 0

    for url in unique_urls:
        filename = url_to_filename(url)
        if not filename:
            skipped_no_name.append(url)
            continue

        dest = output_dir / filename
        if args.skip_existing and dest.exists():
            skipped_existing.append(url)
            continue

        try:
            download(url, dest)
            downloaded += 1
            if args.verbose:
                print(f"Downloaded {dest.name}")
        except Exception as exc:  # pragma: no cover - we just log and continue
            failures.append((url, str(exc)))

    print(f"Found {len(unique_urls)} URLs.")
    print(f"Downloaded {downloaded} files into {output_dir}.")
    if skipped_existing:
        print(f"Skipped {len(skipped_existing)} existing files.")
    if skipped_no_name:
        print(f"Skipped {len(skipped_no_name)} URLs without filenames.")
    if failures:
        print(f"Failed to download {len(failures)} files:", file=sys.stderr)
        for url, error in failures:
            print(f"- {url} ({error})", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

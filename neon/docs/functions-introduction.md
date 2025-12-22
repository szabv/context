# Postgres functions

> The document outlines the use and implementation of PostgreSQL functions within the Neon database, detailing how to create, manage, and utilize these functions to enhance database operations.

## Source

- [Postgres functions HTML](https://neon.com/docs/functions/introduction): The original HTML version of this documentation

Get started with commonly-used Postgres functions with Neon's function guides. For other functions that Postgres supports, visit the official Postgres [Functions and Operators](https://www.postgresql.org/docs/current/functions.html) documentation.

## Aggregate functions

- [array_agg()](functions-array_agg.md): Aggregate elements into an array
- [avg()](functions-avg.md): Calculate the average of a set of values
- [count()](functions-count.md): Count rows or non-null values in a result set
- [max()](functions-max.md): Find the maximum value in a set of values
- [sum()](functions-sum.md): Calculate the sum of a set of values

## Array functions

- [array_length()](functions-array_length.md): Determine the length of an array

## Date / Time functions

- [age()](functions-age.md): Calculate the difference between timestamps or between a timestamp and the current date/time
- [current_timestamp](functions-current_timestamp.md): Get the current date and time
- [date_trunc()](functions-date_trunc.md): Truncate date/time values to a specified precision
- [extract()](functions-extract.md): Extract date and time components from timestamps and intervals
- [now()](functions-now.md): Get the current date and time

## JSON functions

- [array_to_json()](functions-array_to_json.md): Convert an SQL array to a JSON array
- [json()](functions-json.md): Transform JSON data into relational views
- [json_agg()](functions-json_agg.md): Aggregate values into a JSON array
- [json_array_elements()](functions-json_array_elements.md): Expand a JSON array into a set of rows
- [jsonb_array_elements()](functions-jsonb_array_elements.md): Expand a JSONB array into a set of rows
- [json_build_object()](functions-json_build_object.md): Build a JSON object out of a variadic argument list
- [json_each()](functions-json_each.md): Expand JSON into a record per key-value pair
- [json_exists()](functions-json_exists.md): Check for Values in JSON Data Using SQL/JSON Path Expressions
- [json_extract_path()](functions-json_extract_path.md): Extract a JSON sub-object at the specified path
- [json_extract_path_text()](functions-json_extract_path_text.md): Extract a JSON sub-object at the specified path as text
- [json_object()](functions-json_object.md): Create a JSON object from key-value pairs
- [json_populate_record()](functions-json_populate_record.md): Cast a JSON object to a record
- [json_query()](functions-json_query.md): Extract and Transform JSON Values with SQL/JSON Path Expressions
- [json_scalar()](functions-json_scalar.md): Convert Text and Binary Data to JSON Values
- [json_serialize()](functions-json_serialize.md): Convert JSON Values to Text or Binary Format
- [json_table()](functions-json_table.md): Transform JSON data into relational views
- [json_to_record()](functions-json_to_record.md): Convert a JSON object to a record
- [json_value()](functions-json_value.md): Extract and Convert JSON Scalar Values
- [jsonb_each()](functions-jsonb_each.md): Expand JSONB into a record per key-value pair
- [jsonb_extract_path()](functions-jsonb_extract_path.md): Extract a JSONB sub-object at the specified path
- [jsonb_extract_path_text()](functions-jsonb_extract_path_text.md): Extract a JSONB sub-object at the specified path as text
- [jsonb_object()](functions-jsonb_object.md): Create a JSONB object from key-value pairs
- [jsonb_populate_record()](functions-jsonb_populate_record.md): Cast a JSONB object to a record
- [jsonb_to_record()](functions-jsonb_to_record.md): Convert a JSONB object to a record

## Mathematical functions

- [abs()](functions-math-abs.md): Calculate the absolute value of a number
- [random()](functions-math-random.md): Generate a random number between 0 and 1
- [round()](functions-math-round.md): Round numbers to a specified precision

## String functions

- [concat()](functions-concat.md): Concatenate strings
- [lower()](functions-lower.md): Convert a string to lowercase
- [substring()](functions-substring.md): Extract a substring from a string
- [regexp_match()](functions-regexp_match.md): Extract substrings matching a regular expression pattern
- [regexp_replace()](functions-regexp_replace.md): Replace substrings matching a regular expression pattern
- [trim()](functions-trim.md): Remove leading and trailing characters from a string

## Window functions

- [dense_rank()](functions-dense_rank.md): Return the rank of the current row without gaps
- [lag()](functions-window-lag.md): Access values from previous rows in a result set
- [lead()](functions-window-lead.md): Access values from subsequent rows in a result set
- [rank()](functions-window-rank.md): Assign ranks to rows within a result set

---
name: 'sys.sp_cdc_generate_wrapper_function'
title: 'sys.sp_cdc_generate_wrapper_function'
category: 'general'
description: 'Generates scripts to create wrapper functions for the change data capture query functions that'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

The flag bit that indicates whether changes that have a commit time equal to the high

endpoint are included within the extraction interval by the generated procedure.

@closed_high_end_point

is

and has a default value of

, which indicates that the endpoint

should be included. A value of

indicates that all commit times are strictly less than the high

endpoint.

A list of captured columns included in the result set that is returned by the wrapper function.

@column_list

is

and has a default value of

. When

is specified, all

captured columns are included.

A list of included columns for which an update flag is included in the result set returned by the

wrapper function.

@update_flag_list

is

and has a default value of

. When

is specified, no update flags are included.

(success) or

(failure).


## Description
Name of the generated function.

The script that creates the capture-instance wrapper function.

The script that creates the function to wrap the all-changes query for a capture instance is

always generated. If the capture instance supports net-changes queries, the script to generate

a wrapper for this query is also generated.

ﾉ

Expand table

The following example show how you can use

to create

wrappers for all the change data capture functions.

SQL

Change Data Capture stored procedures (Transact-SQL)

Change Data Capture (SSIS)

Related content

```sql
1
```

```sql
0
```

```sql
NULL
```

```sql
NULL
```

```sql
NULL
```

```sql
NULL
```

```sql
0
```

```sql
1
```

```sql
function_name
```

```sql
create_script
```

```sql
sys.sp_cdc_generate_wrapper_function
```

```sql
DECLARE
@wrapper_functions
TABLE
(
function_name SYSNAME,
create_script
NVARCHAR
(
MAX
));
INSERT
INTO
@wrapper_functions
EXECUTE
sys.sp_cdc_generate_wrapper_function;
DECLARE
@create_script
AS
NVARCHAR
(
MAX
);
DECLARE
#hfunctions
CURSOR
LOCAL
FAST_FORWARD
FOR
SELECT
create_script
FROM
@wrapper_functions;
OPEN #hfunctions;
FETCH #hfunctions INTO @create_script;
WHILE (@@fetch_status <> -1)
BEGIN
EXECUTE
sp_executesql @create_script;
FETCH #hfunctions INTO @create_script;
END
CLOSE
#hfunctions;
DEALLOCATE
#hfunctions;
```

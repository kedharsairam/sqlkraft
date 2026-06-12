---
name: "File metadata functions"
title: "File metadata functions"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

assumes that, if not specified, the maximum length of

,

, or

data doesn't exceed 8,000 bytes. If the data being imported is in a LOB data field that

contains any

,

, or

objects that exceed 8,000 bytes,

you must use an XML format file that defines the maximum length for the data field. To specify

the maximum length, edit the format file and declare the MAX_LENGTH attribute.

To bulk export or import SQLXML data, use one of the following data types in your format file.

or

The data is sent in the client code page, or in the code page implied by the

collation.

or

The data is sent as Unicode.

or

The data is sent without any conversion.

Sometimes, you might need to know which file or folder source correlates to a specific row in the

result set.

When you use

, it's important to understand how SQL Server handles

impersonation. For information about security considerations, see.

７

Note

An automatically generated format file doesn't specify the length or maximum length for a

LOB field. However, you can edit a format file and specify the length or maximum length

manually.

Expand table

### nvarchar(1024)

## Filename function

You can use functions

and

to return file names and/or the path in the result

set. Or you can use them to filter data based on the file name and/or folder path. In the following

sections, you'll find short descriptions along samples.

This function returns the file name that the row originates from.

Return data type is. For optimal performance, always cast result of filename

function to appropriate data type. If you use character data type, make sure appropriate length is

used.

The following sample reads the NYC Yellow Taxi data files for the last three months of 2017 and

## returns the number of rides per file. The

part of the query specifies which files will be

read.

The following example shows how

can be used in the

clause to filter the files

to be read. It accesses the entire folder in the

part of the query and filters files in the

clause.

Your results will be the same as the prior example.

### nvarchar(1024)

## Filepath function

This function returns a full path or a part of path:

When called without parameter, returns the full file path that a row originates from.

When called with parameter, returns part of path that matches the wildcard on position

specified in the parameter. For example, parameter value 1 would return part of path that

matches the first wildcard.

Return data type is. For optimal performance, always cast result of

function to appropriate data type. If you use character data type, make sure appropriate length is

used.

The following sample reads NYC Yellow Taxi data files for the last three months of 2017. It returns

the number of rides per file path. The

part of the query specifies which files will be

read.

The following example shows how

can be used in the

clause to filter the files

to be read.

### varbinary(max)

`OPENROWSET(BULK.)`

`SQLCHAR`

`SQLNCHAR`

`SQLBINARY`

`SQLCHAR`

`SQLVARYCHAR`

`SQLNCHAR`

`SQLNVARCHAR`

`SQLBINARY`

`SQLVARYBIN`

`OPENROWSET`

`filepath`

`filename`

`OPENROWSET`

`filename()`

`WHERE`

`OPENROWSET`

`WHERE`

```sql
SELECT nyc.filename()
AS
[filename]
,
COUNT_BIG (*)
AS
[
rows
]
FROM
OPENROWSET(
BULK
'parquet/taxi/year=2017/month=9/*.parquet'
,
DATA_SOURCE =
'SqlOnDemandDemo'
,
FORMAT
=
'PARQUET'
) nyc
GROUP
BY nyc.filename();
SELECT r.filename()
AS
[filename]
,
COUNT_BIG (*)
AS
[
rows
]
FROM
OPENROWSET(
BULK
'csv/taxi/yellow_tripdata_2017-*.csv'
,
DATA_SOURCE =
'SqlOnDemandDemo'
,
FORMAT
=
'CSV'
,
FIRSTROW = 2)
WITH (C1 varchar (200) )
AS
[r]
```

`filepath`

`OPENROWSET`

`filepath()`

`WHERE`

```sql
WHERE r.filename()
IN (
'yellow_tripdata_2017-10.csv'
,
'yellow_tripdata_2017-11.csv'
,
'yellow_tripdata_2017-12.csv'
)
GROUP
BY r.filename()
ORDER
BY
[filename];
```

```sql
SELECT r.filepath()
AS filepath
,
COUNT_BIG (*)
AS
[
rows
]
FROM
OPENROWSET(
BULK
'csv/taxi/yellow_tripdata_2017-1*.csv'
,
DATA_SOURCE =
'SqlOnDemandDemo'
,
FORMAT
=
'CSV'
,
FIRSTROW = 2
)
WITH (
vendor_id
INT
)
AS
[r]
GROUP
BY r.filepath()
ORDER
BY filepath;
```

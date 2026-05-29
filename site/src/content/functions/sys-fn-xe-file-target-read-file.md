---
name: 'sys.fn_xe_file_target_read_file'
title: 'sys.fn_xe_file_target_read_file'
category: 'system'
description: 'Azure SQL Managed Instance'
tags: ["function"]
pubDate: 2026-05-29
---

## A. Retrieve data from files in the local file system

In SQL Server 2019 (15.x) and previous versions, requires

permission on the

server.

In SQL Server 2022 (16.x) and later versions, requires

permission

on the server.

For SQL Server 2014 (12.x) and previous versions, the following example gets all the rows from all

the files, including both the

and

file. In this example, the file targets and metafiles are

located in the trace folder in the

folder.

SQL

In SQL Server 2016 (13.x) and later versions, the following example retrieves events inside all

files in the default folder. The default location is

within the installation folder of

the instance.

SQL

In SQL Server 2017 (14.x) and later versions, the following example retrieves only data from the

last day, from the built-in

session. The

session is an Extended

Events session that is included by default with SQL Server. For more information, see

Use the

system_health session

.

SQL

## B. Retrieve data from blobs in an Azure Storage container

Read data from all blobs in the container with names starting with

.

SQL

Read data from the

blob.

SQL

Read data from the

blob starting with offset 33280.

SQL

Related content

Extended Events Dynamic Management Views

Extended Events Catalog Views (Transact-SQL)

Extended Events overview

Targets for Extended Events

View event data in SQL Server Management Studio

Convert an Existing SQL Trace Script to an Extended Events Session

Use the system_health session

Last updated on 04/28/2026

```sql
VIEW SERVER STATE
```

```sql
VIEW SERVER PERFORMANCE STATE
```

```sql
.xel
```

```sql
.xem
```

```sql
C:\traces\
```

```sql
.xel
```

```sql
\MSSQL\Log
```

```sql
system_health
```

```sql
system_health
```

```sql
Msg 40538, Level 16, State 3, Line 15
A valid URL beginning with 'https://' is required as value for any filepath specified.
```

```sql
SELECT
*
FROM
sys.fn_xe_file_target_read_file(
'C:\traces\*.xel'
,
'C:\traces\metafile.xem'
,
NULL
,
NULL
);
SELECT
*
FROM
sys.fn_xe_file_target_read_file(
'*.xel'
,
NULL
,
NULL
,
NULL
);
```

```sql
xe_session_
```

```sql
xe_session_0_133614763336380000.xel
```

```sql
xe_session_0_133614763336380000.xel
```

```sql
SELECT
*
FROM
sys.fn_xe_file_target_read_file(
'system_health*.xel'
,
NULL
,
NULL
,
NULL
)
WHERE
CAST
(timestamp_utc
AS
DATETIME2 (7)) >
DATEADD
(
DAY
, -1,
GETUTCDATE
());
```

```sql
SELECT
*
FROM
sys.fn_xe_file_target_read_file(
'https://<storage-account-name>.blob.core.windows.net/<container-
name>/xe_session_'
,
NULL
,
NULL
,
NULL
);
SELECT
*
FROM
sys.fn_xe_file_target_read_file(
'https://<storage-account-name>.blob.core.windows.net/<container-
name>/xe_session_0_133614763336380000.xel'
,
NULL
,
NULL
,
NULL
);
SELECT
*
FROM
sys.fn_xe_file_target_read_file(
'https://<storage-account-name>.blob.core.windows.net/<container-
name>/xe_session_'
,
NULL
,
'https://<storage-account-name>.blob.core.windows.net/<container-
name>/xe_session_0_133614763336380000.xel'
,
33280
);
```

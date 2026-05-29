---
name: 'Syntax for SQL Server 2019'
title: 'Syntax for SQL Server 2019'
category: 'statements'
description: 'SQL Server 2017 (14.x) and later versions'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2017 (14.x) and later versions

Azure SQL Managed Instance

Uploads R, Python, or Java package files to a database from the specified byte stream or file

path. This statement serves as a generic mechanism for the database administrator to upload

artifacts needed for any new external language runtimes and OS platforms supported by SQL

Server.


## syntaxsql
７

Note

In SQL Server 2017 (14.x), R language and Windows platform are supported. R, Python,

and external languages on the Windows and Linux platforms are supported in SQL Server

2019 (15.x) and later versions.

### ggplot2

### ggplot2

## LIBRARY_NAME

## OWNER_NAME

## FILE_SPEC

Libraries uploaded to the instance can be either public or private. If the library is created by a

member of

, the library is public and can be shared with all users. Otherwise, the library is

private to that user only.

Library names must be unique within the context of a specific user or owner. For example, two

users

and

can both individually and separately upload the R library

.

However, if

wanted to upload a newer version of

, the second instance must be

named differently or must replace the existing library.

Library names can't be arbitrarily assigned; the library name should be the same as the name

required to load the library in the external script.

Specifies the name of the user or role that owns the external library. If not specified, ownership

is given to the current user.

The libraries owned by database owner are considered global to the database and runtime. In

other words, database owners can create libraries that contain a common set of libraries or

packages that are shared by many users. When an external library is created by a user other

than the

user, the external library is private to that user only.

When the user

executes an external script, the value of

can contain multiple

paths. The first path is always the path to the shared library created by the database owner. The

second part of

specifies the path containing packages uploaded individually by

.

Specifies the content of the package for a specific platform. Only one file artifact per platform

is supported.

## LIBRARY_BITS

## PLATFORM

## LANGUAGE

```sql
CREATE
EXTERNAL
LIBRARY
library_name
[
AUTHORIZATION
owner_name ]
FROM
<file_spec>
[ ,...2 ]
WITH
(
LANGUAGE
=
<language>
)
[ ; ]
<file_spec>
::=
{
(
CONTENT
= {
<client_library_specifier>
|
<library_bits>
}
[,
PLATFORM
=
<platform>
])
}
<client_library_specifier>
:: =
{
'[file_path\]manifest_file_name'
}
<library_bits>
:: =
{
varbinary_literal
| varbinary_expression
}
<platform>
:: =
{
WINDOWS
|
LINUX
}
```

```sql
dbo
```

```sql
RUser1
```

```sql
RUser2
```

```sql
RUser1
```

```sql
dbo
```

```sql
RUser1
```

```sql
libPath
```

```sql
libPath
```

```sql
RUser1
```

```sql
<language>
:: =
{
'R'
|
'Python'
|
<external_language>
}
```

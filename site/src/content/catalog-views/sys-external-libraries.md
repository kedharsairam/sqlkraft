---
name: 'sys.external_libraries'
title: 'sys.external_libraries'
category: 'external'
description: 'Summarize this article for me'
tags: ["catalog-view", "external"]
pubDate: 2026-05-29
---

ﾃ

Summarize this article for me

Applies to:

SQL Server 2017 (14.x) and later versions

Azure SQL Managed Instance

The

catalog view supports the management of package libraries

related to external runtimes such as R, Python, and Java.

lists a row for each external library that is uploaded into the database.


## Description
ID of the external library object.

Name of the external library. Is unique within the database per

owner.

ID of the principal that owns this external library.

Name of the language or runtime that supports the external library.

Valid values are

,

, and

.

for public scope;

for private scope.

Indicates whether the package is public or private.

In SQL Server 2017 (14.x), R language and Windows platform are supported. R, Python, and

Java on the Windows and Linux platforms are supported in SQL Server 2019 (15.x) and later. On

Azure SQL Managed Instance, R and Python are supported.

sys.external_library_files

CREATE EXTERNAL LIBRARY (Transact-SQL)

Install R packages with sqlmlutils

Last updated on 02/18/2026

ﾉ

Expand table

Related content

```sql
sys.external_libraries
```

```sql
sys.external_libraries
```

```sql
external_library_id
```

```sql
name
```

```sql
principal_id
```

```sql
language
```

```sql
R
```

```sql
Python
```

```sql
Java
```

```sql
scope
```

```sql
0
```

```sql
1
```

```sql
scope_desc
```

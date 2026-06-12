---
name: "sys.sp_databases"
title: "sp_databases"
category: "general"
description: "Lists databases that either reside in an instance of the SQL Server or are accessible through a database gateway."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  USE
  master
  ;
  GO
  EXECUTE
  sp_databases;
---

## Description

Lists databases that either reside in an instance of the SQL Server or are accessible through a database gateway.

## Syntax

```sql
USE master
;
GO
EXECUTE sp_databases;
```

## Remarks

Lists databases that either reside in an instance of the SQL Server or are accessible through a

database gateway.

Description

Name of the database. In the Database Engine, this column represents

the database name as stored in the

catalog view.

Size of database, in kilobytes.

For the Database Engine, this field always returns

Database names that are returned can be used as parameters in the

statement to change

the current database context.

value for databases larger than 2.15 TB.

Expand table

## Examples

### Example 1

`sp_databases`

### Example 2

```sql
CREATE DATABASE
```

### Example 3

```sql
ALTER ANY DATABASE
```

### Example 4

```sql
VIEW ANY DEFINITION
```

### Example 5

```sql
VIEW ANY DEFINITION
```

### Example 6

`sp_databases`

### Example 7

```sql
USE master
;
GO
EXECUTE sp_databases;
```

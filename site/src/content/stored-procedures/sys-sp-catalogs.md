---
name: "sys.sp_catalogs"
title: "sp_catalogs"
category: "general"
description: "Returns the list of catalogs in the specified linked server. This is equivalent to databases in SQL Transact-SQL syntax conventions"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_catalogs [ @server_name = ]
  N
  'server_name'
  [ ; ]
---

## Description

Returns the list of catalogs in the specified linked server. This is equivalent to databases in SQL Transact-SQL syntax conventions

## Syntax

```sql
sp_catalogs [ @server_name = ]
N
'server_name'
[ ; ]
```

## Examples

### Example 1

`CATALOG_NAME`

### Example 2

`DESCRIPTION`

### Example 3

`SELECT`

### Example 4

```sql
sp_catalogs [ @server_name = ]
N
'server_name'
[ ; ]
```

### Example 5

```sql
OLE DB ODBC
Linked Server #3
```

### Example 6

`sp_catalogs`

### Example 7

```sql
OLE DB ODBC Linked Server #3
```

### Example 8

```sql
USE master
;
GO
EXECUTE sp_catalogs
'OLE DB ODBC Linked Server #3'
;
```

### Example 9

```sql
@table_schema =
'HumanResources'
,
@table_catalog =
'AdventureWorks2022'
;
```

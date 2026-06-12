---
name: "sys.sp_help_fulltext_tables_cursor"
title: "sp_help_fulltext_tables_cursor"
category: "general"
description: "Uses a cursor to return a list of tables that are registered for full-text indexing. The cursor is a read-only, scrollable, dynamic cursor."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_fulltext_tables_cursor
  [ @cursor_return = ] cursor_return
  OUTPUT
  [ , [ @fulltext_catalog_name = ]
  N
  'fulltext_catalog_name'
  ]
  [ , [ @table_name = ]
  N
  'table_name'
  ]
  [ ; ]
---

## Description

Uses a cursor to return a list of tables that are registered for full-text indexing. The cursor is a read-only, scrollable, dynamic cursor.

## Syntax

```sql
sp_help_fulltext_tables_cursor
[ @cursor_return = ] cursor_return
OUTPUT
[ , [ @fulltext_catalog_name = ]
N
'fulltext_catalog_name'
]
[ , [ @table_name = ]
N
'table_name'
]
[ ; ]
```

## Examples

### Example 1

`Cat_Desc`

### Example 2

```sql
USE
AdventureWorks2022;
GO
DECLARE
@mycursor
AS
CURSOR
;
EXECUTE sp_help_fulltext_tables_cursor @mycursor
OUTPUT
,
'Cat_Desc'
;
FETCH NEXT FROM @mycursor;
WHILE (@@FETCH_STATUS <> -1)
BEGIN
FETCH
NEXT
FROM
@mycursor;
END
CLOSE
@mycursor;
DEALLOCATE
@mycursor;
GO
```

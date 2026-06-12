---
name: "sys.sp_help_fulltext_columns_cursor"
title: "sp_help_fulltext_columns_cursor"
category: "general"
description: "Uses a cursor to return the columns designated for full-text indexing. is an OUTPUT parameter of type . The resulting cursor is a read-only, The one- or two-part table name for which full-text index information is requested. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applicatio"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_fulltext_columns_cursor
              [ @cursor_return = ] cursor_return
              OUTPUT
              [ , [ @table_name = ]
              N
              'table_name'
              ]
              [ , [ @column_name = ]
              N
              'column_name'
              ]
              [ ; ]
---

## Description

Uses a cursor to return the columns designated for full-text indexing. is an OUTPUT parameter of type. The resulting cursor is a read-only, The one- or two-part table name for which full-text index information is requested. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_help_fulltext_columns_cursor
[ @cursor_return = ] cursor_return
OUTPUT
[ , [ @table_name = ]
N
'table_name'
]
[ , [ @column_name = ]
N
'column_name'
]
[ ; ]
```

## Examples

### Example 1

```sql
USE
AdventureWorks2022;
GO
DECLARE
@mycursor
AS
CURSOR
;
EXECUTE sp_help_fulltext_columns_cursor @mycursor
OUTPUT
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

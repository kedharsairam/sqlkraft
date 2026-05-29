---
title: "Manage"
topic: "filestream"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Describes common administrative tasks for managing FileTables.

  To get a list of FileTables, query one of the following catalog views:

  sys.filetables
tags:
  - "filestream"
  - "manage"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Describes common administrative tasks for managing FileTables.

To get a list of FileTables, query one of the following catalog views:

sys.filetables (Transact-SQL)

sys.tables (Transact-SQL)

(Check the value of the

column.)

SQL

To get a list of the system-defined objects that were created when the associated FileTables

were created, query the catalog view

sys.filetable_system_defined_objects (Transact-SQL)

.

SQL

To acquire the exclusive access that is required for certain administrative tasks, you may have

to disable non-transactional access temporarily.

```sql
SELECT
*
FROM
sys.filetables;
GO
SELECT
*
FROM
sys.tables
WHERE
is_filetable = 1;
GO
SELECT
object_id, OBJECT_NAME(object_id)
AS
'Object Name'
FROM
sys.filetable_system_defined_objects;
GO
```

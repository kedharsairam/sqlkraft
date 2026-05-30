---
name: "sys.trace_columns"
title: "sys.trace_columns"
category: "objects"
description: "Contains one row for each Extended Events action that is mapped to a SQL Trace column ID. This table is stored in the master database, in the sys schema. trace_column_id The ID of the SQL Trace column that is being mapped. The name of the Extended Events package where the mapped action The name of the Extended Events action that is mapped to the SQL You can use the following query to identify the "
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: "SELECT * FROM sys.trace_columns"
---

## Description

Contains one row for each Extended Events action that is mapped to a SQL Trace column ID. This table is stored in the master database, in the sys schema. trace_column_id The ID of the SQL Trace column that is being mapped. The name of the Extended Events package where the mapped action The name of the Extended Events action that is mapped to the SQL You can use the following query to identify the Extended Events actions that are equivalent to the SQL Trace columns: SQL Trace columns that do not map to actions are not included in the table. trace_xe_event_map (Transact-SQL)

## Syntax

```sql
SELECT * FROM sys.trace_columns
```

## Permissions

Article • 02/28/2023 Applies to: SQL Server Azure SQL Managed Instance The catalog view contains a list of all possible usage combinations of events and columns. For each event listed in the column, all available columns are listed in the column. Not all available columns are populated each time a given event occurs. These values do not change for a given version of the SQL Server Database Engine. For a complete list of supported trace events, see SQL Server Event Class Reference . Description ID of the trace event. This column is also in the catalog view. ID of the trace column. This column is also in the catalog view. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Object Catalog Views (Transact-SQL) sys.traces (Transact-SQL) sys.trace_categories (Transact-SQL) sys.trace_columns (Transact-SQL) ） Important This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Use Extended Event catalog views instead. ﾉ Expand table See Also Article • 02/28/2023 Applies to: SQL Server Azure SQL Managed Instance The catalog view contains a list of named column values. These subclass values do not change for a given version of the SQL Server Database Engine. For a complete list of supported trace events, see SQL Server Event Class Reference . Description ID of the trace event. This parameter is also in the catalog view. ID of the trace column used for enumeration. This parameter is also in the catalog view. Meaning of the column value. Column value. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Object Catalog Views (Transact-SQL) sys.traces (Transact-SQL) sys.trace_categories (Transact-SQL) sys.trace_columns (Transact-SQL) ） Important This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Use Extended Event catalog views instead. ﾉ Expand table See Also

## Remarks

Applies to:

Contains one row for each Extended Events action that is mapped to a SQL Trace column ID.

This table is stored in the master database, in the sys schema.

Description

trace_column_id

The ID of the SQL Trace column that is being mapped.

package_name

The name of the Extended Events package where the mapped action

xe_action_name

The name of the Extended Events action that is mapped to the SQL

Trace column.

You can use the following query to identify the Extended Events actions that are equivalent to

the SQL Trace columns:

SQL Trace columns that do not map to actions are not included in the table.

trace_xe_event_map (Transact-SQL)

Expand table

---
name: "sys.sp_flush_ct_internal_table_on_demand"
title: "sys.sp_flush_CT_internal_table_on_demand"
category: "general"
description: "SQL database in Microsoft Fabric This stored procedure allows you to manually clean the side table ( for a table in a database for which change tracking is enabled. If the isn't passed, then this process cleans all side tables for all tables in the database where change Transact-SQL syntax conventions The change tracking-enabled table to be manually cleaned up. The backlogs are left for the automa"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "change_tracking_objectid"
---

## Description

SQL database in Microsoft Fabric This stored procedure allows you to manually clean the side table ( for a table in a database for which change tracking is enabled. If the isn't passed, then this process cleans all side tables for all tables in the database where change Transact-SQL syntax conventions The change tracking-enabled table to be manually cleaned up. The backlogs are left for the automatic cleanup by change tracking. Can be null to clean up all side tables.

## Syntax

`change_tracking_objectid`

## Permissions

SQL Here's the result set. Output This procedure must be run in a database that has change tracking enabled. When you run the stored procedure, one of the following scenarios happens: If the table doesn't exist or if change tracking isn't enabled, appropriate error messages are thrown. This stored procedure calls another internal stored procedure that cleans up contents from the change tracking side table that's based on the invalid cleanup version by using the dynamic management view. When it's running, it shows the information of total rows deleted (for every 5000 rows). This stored procedure is available in the following products: SQL Server 2016 (13.x) Service Pack 1 and later versions Azure SQL Database and Azure SQL Managed Instance Only a member of the server role or database role can execute this procedure.

## Examples

### Example 1

`change_tracking_objectid`

### Example 2

```sql
0
```

### Example 3

```sql
1
```

### Example 4

```sql
sys.sp_flush_
CT
_internal_table_on_demand
[ @
T able
T o
C lean = ]
'TableToClean'
[ , [ @
D eleted
R ow
C ount = ]
D eleted
R ow
C ount
OUTPUT
]
[ ; ]
```

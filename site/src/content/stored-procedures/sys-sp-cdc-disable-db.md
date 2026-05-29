---
name: 'sys.sp_cdc_disable_db'
title: 'sys.sp_cdc_disable_db'
category: 'general'
description: 'Disables change data capture (CDC) for the current database. Change data capture isn''t'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

Requires membership in the

fixed server role for change data capture on Azure SQL

Managed Instance or SQL Server. Requires membership in the

for Change Data

Capture on Azure SQL Database.

The following example disables change data capture for the

database.

SQL

sys.sp_cdc_enable_db (Transact-SQL)

sys.sp_cdc_disable_table (Transact-SQL)

Related content

```sql
AdventureWorks2022
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_disable_db;
GO
```

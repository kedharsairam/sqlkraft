---
name: 'sys.sp_cdc_enable_db'
title: 'sys.sp_cdc_enable_db'
category: 'general'
description: 'Enables change data capture for the current database. This procedure must be executed for a'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

creates the change data capture objects that have database wide scope,

including metadata tables and DDL triggers. It also creates the CDC schema and CDC database

user and sets the

column for the database entry in the

sys.databases

catalog

view to

.

Requires membership in the

fixed server role for Change Data Capture on Azure SQL

Managed Instance or SQL Server. Requires membership in the

for Change Data

Capture on Azure SQL Database.

The following example enables change data capture.

SQL

sys.sp_cdc_disable_db (Transact-SQL)

Related content

```sql
sys.sp_cdc_enable_db
```

```sql
is_cdc_enabled
```

```sql
1
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_enable_db;
GO
```

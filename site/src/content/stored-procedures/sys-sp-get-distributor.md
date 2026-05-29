---
name: "sys.sp_get_distributor"
title: "sp_get_distributor"
category: "general"
description: "Determines whether a Distributor is installed on a server. This stored procedure is executed at the computer where the Distributor is being looked for, on any database. Transact-SQL syntax conventions Name of the Distributor server is used primarily by the SQL Server Management Studio in snapshot, transactional, and merge replication."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "distribution db installed"
---

## Description

Determines whether a Distributor is installed on a server. This stored procedure is executed at the computer where the Distributor is being looked for, on any database. Transact-SQL syntax conventions Name of the Distributor server is used primarily by the SQL Server Management Studio in snapshot, transactional, and merge replication.

## Syntax

```sql
distribution db installed
```

## Permissions

Any user can execute . A non-NULL result set is returned when this stored procedure is executed by members of the or fixed database roles on the distribution database, or members of the fixed database role on at least one published database. A non-NULL result set is also returned when this stored procedure is executed by users in the publication access list (PAL) of at least one published database, or in the PAL of the distribution database for a non-SQL Server Publisher, can also execute . Configure Publishing and Distribution Distributor and Publisher Information Script Replication stored procedures (Transact-SQL) Related content

## Remarks

Applies to:

Determines whether a Distributor is installed on a server. This stored procedure is executed at

the computer where the Distributor is being looked for, on any database.

Transact-SQL syntax conventions

Description

Name of the Distributor server

is used primarily by the SQL Server Management Studio in snapshot,

transactional, and merge replication.

Expand table

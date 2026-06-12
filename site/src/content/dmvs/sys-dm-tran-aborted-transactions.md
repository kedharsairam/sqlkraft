---
name: "sys.dm_tran_aborted_transactions"
title: "sys.dm_tran_aborted_transactions"
category: "io"
description: "2019 (15.x) and later versions SQL database in Microsoft Fabric Returns information about unresolved, aborted transactions in the Database Engine instance. In Azure SQL Database, the values are unique within a single database or an elastic pool, but not within a logical server. The starting LSN of the aborted transaction. The ending LSN of the aborted transaction."
tags: ["io","dmv"]
pubDate: "2026-05-29"
syntax: "##MS_ServerStateReader##"
---

## Description

2019 (15.x) and later versions SQL database in Microsoft Fabric Returns information about unresolved, aborted transactions in the Database Engine instance. In Azure SQL Database, the values are unique within a single database or an elastic pool, but not within a logical server. The starting LSN of the aborted transaction. The ending LSN of the aborted transaction. The begin time of the aborted transaction.

## Syntax

```sql
##MS_ServerStateReader##
```

## Permissions

2019 (15.x) and later versions SQL database in Microsoft Fabric Returns information about unresolved, aborted transactions in the Database Engine instance. The of the aborted transaction. The of the aborted transaction. In Azure SQL Database, the values are unique within a single database or an elastic pool, but not within a logical server. The starting LSN of the aborted transaction. The ending LSN of the aborted transaction. The begin time of the aborted transaction. When 1, indicates that the transaction has a nested aborted transaction. On SQL Server and SQL Managed Instance, requires permission. On SQL Database , , and service objectives, and for databases in , the server admin account, the Microsoft Entra admin account, or membership in the server role is required. On all other SQL Database service objectives, either the permission on the database, or membership in the server role is required. Requires permission on the server. ﾉ

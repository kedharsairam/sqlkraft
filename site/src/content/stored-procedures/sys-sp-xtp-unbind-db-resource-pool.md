---
name: "sys.sp_xtp_unbind_db_resource_pool"
title: "sys.sp_xtp_unbind_db_resource_pool"
category: "general"
description: "This system procedure removes an existing binding between a database and a resource pool for purposes of tracking In-Memory OLTP memory usage. If there's no pool currently bound to the specified database, success is returned. When the database is unbound, the previously allocated memory for memory-optimized objects stays allocated to the previous resource pool. You need to restart the database to "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_xtp_unbind_db_resource_pool"
---

## Description

This system procedure removes an existing binding between a database and a resource pool for purposes of tracking In-Memory OLTP memory usage. If there's no pool currently bound to the specified database, success is returned. When the database is unbound, the previously allocated memory for memory-optimized objects stays allocated to the previous resource pool. You need to restart the database to free up the allocated memory. Once a database is unbound

## Syntax

```sql
sp_xtp_unbind_db_resource_pool
```

---
name: "sys.fn_virtualservernodes"
title: "sys.fn_virtualservernodes"
category: "system"
description: "Returns a list of failover clustered instance nodes on which an instance of SQL Server can run. This information is useful in failover clustering environments. Transact-SQL syntax conventions If the current server is a clustered server, clustered instance nodes on which this instance of SQL Server has been defined. If the current server instance is not a clustered server, The user must have VIEW S"
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: "fn_virtualservernodes"
---

## Description

Returns a list of failover clustered instance nodes on which an instance of SQL Server can run. This information is useful in failover clustering environments. Transact-SQL syntax conventions If the current server is a clustered server, clustered instance nodes on which this instance of SQL Server has been defined. If the current server instance is not a clustered server, The user must have VIEW SERVER STATE permission for the instance of SQL Server.

## Syntax

`fn_virtualservernodes`

## Examples

### Example 1

`fn_virtualservernodes`

### Example 2

`fn_virtualservernodes()`

### Example 3

```sql
SELECT * FROM fn_virtualservernodes();
```

---
name: "sys.sp_get_redirected_publisher"
title: "sp_get_redirected_publisher"
category: "general"
description: "Used by replication agents to query a distributor to determine whether the original publisher The name of the instance of SQL Server that originally published the database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_get_redirected_publisher
  [ @original_publisher = ]
  N
  'original_publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  [ , [ @bypass_publisher_validation = ] bypass_publisher_validation ]
  [ , [ @multi_subnet_failover = ] multi_subnet_failover ]
  [ ; ]
---

## Description

Used by replication agents to query a distributor to determine whether the original publisher The name of the instance of SQL Server that originally published the database.

## Syntax

```sql
sp_get_redirected_publisher
[ @original_publisher = ]
N
'original_publisher'
, [ @publisher_db = ]
N
'publisher_db'
[ , [ @bypass_publisher_validation = ] bypass_publisher_validation ]
[ , [ @multi_subnet_failover = ] multi_subnet_failover ]
[ ; ]
```

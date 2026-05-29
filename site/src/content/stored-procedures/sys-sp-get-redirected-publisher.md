---
name: 'sys.sp_get_redirected_publisher'
title: 'sp_get_redirected_publisher'
category: 'general'
description: 'Used by replication agents to query a distributor to determine whether the original publisher Transact-SQL syntax conventions The name of the instance of SQL Server that originally published the database. The name of the database being published. Used to bypass validation of the redirected publisher. If SQL Server 2022 (16.x) CU 10 and later versions'
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

Used by replication agents to query a distributor to determine whether the original publisher Transact-SQL syntax conventions The name of the instance of SQL Server that originally published the database. The name of the database being published. Used to bypass validation of the redirected publisher. If SQL Server 2022 (16.x) CU 10 and later versions

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

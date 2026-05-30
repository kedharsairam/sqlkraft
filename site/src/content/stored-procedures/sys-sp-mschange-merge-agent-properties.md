---
name: "sys.sp_mschange_merge_agent_properties"
title: "sp_MSchange_merge_agent_properties"
category: "general"
description: "Changes the properties of a Merge Agent job that runs at a SQL Server 2005 (9.x) or later version Distributor. This stored procedure is used to change properties when the Publisher runs on an instance of SQL Server 2000 (8.x). This stored procedure is executed at the Distributor on Transact-SQL syntax conventions The name of the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_
  MS
  change_merge_agent_properties
  [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  , [ @subscriber = ]
  N
  'subscriber'
  , [ @subscriber_db = ]
  N
  'subscriber_db'
  , [ @property = ]
  N
  'property'
  , [ @value = ]
  N
  'value'
  [ ; ]
---

## Description

Changes the properties of a Merge Agent job that runs at a SQL Server 2005 (9.x) or later version Distributor. This stored procedure is used to change properties when the Publisher runs on an instance of SQL Server 2000 (8.x). This stored procedure is executed at the Distributor on Transact-SQL syntax conventions The name of the publication database.

## Syntax

```sql
sp_
MS
change_merge_agent_properties
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
, [ @subscriber = ]
N
'subscriber'
, [ @subscriber_db = ]
N
'subscriber_db'
, [ @property = ]
N
'property'
, [ @value = ]
N
'value'
[ ; ]
```

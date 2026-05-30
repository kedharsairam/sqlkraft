---
name: "sys.sp_mschange_logreader_agent_properties"
title: "sp_MSchange_logreader_agent_properties"
category: "general"
description: "Changes the properties of a Log Reader Agent job that runs at a SQL Server 2005 (9.x) or later version Distributor. This stored procedure is used to change properties when the Publisher runs on an instance of SQL Server 2000 (8.x). This stored procedure is executed at the Distributor on Transact-SQL syntax conventions The name of the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_
  MS
  change_logreader_agent_properties
  [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publisher_security_mode = ] publisher_security_mode
  , [ @publisher_login = ]
  N
  'publisher_login'
  , [ @publisher_password = ]
  N
  'publisher_password'
  , [ @job_login = ]
  N
  'job_login'
  , [ @job_password = ]
  N
  'job_password'
  , [ @publisher_type = ]
  N
  'publisher_type'
  [ ; ]
---

## Description

Changes the properties of a Log Reader Agent job that runs at a SQL Server 2005 (9.x) or later version Distributor. This stored procedure is used to change properties when the Publisher runs on an instance of SQL Server 2000 (8.x). This stored procedure is executed at the Distributor on Transact-SQL syntax conventions The name of the publication database.

## Syntax

```sql
sp_
MS change_logreader_agent_properties
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publisher_security_mode = ] publisher_security_mode
, [ @publisher_login = ]
N
'publisher_login'
, [ @publisher_password = ]
N
'publisher_password'
, [ @job_login = ]
N
'job_login'
, [ @job_password = ]
N
'job_password'
, [ @publisher_type = ]
N
'publisher_type'
[ ; ]
```

## Permissions

For more information about the differences between an Oracle Publisher and an Oracle Gateway Publisher, see Oracle Publishing Overview . is used in transactional replication. You must specify all parameters when executing . Execute sp_helplogreader_agent to return the current properties of the Log Reader Agent job. After changing an agent login or password, you must stop and restart the agent before the change takes effect. You can use sp_changelogreader_agent on the Publisher to change properties of the Log Reader Agent. Only members of the fixed server role at the Distributor can execute . sp_addlogreader_agent (Transact-SQL) Related content

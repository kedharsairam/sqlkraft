---
name: "sys.sp_addlogreader_agent"
title: "sp_addlogreader_agent"
category: "general"
description: "Adds a Log Reader agent for a given database. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The login for the Windows account under which the agent runs. This Windows account is always used for agent connections to the Distributor. On Azure SQL Managed Instance, use a SQL Server account. When configuring a Publisher with a remote"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addlogreader_agent
  [ [ @job_login = ]
  N
  'job_login'
  ]
  [ , [ @job_password = ]
  N
  'job_password'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @publisher_security_mode = ] publisher_security_mode ]
  [ , [ @publisher_login = ]
  N
  'publisher_login'
  ]
  [ , [ @publisher_password = ]
  N
  'publisher_password'
  ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Adds a Log Reader agent for a given database. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The login for the Windows account under which the agent runs. . This Windows account is always used for agent connections to the Distributor. On Azure SQL Managed Instance, use a SQL Server account. When configuring a Publisher with a remote Distributor, the values supplied for all

## Syntax

```sql
sp_addlogreader_agent
[ [ @job_login = ]
N
'job_login'
]
[ , [ @job_password = ]
N
'job_password'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @publisher_security_mode = ] publisher_security_mode ]
[ , [ @publisher_login = ]
N
'publisher_login'
]
[ , [ @publisher_password = ]
N
'publisher_password'
]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute . Windows authentication logins must have a user account in the database representing their Windows user account. A user account representing a Windows group isn't sufficient. sp_addlogreader_agent (Transact-SQL) sp_addpublication_snapshot (Transact-SQL) sp_changepublication (Transact-SQL) sp_droppublication (Transact-SQL) sp_helppublication (Transact-SQL) sp_replicationdboption (Transact-SQL) Publish Data and Database Objects Related content Only members of the fixed server role or fixed database role can execute . Create a publication Create and Apply the Initial Snapshot sp_addpublication (Transact-SQL) sp_changepublication_snapshot (Transact-SQL) sp_startpublication_snapshot (Transact-SQL) Replication stored procedures (Transact-SQL) Related content

## Examples

### Example 1

`sp_addlogreader_agent`

### Example 2

```sql
-- To avoid storing the login and password in the script file, the values
-- are passed into SQLCMD as scripting variables. For information about
-- how to use scripting variables on the command line and in SQL Server
-- Management Studio, see the "Executing Replication Scripts" section in
-- the topic "Programming Replication Using System Stored Procedures".
DECLARE
@publicationDB
AS sysname;
DECLARE
@publication
AS sysname;
DECLARE
@login
AS sysname;
DECLARE
@
password
AS sysname;
SET
@publicationDB = N
'AdventureWorks'
;
SET
@publication = N
'AdvWorksProductTran'
;
-- Windows account used to run the Log Reader and Snapshot Agents.
SET
@login = $(Login);
-- This should be passed at runtime.
SET
@
password
= $(
Password
);
-- Enable transactional or snapshot replication on the publication database.
EXEC sp_replicationdboption
@dbname=@publicationDB,
@optname=N'publish',
@value = N'true';
-- Execute sp_addlogreader_agent to create the agent job.
EXEC sp_addlogreader_agent
@job_login = @login,
@job_password = @password,
-- Explicitly specify the use of Windows Integrated Authentication (default)
-- when connecting to the Publisher.
@publisher_security_mode = 1;
-- Create a new transactional publication with the required properties.
EXEC sp_addpublication
@publication = @publication,
@status = N'active',
@allow_push = N'true',
@allow_pull = N'true',
@independent_agent = N'true';
```

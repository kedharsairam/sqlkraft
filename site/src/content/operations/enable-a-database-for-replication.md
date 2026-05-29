---
title: "Enable a Database for Replication"
topic: "migration"
description: |
  Article
  
  •
  
  09/27/2024
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  A database is implicitly enabled for replication when a member of the
  
  fixed server
  
  role creates a publication with the Ne
tags:
  - "migration"
  - "enable-a-database-for-replication"
pubDate: 2025-12-01
---

Article

•

09/27/2024

Applies to:

SQL Server

Azure SQL Managed Instance

A database is implicitly enabled for replication when a member of the

fixed server

role creates a publication with the New Publication Wizard. A member of the

fixed

server role can also enable a database for replication explicitly, so that a member of the

fixed database role can create one or more publications in that database. To enable

a database explicitly, use the

page of the

dialog box. For more information about accessing this dialog box, see

Create a

Publication

.

1. On the

page of the

dialog

box, select the

and/or

check box for each database you want to

replicate. Select

to enable the database for snapshot replication.

2. Select

.

You can enable a database for replication with the following Transact-SQL code:

SQL

To disable publishing, set the @value = 'false'.

```cmd
USE
master
EXEC sp_replicationdboption @dbname =
'AdventureWorks2022'
,
@optname =
'publish'
,
@
value
=
'true'
GO
```
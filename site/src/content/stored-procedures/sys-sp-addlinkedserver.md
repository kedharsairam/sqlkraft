---
name: "sys.sp_addlinkedserver"
title: "sp_addlinkedserver"
category: "general"
description: "be specified in the parameter. Optionally, the connection string can also supply a failover partner name. from a local login, or a login that isn't part of the role, you might receive the following error: To resolve this issue, add the parameter to your connection string."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addlinkedserver
  [ @server = ]
  N
  'server'
  [ , [ @srvproduct = ]
  N
  'srvproduct'
  ]
  [ , [ @provider = ]
  N
  'provider'
  ]
  [ , [ @datasrc = ]
  N
  'datasrc'
  ]
  [ , [ @location = ]
  N
  'location'
  ]
  [ , [ @provstr = ]
  N
  'provstr'
  ]
  [ , [ @catalog = ]
  N
  'catalog'
  ]
  [ , [ @linkedstyle = ] linkedstyle ]
  [ ; ]
---

## Description

be specified in the parameter. Optionally, the connection string can also supply a failover partner name. from a local login, or a login that isn't part of the role, you might receive the following error: To resolve this issue, add the parameter to your connection string. In the following is the User ID passed to the connection string: For more information, see Access to the remote server is denied because no login-mapping The catalog to be used when a connection is made to the OLE DB provider. with a default of is passed as the property to initialize the OLE DB provider. When the linked server is defined against an instance of SQL Server, catalog refers to the default database to which the linked server is mapped. Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. source; there can be more than one row for a data source type. This table also shows the Removes an existing mapping between a login on the local server running SQL Server, and a Specifies that when a local transaction is active, executing a remote stored procedure starts a

## Syntax

```sql
sp_addlinkedserver
[ @server = ]
N
'server'
[ , [ @srvproduct = ]
N
'srvproduct'
]
[ , [ @provider = ]
N
'provider'
]
[ , [ @datasrc = ]
N
'datasrc'
]
[ , [ @location = ]
N
'location'
]
[ , [ @provstr = ]
N
'provstr'
]
[ , [ @catalog = ]
N
'catalog'
]
[ , [ @linkedstyle = ] linkedstyle ]
[ ; ]
```

## Arguments

Applies to:

Azure SQL Managed Instance

Creates a linked server. A linked server provides access to distributed, heterogeneous queries

against OLE DB data sources. After a linked server is created by using

distributed queries can be run against this server. If the linked server is defined as an instance of

SQL Server, remote stored procedures can be executed.

Transact-SQL syntax conventions

The name of the linked server to create.

, with no default.

The product name of the OLE DB data source to add as a linked server.

@srvproduct

nvarchar(128)

, with a default of

. If the value is

don't have to be specified.

The unique programmatic identifier (PROGID) of the OLE DB provider that corresponds to this

data source. The

must be unique for the specified OLE DB provider installed on the

current computer.

nvarchar(128)

, with a default of

In SQL Server 2019 (15.x) and earlier versions, if

is omitted,

will redirect SQL Server to the latest version of SQL Server Native Client OLE

Microsoft Entra ID

was previously known as Azure Active Directory (Azure AD).

## Permissions

database of the server (mssqlsystemresource). The resource database is read-only. A link to the object is exposed as a record in the sys schema of every database. Permission to execute or select a system object can be granted, denied, and revoked. Granting permission to execute or select an object doesn't necessarily convey all the permissions required to use the object. Most objects perform operations for which extra permissions are required. For example, a user that is granted permission on can't create a linked server unless the user is also a member of the fixed server role. Default name resolution resolves unqualified procedure names to the resource database. Therefore, the sys qualifier is only required when you're specifying catalog views and dynamic management views. Granting permissions on triggers and on columns of system objects isn't supported. Permissions on system objects are preserved during upgrades of SQL Server. You must be in the database to grant permissions, and the principal you grant the permissions to must be a user in the database. That is, if they're server-level permissions, you can't grant them to server principals, only database principals. System objects are visible in the sys.system_objects catalog view. The permissions on system objects are visible in the sys.database_permissions catalog view in the database. The following query returns information about permissions of system objects: SQL Requires CONTROL SERVER permission. completion of the transaction. When a subsequent COMMIT TRANSACTION or ROLLBACK TRANSACTION statement is issued for the connection, the controlling instance requests that MS DTC manage the completion of the distributed transaction across the computers involved. After a Transact-SQL distributed transaction has been started, remote stored procedure calls can be made to other instances of SQL Server that have been defined as remote servers. The remote servers are all enlisted in the Transact-SQL distributed transaction, and MS DTC ensures that the transaction is completed against each remote server. REMOTE_PROC_TRANSACTIONS is a connection-level setting that can be used to override the instance-level option. When REMOTE_PROC_TRANSACTIONS is OFF, remote stored procedure calls are not made part of a local transaction. The modifications made by the remote stored procedure are committed or rolled back at the time the stored procedure completes. Subsequent COMMIT TRANSACTION or ROLLBACK TRANSACTION statements issued by the connection that called the remote stored procedure have no effect on the processing done by the procedure. The REMOTE_PROC_TRANSACTIONS option is a compatibility option that affects only remote stored procedure calls made to instances of SQL Server defined as remote servers using . The option does not apply to distributed queries that execute a stored procedure on an instance defined as a linked server using . The setting of SET REMOTE_PROC_TRANSACTIONS is set at execute or run time and not at parse time. Requires membership in the role. BEGIN DISTRIBUTED TRANSACTION (Transact-SQL) SET Statements (Transact-SQL) See Also

## Remarks

be specified in the

parameter. Optionally, the connection string can

also supply a failover partner name.

from a local login, or a login that isn't part of the

role, you might receive the following error:

To resolve this issue, add the

parameter to your connection string. In the following

is the User ID passed to the connection string:

For more information, see

Access to the remote server is denied because no login-mapping

The catalog to be used when a connection is made to the OLE DB provider.

with a default of

is passed as the

property to initialize the

OLE DB provider. When the linked server is defined against an instance of SQL Server, catalog

refers to the default database to which the linked server is mapped.

Identified for informational purposes only. Not supported. Future compatibility is not guaranteed.

(success) or

The following table shows the ways that a linked server can be set up for data sources that can be

accessed through OLE DB. A linked server can be set up more than one way for a particular data

source; there can be more than one row for a data source type. This table also shows the

parameter values to be used for setting up the linked server.

data source

@srvproduct

Network name of SQL

Server (for default

instancename

(for specific instance)

Alias for the Oracle

Full path of Jet database

System DSN of ODBC

data source

File system

Indexing Service catalog

Spreadsheet

Full path of Excel file

Expand table

Applies to:

Removes an existing mapping between a login on the local server running SQL Server, and a

login on the linked server.

Transact-SQL syntax conventions

The name of a linked server that the SQL Server login mapping applies to.

@rmtsrvname

, with no default.

The SQL Server login on the local server that's a mapping to the linked server

@rmtsrvname

@locallogin

, with no default. A mapping for

@locallogin

@rmtsrvname

already exist. If

, the default mapping created by

, which maps all

logins on the local server to logins on the linked server, is deleted.

(success) or

Applies to:

Specifies that when a local transaction is active, executing a remote stored procedure starts a

Transact-SQL distributed transaction managed by Microsoft Distributed Transaction

Coordinator (MS DTC).

Transact-SQL syntax conventions

When ON, a Transact-SQL distributed transaction is started when a remote stored procedure is

executed from a local transaction. When OFF, calling remote stored procedures from a local

transaction does not start a Transact-SQL distributed transaction.

When REMOTE_PROC_TRANSACTIONS is ON, calling a remote stored procedure starts a

distributed transaction and enlists the transaction with MS DTC. The instance of SQL Server

making the remote stored procedure call is the transaction originator and controls the

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

This option is provided for backward compatibility for applications that use remote stored

procedures. Instead of issuing remote stored procedure calls, use distributed queries that

reference linked servers. These are defined by using

## Examples

### Example 1

`sp_addlinkedserver`

### Example 2

`sp_addlinkedsrvlogin`

### Example 3

`true`

### Example 4

`sp_addlinkedsrvlogin`

### Example 5

`sp_droplinkedsrvlogin`

### Example 6

`sp_addlinkedsrvlogin`

### Example 7

`sp_addlinkedsrvlogin`

### Example 8

`sp_addlinkedsrvlogin`

### Example 9

`SEATTLESales`

### Example 10

```sql
USE master
;
GO
EXECUTE sp_addlinkedserver
'SEATTLESales'
, N
'SQL Server'
;
GO
EXECUTE sp_testlinkedserver SEATTLESales;
GO
```

_(... and 6 more examples)_

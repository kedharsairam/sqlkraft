---
name: "sys.sp_addserver"
title: "sp_addserver"
category: "general"
description: "Defines the name of the local instance of SQL Server. When the computer hosting SQL Server is to inform the instance of the SQL Server Database Engine of the new computer name. This procedure must be executed on all instances of the Database Engine The instance name of the Database Engine can't be changed."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  <servername>\
  <instancename>
---

## Description

Defines the name of the local instance of SQL Server. When the computer hosting SQL Server is to inform the instance of the SQL Server Database Engine of the new computer name. This procedure must be executed on all instances of the Database Engine The instance name of the Database Engine can't be changed.

## Syntax

```sql
<servername>\
<instancename>
```

## Permissions

completion of the transaction. When a subsequent COMMIT TRANSACTION or ROLLBACK TRANSACTION statement is issued for the connection, the controlling instance requests that MS DTC manage the completion of the distributed transaction across the computers involved. After a Transact-SQL distributed transaction has been started, remote stored procedure calls can be made to other instances of SQL Server that have been defined as remote servers. The remote servers are all enlisted in the Transact-SQL distributed transaction, and MS DTC ensures that the transaction is completed against each remote server. REMOTE_PROC_TRANSACTIONS is a connection-level setting that can be used to override the instance-level option. When REMOTE_PROC_TRANSACTIONS is OFF, remote stored procedure calls are not made part of a local transaction. The modifications made by the remote stored procedure are committed or rolled back at the time the stored procedure completes. Subsequent COMMIT TRANSACTION or ROLLBACK TRANSACTION statements issued by the connection that called the remote stored procedure have no effect on the processing done by the procedure. The REMOTE_PROC_TRANSACTIONS option is a compatibility option that affects only remote stored procedure calls made to instances of SQL Server defined as remote servers using. The option does not apply to distributed queries that execute a stored procedure on an instance defined as a linked server using. The setting of SET REMOTE_PROC_TRANSACTIONS is set at execute or run time and not at parse time. Requires membership in the role. BEGIN DISTRIBUTED TRANSACTION (Transact-SQL) SET Statements (Transact-SQL) See Also

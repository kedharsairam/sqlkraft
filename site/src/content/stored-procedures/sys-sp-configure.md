---
name: 'sys.sp_configure'
title: 'sp_configure'
category: 'general'
description: 'Summarize this article for me Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Returns information about the current SET options. Transact-SQL syntax conventions The options can come from use of the command or from the value. Session values configured with the command override the Many tools, such as Management Studio, automatically configure set options. Each user ha'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_configure
  [ [ @configname = ]
  'configname'
  ]
  [ , [ @configvalue = ] configvalue ]
  [ ; ]
  sp_configure
  [ ; ]
---

## Description

Summarize this article for me Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Returns information about the current SET options. Transact-SQL syntax conventions The options can come from use of the command or from the value. Session values configured with the command override the Many tools, such as Management Studio, automatically configure set options. Each user has an function that represents the configuration. You can change the language and query-processing options for a specific user session by using can only detect the options that are set to ON or OFF. function returns a bitmap of the options, converted to a base 10 (decimal) integer. The bit settings are stored in the locations described in a table in the article the user options Server Configuration Option sp_configure (Transact-SQL) Azure SQL Managed Instance instead to specify the list of binary values that make up the file. sys.database_files CLR uses Code Access Security (CAS) in the .NET Framework, which is no longer supported as a Azure SQL Database

## Syntax

```sql
sp_configure
[ [ @configname = ]
'configname'
]
[ , [ @configvalue = ] configvalue ]
[ ; ]
sp_configure
[ ; ]
```

## Permissions

Disabling the setting only prevents direct recursions. To disable indirect recursion also, set the nested triggers server option to 0 by using . If any one of the triggers carries out a , regardless of the nesting level, no more triggers are run. You can nest triggers to a maximum of 32 levels. If a trigger changes a table on which there's another trigger, the second trigger activates and can then call a third trigger, and so on. If any trigger in the chain sets off an infinite loop, the nesting level is exceeded and the trigger is canceled. When a Transact-SQL trigger launches managed code by referencing a CLR routine, type, or aggregate, this reference counts as one level against the 32-level nesting limit. Methods invoked from within managed code don't count against this limit. To disable nested triggers, set the nested triggers option of to 0 (off). The default configuration supports nested triggers. If nested triggers are off, recursive triggers are also disabled, despite the setting that's set by using . The first trigger nested inside an trigger fires even if the server configuration option is 0. But, under this setting, the later triggers don't fire. Review your applications for nested triggers to determine if the applications follow your business rules when the server configuration option is set to 0. If not, make the appropriate modifications. SQL Server allows for Transact-SQL stored procedures, triggers, functions, and batches to refer to tables that don't exist at compile time. This ability is called deferred name resolution. To create a DML trigger, it requires permission on the table or view on which the trigger is being created. ７ Note The previous behavior occurs only if the setting is enabled by using . There's no defined order in which multiple triggers defined for a specific event are run. Each trigger should be self-contained. completion of the transaction. When a subsequent COMMIT TRANSACTION or ROLLBACK TRANSACTION statement is issued for the connection, the controlling instance requests that MS DTC manage the completion of the distributed transaction across the computers involved. After a Transact-SQL distributed transaction has been started, remote stored procedure calls can be made to other instances of SQL Server that have been defined as remote servers. The remote servers are all enlisted in the Transact-SQL distributed transaction, and MS DTC ensures that the transaction is completed against each remote server. REMOTE_PROC_TRANSACTIONS is a connection-level setting that can be used to override the instance-level option. When REMOTE_PROC_TRANSACTIONS is OFF, remote stored procedure calls are not made part of a local transaction. The modifications made by the remote stored procedure are committed or rolled back at the time the stored procedure completes. Subsequent COMMIT TRANSACTION or ROLLBACK TRANSACTION statements issued by the connection that called the remote stored procedure have no effect on the processing done by the procedure. The REMOTE_PROC_TRANSACTIONS option is a compatibility option that affects only remote stored procedure calls made to instances of SQL Server defined as remote servers using . The option does not apply to distributed queries that execute a stored procedure on an instance defined as a linked server using . The setting of SET REMOTE_PROC_TRANSACTIONS is set at execute or run time and not at parse time. Requires membership in the role. BEGIN DISTRIBUTED TRANSACTION (Transact-SQL) SET Statements (Transact-SQL) See Also

## Remarks

Summarize this article for me

Applies to:

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Returns information about the current SET options.

Transact-SQL syntax conventions

The options can come from use of the

command or from the

value. Session values configured with the

command override the

Many tools, such as Management Studio, automatically configure set options. Each user has an

function that represents the configuration.

You can change the language and query-processing options for a specific user session by using

can only detect the options that are set to ON or OFF.

function returns a bitmap of the options, converted to a base 10 (decimal)

integer. The bit settings are stored in the locations described in a table in the article

the user options Server Configuration Option

To decode the

value, convert the integer returned by

to binary, and then

look up the values on the table at

Configure the user options Server Configuration Option

example, if

returns the value

, use the Windows programmer calculator

) to convert decimal

to binary. The result is

. The rightmost

characters (binary 1, 2, and 4) are 0, indicating that the first three items in the table are off.

Consulting the table, you see that those are

sp_configure (Transact-SQL)

Configure the user options Server Configuration Option

Last updated on 02/10/2026

Applies to:

Azure SQL Managed Instance

Updates the currently configured value (the

column in the

set) of a configuration option changed with the

system stored procedure.

Because some configuration options require a server stop and restart to update the currently

running value, RECONFIGURE does not always update the currently running value (the

column in the

result set) for a changed configuration value.

Transact-SQL syntax conventions

RECONFIGURE

Specifies that if the configuration setting does not require a server stop and restart, the

currently running value should be updated. RECONFIGURE also checks the new configuration

values for either values that are not valid (for example, a sort order value that does not exist in

) or nonrecommended values. With those configuration options not requiring a

server stop and restart, the currently running value and the currently configured values for the

configuration option should be the same value after RECONFIGURE is specified.

WITH OVERRIDE

Disables the configuration value checking (for values that are not valid or for

nonrecommended values) for the

advanced configuration option.

Almost any configuration option can be reconfigured by using the WITH OVERRIDE option,

however some fatal errors are still prevented. For example, the

configuration option cannot be configured with a value greater than the value specified in the

configuration option.

instead to specify the list of binary values that make up the file.

specifies the name

under which the file should be stored in the instance of SQL Server.

specified if

is specified, and is optional if

client_file_specifier

is specified. If

isn't specified, the file_name part of

client_file_specifier

CLR uses Code Access Security (CAS) in the .NET Framework, which is no longer supported as a

security boundary. A CLR assembly created with

might be able to

access external system resources, call unmanaged code, and acquire sysadmin privileges. In

SQL Server 2017 (14.x) and later versions, the

clr strict security

the security of CLR assemblies.

is enabled by default, and treats

assemblies as if they were marked

can be disabled for backward compatibility, but isn't recommended.

We recommend that you sign all assemblies by a certificate or asymmetric key, with a

corresponding login that has been granted

permission in the

database. SQL Server administrators can also add assemblies to a list of assemblies, which the

Database Engine should trust. For more information, see

sys.sp_add_trusted_assembly

doesn't disrupt currently running sessions that are running code in the

assembly being modified. Current sessions complete execution by using the unaltered bits of

the assembly.

clause is specified,

updates the assembly with respect to the latest

copies of the modules provided. Because there might be CLR functions, stored procedures,

triggers, data types, and user-defined aggregate functions in the instance of SQL Server that

are already defined against the assembly, the

statement rebinds them to the

latest implementation of the assembly. To accomplish this rebinding, the methods that map to

CLR functions, stored procedures, and triggers must still exist in the modified assembly with

the same signatures. The classes that implement CLR user-defined types and user-defined

aggregate functions must still satisfy the requirements for being a user-defined type or

This option isn't available in a contained database or Azure SQL Database.

sp_configure

sp_spaceused

sys.databases

sys.database_files

sys.data_spaces

sys.filegroups

sys.master_files

System Databases

Last updated on 04/27/2026

CLR uses Code Access Security (CAS) in the .NET Framework, which is no longer supported as a

security boundary. A CLR assembly created with

might be able to

access external system resources, call unmanaged code, and acquire sysadmin privileges. In

SQL Server 2017 (14.x) and later versions, the

clr strict security

the security of CLR assemblies.

is enabled by default, and treats

assemblies as if they were marked

can be disabled for backward compatibility, but isn't recommended.

We recommend that you sign all assemblies by a certificate or asymmetric key, with a

corresponding login that has been granted

permission in the

database. SQL Server administrators can also add assemblies to a list of assemblies, which the

Database Engine should trust. For more information, see

sys.sp_add_trusted_assembly

uploads an assembly that was previously compiled as a .dll file from managed

code for use inside an instance of SQL Server.

When enabled, the

option in the

statements is ignored at run-time, but the

options are preserved in metadata.

Ignoring the option minimizes breaking existing code statements.

SQL Server doesn't allow registering different versions of an assembly with the same name,

culture, and public key.

When attempting to access the assembly specified in

, SQL Server

impersonates the security context of the current Windows login. If

specifies a network location (UNC path), the impersonation of

the current login isn't carried forward to the network location because of delegation

limitations. In this case, access is made using the security context of the SQL Server service

account. For more information, see

Credentials (Database Engine)

Besides the root assembly specified by

assembly_name

, SQL Server tries to upload any

assemblies that are referenced by the root assembly being uploaded. If a referenced assembly

is already uploaded to the database because of an earlier

statement, this

assembly isn't uploaded but is available to the root assembly. If a dependent assembly wasn't

previously uploaded, but SQL Server can't locate its manifest file in the source directory,

returns an error.

Applies to:

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Overrides the currently configured

value for the current connection.

Transact-SQL syntax conventions

Is a numeric or integer value specifying the highest estimated cost allowed for a given query to

run. Values are rounded down to the nearest integer. Negative values are rounded up to 0. The

query governor disallows execution of any query that has an estimated cost exceeding that

value. Specifying 0 (the default) for this option turns off the query governor, and all queries of

any cost are allowed to execute.

Query cost is an abstract figure determined by the query optimizer based on estimated

execution requirements such as cpu time, memory, and disk IO and refers to the estimated

elapsed time, in seconds, that would be required to complete a query on a specific hardware

configuration. This abstract figure does not equate to the time required to complete a query

on the running instance, and should instead be treated as a relative measure.

Using SET QUERY_GOVERNOR_COST_LIMIT applies to the current connection only and lasts the

duration of the current connection. Use the

Configure the query governor cost limit Server

Configuration Option

to change the server-wide query governor cost

limit value. For more information about configuring this option, see

sp_configure

Configuration Options (SQL Server)

## Examples

### Example 1

```sql
@@
MAX
_
CONNECTIONS
```

### Example 2

```sql
SELECT
@@MAX_CONNECTIONS
AS
'Max Connections'
;
```

### Example 3

```sql
Max Connections
---------------
32767
```

### Example 4

```sql
@@CURSOR_ROWS
```

### Example 5

```sql
sp_configure
```

### Example 6

```sql
0
```

### Example 7

```sql
SELECT
```

### Example 8

```sql
@@CURSOR_ROWS
```

### Example 9

```sql
0
```

### Example 10

```sql
-1
```


*(... and 11 more examples)*

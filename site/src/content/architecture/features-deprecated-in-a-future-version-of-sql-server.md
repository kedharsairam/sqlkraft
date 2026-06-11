---
title: "Features deprecated in a future version of SQL Server"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Category

Deprecated feature

Replacement

Feature name

Feature

ID

Compatibility Level as long as possible, to make the

upgrades easier. For more information about

compatibility levels, see

ALTER DATABASE (Transact-SQL)

compatibility level

.

Database

objects

Ability to return result sets from triggers

None

Returning results from

trigger

12

Encryption

Encryption using RC4 or RC4_128 is

deprecated and will be removed in the next

version. Decrypting RC4 and RC4_128 isn't

deprecated.

Use another encryption algorithm such as AES.

Deprecated encryption

algorithm

253

Hash

algorithms

Using the MD2, MD4, MD5, SHA, and SHA1 is

deprecated.

Use SHA2_256 or SHA2_512 instead. Older algorithms

continue working, but they raise a deprecation event.

Deprecated hash algorithm

None

Remote

servers

Replace remote servers by using linked servers.

can only be used with the local option.

70

69

71

72

73

Remote

servers

@@remserver

Replace remote servers by using linked servers.

None

None

Remote

servers

Replace remote servers by using linked servers.

110

Table hints

HOLDLOCK table hint without parenthesis.

Use HOLDLOCK with parenthesis.

HOLDLOCK table hint

without parenthesis

167

The following SQL Server Database Engine features are supported in the next version of SQL Server, but will be deprecated in a later version. The

specific version of SQL Server hasn't been determined.

Category

Deprecated feature

Replacement

Feature name

Compatibility

levels

.

For more information, see

ALTER DATABASE

(Transact-SQL) compatibility level

.

sp_dbcmptlevel

Compatibility

levels

Database compatibility level 110 and 120.

Plan to upgrade the database and application

for a future release. However, we continue to

support applications certified on any supported

database compatibility level as long as possible,

to make the upgrades easier. For more

information about compatibility levels, see

ALTER DATABASE (Transact-SQL) compatibility

level

.

Database compatibility l

Database compatibility l

XML

Inline XDR Schema Generation

The XMLDATA directive to the

option is

deprecated. Use XSD generation in the case of

and

modes. There's no replacement

for the XMLDATA directive in EXPLICT mode.

XMLDATA

XML

For more information, see

ALTER INDEX

.

sys.sp*db_selective_xml*

Backup and

restore

BACKUP { DATABASE | LOG } TO TAPE

BACKUP { DATABASE | LOG } TO

device_that_is_a_tape

BACKUP { DATABASE | LOG } TO DISK

BACKUP DATABASE or LO

ﾉ

Expand table

Category

Deprecated feature

Replacement

Feature name

BACKUP { DATABASE | LOG } TO

device_that_is_a_disk

Backup and

restore

Backup and

restore

Collations

Korean_Wansung_Unicode

Lithuanian_Classic

SQL_AltDiction_CP1253_CS_AS

None. These collations exist in SQL Server 2005

(9.x), but aren't visible through

fn_helpcollations.

Korean_Wansung_Unico

Lithuanian_Classic

SQL*AltDiction_CP1253*

Collations

Hindi

Macedonian

These collations exist in SQL Server 2005 (9.x)

and higher, but aren't visible through

fn_helpcollations. Use Macedonian_FYROM_90

and Indic_General_90 instead.

Hindi

Macedonian

Collations

Azeri_Latin_90

Azeri_Cyrilllic_90

Azeri_Latin_100

Azeri_Cyrilllic_100

Azeri_Latin_90

Azeri_Cyrilllic_90

Configuration

and

database option

and

database option

and

database option

None.

,

and

CONCAT_NULLS_YIELDS_NULL are always set to

.

will be unavailable.

Data types

Data types

timestamp

## syntax for

rowversion

data type

rowversion

data type syntax

Data types

Ability to insert null values into

timestamp

columns.

Use a

instead.

into

Data types

'text in row' table option

Use

varchar(max)

,

nvarchar(max)

, and

varbinary(max)

data types. For more

information, see

sp_tableoption

.

Text in row table option

Data types

Data types:

text

ntext

image

Use

varchar(max)

,

nvarchar(max)

, and

varbinary(max)

data types.

Data types:

text

,

ntext

, o

Database

management

statement with the

option. To rebuild multiple log files,

when one or more have a new location, use the

option.

sp_attach_single_file_db

Database

objects

sp_bindefault

keyword in

and

CREATE_DROP_DEFAULT

Category

Deprecated feature

Replacement

Feature name

Database

objects

keyword in

and

CREATE_DROP_RULE

Database

objects

Use

.

Database

objects

and

Database

objects

in

Database

objects

Use MARS or distributed transactions.

Database

options

Use MARS or distributed transactions.

Database

options

{

|

}

Database

options

option of

option of

DBCC

DBCC DBREINDEX

option of

.

DBCC DBREINDEX

DBCC

DBCC INDEXDEFRAG

option of

DBCC INDEXDEFRAG

DBCC

DBCC SHOWCONTIG

DBCC SHOWCONTIG

DBCC

DBCC PINTABLE

DBCC UNPINTABLE

Has no effect.

DBCC [UN]PINTABLE

Extended

properties

Level0type = 'type' and Level0type = 'USER' to add extended properties to

level-1 or level-2 type objects.

Use Level0type = 'USER' only to add an

extended property directly to a user or role.

Use Level0type = '

' to add an extended

property to level-1 types such as

or

VIEW, or level-2 types such as COLUMN or

TRIGGER. For more information, see

sp_addextendedproperty

.

EXTPROP_LEVEL0

EXTPROP_LEVEL0USER

Extended

stored

procedure

programming

srv_alloc

srv_convert

srv_describe

srv_getbindtoken

srv_got_attention

srv_message_handler

srv_paramdata

srv_paraminfo

srv_paramlen

srv_parammaxlen

srv_paramname

srv_paramnumber

srv_paramset

Use CLR Integration instead.

Category

Deprecated feature

Replacement

Feature name

srv_paramsetoutput

srv_paramstatus

srv_paramtype

srv_pfield

srv_pfieldex

srv_rpcdb

srv_rpcname

srv_rpcnumber

srv_rpcoptions

srv_rpcowner

srv_rpcparams

srv_senddone

srv_sendmsg

srv_sendrow

srv_setcoldata

srv_setcollen

srv_setutype

srv_willconvert

srv_wsendmsg

Extended

stored

procedure

programming

Use CLR Integration instead.

Extended

stored

procedures

Use

Use

argument of

Functions

fn_get_sql

fn_get_sql

High

availability

database mirroring

Always On availability groups

If your edition of SQL Server doesn't support

Always On availability groups, use log shipping.

DATABASE_MIRRORING

Index options

Index options

,

, or

## syntax without parentheses

around the options.

Rewrite the statement to use the current syntax.

INDEX_OPTION

Instance

options

option 'allow updates'

System tables are no longer updatable. Setting

has no effect.

'allow upd

Instance

options

options:

'locks'

'open objects'

Now automatically configured. Setting has no

effect.

'locks'

'open obje

'set workin

Category

Deprecated feature

Replacement

Feature name

'set working set size'

Instance

options

option 'priority boost'

System tables are no longer updatable. Setting

has no effect. Use the Windows

option instead.

'priority bo

Instance

options

option 'remote proc trans'

System tables are no longer updatable. Setting

has no effect.

'remote pr

Linked

servers

Specifying the SQLOLEDB provider for linked servers.

Microsoft OLE DB Driver for SQL Server

SQLOLEDB for linked ser

Locking

Metadata

FILE_ID

INDEXKEY_PROPERTY

FILE_IDEX

FILE_ID

INDEXKEY_PROPERTY

Native XML

Web Services

The

or

statement with the

option.

sys.endpoint_webmethods

sys.soap_endpoints

Use Windows Communications Foundation

(WCF) or ASP.NET instead.

/

sys.endpoint_webmetho

EXT_soap_endpoints

Removable

databases

Removable

databases

Security

The

## syntax

Replaced by the new

and

## syntax

Security

Security

Security

Security

Security

Security

Security

or

Security

A master key must exist and password must be

correct.

Security

Security

Category

Deprecated feature

Replacement

Feature name

sp_revokelogin

Security

USER_ID

DATABASE_PRINCIPAL_ID

USER_ID

Security

These stored procedures return information

that was correct in SQL Server 2000 (8.x). The

output doesn't reflect changes to the

## permissions hierarchy implemented in SQL

Server 2008 (10.0.x). For more information, see

## Permissions of Fixed Server Roles

.

Security

,

, and

specific permissions.

ALL Permission

Security

## PERMISSIONS intrinsic function

Query

instead.

## PERMISSIONS

Security

SETUSER

SETUSER

Security

RC4 and

encryption algorithms

Use another algorithm such as AES.

algorithm

options

sys.dm_exec_describe_first_result_set

,

sys.dm_exec_describe_first_result_set_for_object

,

sp_describe_first_result_set

, and

sp_describe_undeclared_parameters

.

Server

Configuration

Options

c2 audit option

default trace enabled option

common criteria compliance enabled Server

Configuration Option

Extended Events overview

'c2 audit m

'default tra

SMO classes

class

class

class

property

class

class

class

None

None

SQL Server

Agent

net send

notification

Pager notification

E-mail notification

E-mail notification

None

SQL Server

Management

Studio

Solution Explorer integration in SQL Server Management Studio

None

System

Stored

Procedures

None. Support for increased partitions is now

available by default.

System tables

sysaltfiles

syscacheobjects

syscolumns

syscomments

sysconfigures

sysconstraints

syscurconfigs

sysdatabases

sysdepends

Compatibility views. For more information, see

System Compatibility Views

.

Important:

The compatibility views don't

expose metadata for features that were

introduced in SQL Server 2005 (9.x). We

recommend that you upgrade your applications

to use catalog views. For more information, see

System catalog views

.

sysaltfiles

syscacheobjects

syscolumns

syscomments

sysconfigures

sysconstraints

syscurconfigs

sysdatabases

sysdepends

Category

Deprecated feature

Replacement

Feature name

sysdevices

sysfilegroups

sysfiles

sysforeignkeys

sysfulltextcatalogs

sysindexes

sysindexkeys

syslockinfo

syslogins

sysmembers

sysmessages

sysobjects

sysoledbusers

sysopentapes

sysperfinfo

syspermissions

sysprocesses

sysprotects

sysreferences

sysremotelogins

sysservers

systypes

sysusers

sysdevices

sysfilegroups

sysfiles

sysforeignkeys

sysfulltextcatalogs

sysindexes

sysindexkeys

syslockinfo

syslogins

sysmembers

sysmessages

sysobjects

sysoledbusers

sysopentapes

sysperfinfo

syspermissions

sysprocesses

sysprotects

sysreferences

sysremotelogins

sysservers

systypes

sysusers

System tables

None

numbered_procedures

numbered_procedure_pa

System

functions

fn_virtualservernodes

fn_servershareddrives

fn_virtualservernodes

fn_servershareddrives

System views

Table

compression

The use of the vardecimal storage format.

Vardecimal storage format is deprecated. Data

compression in this version compresses decimal

values and other data types. We recommend

that you use data compression instead of the

vardecimal storage format.

Vardecimal storage form

Table

compression

Use of the

procedure.

Vardecimal storage format is deprecated. The

SQL Server data compression feature

compresses decimal values as well as other data

types. We recommend that you use data

compression instead of the vardecimal storage

format.

Table

compression

Use of the

procedure.

Use data compression and the

Category

Deprecated feature

Replacement

Feature name

procedure instead.

Table hints

Specifying

or

in the

clause of an

or

statement.

Remove the

or

table

hints from the

clause.

or

Table hints

Specifying table hints without using the

keyword.

Use

.

Table hint without

Table hints

INSERT_HINTS

INSERT_HINTS

Text pointers

WRITETEXT

UPDATETEXT

READTEXT

None

UPDATETEXT or WRITET

READTEXT

Text pointers

TEXTPTR()

TEXTVALID()

None

TEXTPTR

TEXTVALID

Transact-SQL

function-calling sequence

Replaced by

.

For example, replace

with

.

'::' function calling syntax

Transact-SQL

Three-part and four-part column references.

Two-part names is the standard-compliant

behavior.

More than two-part colu

Transact-SQL

A string enclosed in quotation marks used as a column alias for an

expression in a

list:

'

string_alias

' =

expression

expression

[AS]

column_alias

expression

[AS] [

column_alias

]

expression

[AS] "

column_alias

"

expression

[AS] '

column_alias

'

column_alias

=

expression

String literals as column

Transact-SQL

Numbered procedures

None. Don't use.

ProcNums

Transact-SQL

table_name.index_name

## syntax in

index_name

table_name

## syntax in

.

with two-pa

Transact-SQL

Not ending Transact-SQL statements with a semicolon.

End Transact-SQL statements with a semicolon

(

).

None

Transact-SQL

Use custom case-by-case solution with

or derived table.

Transact-SQL

as a column name in DML statements.

Use $rowguid.

Transact-SQL

IDENTITYCOL as a column name in DML statements.

Use $identity.

IDENTITYCOL

Transact-SQL

Use of #, ## as temporary table and temporary stored procedure names.

Use at least one additional character.

'#' and '##' as the name

and stored procedures

Transact-SQL

Use of @ or @@ as Transact-SQL identifiers.

Don't use @ or @@ or names that begin with

@@ as identifiers.

'@' and names that start

SQL identifiers

Transact-SQL

Use of

keyword as default value.

Don't use the word

as a default value.

keyword as a de

Transact-SQL

Use of a space as a separator between table hints.

Use a comma to separate table hints.

Multiple table hints with

Transact-SQL

The select list of an aggregate indexed view must contain COUNT_BIG (\*) in

90 compatibility mode

Use COUNT_BIG (\*).

Index view select list wit

Transact-SQL

The indirect application of table hints to an invocation of a multi-statement

table-valued function (TVF) through a view.

None.

Indirect TVF hints

Transact-SQL

## syntax:

Category

Deprecated feature

Replacement

Feature name

Other

DB-Library

Embedded SQL for C

Although the Database Engine still supports

connections from existing applications that use

the DB-Library and Embedded SQL APIs, it

doesn't include the files or documentation

required to do programming work on

applications that use these APIs. A future

version of the SQL Server Database Engine will

drop support for connections from DB-Library

or Embedded SQL applications. Don't use DB-

Library or Embedded SQL to develop new

applications. Remove any dependencies on

either DB-Library or Embedded SQL when you

modify existing applications. Instead of these

APIs, use the SQLClient namespace or an API

such as ODBC. The current version doesn't

include the DB-Library DLL required to run

these applications. To run DB-Library or

Embedded SQL applications, you must have

available the DB-Library DLL from SQL Server

version 6.5, SQL Server 7.0, or SQL Server 2000

(8.x).

None

Tools

SQL Server Profiler for Trace Capture

Use Extended Events Profiler embedded in SQL

Server Management Studio.

SQL Server Profiler

Tools

SQL Server Profiler for Trace Replay

SQL Server Distributed Replay overview

SQL Server Profiler

Trace

Management

Objects

Microsoft.SqlServer.Management.Trace namespace (contains the APIs for

SQL Server Trace and Replay objects)

Trace Configuration:

Microsoft.SqlServer.Management.XEvent

Trace Reading:

Microsoft.SqlServer.XEvent.Linq

Trace Replay: None

SQL Trace

stored

procedures,

functions,

and catalog

views

fn_trace_geteventinfo

fn_trace_getfilterinfo

fn_trace_getinfo

fn_trace_gettable

sys.trace_categories

sys.trace_columns

sys.trace_subclass_values

Extended Events overview

fn_trace_geteventinfo

fn_trace_getfilterinfo

fn_trace_getinfo

fn_trace_gettable

Set options

for

,

, and

statements

keyword

７

Note

The cookie

parameter for

is currently documented as

varbinary(8000)

which is the correct maximum length. However

the current implementation returns

varbinary(50)

. If developers have allocated

varbinary(50)

the application might require changes if the

Discontinued Database Engine functionality in SQL Server

Deprecated Database Engine features in SQL Server 2017 (14.x)

Last updated on 11/18/2025

cookie return size increases in a future release. Though not a deprecation issue this is mentioned in this topic because the application

adjustments are similar. For more information, see

sp_setapprole

.

Related content

```sql
sp_addremotelogin sp_addserver sp_dropremotelogin sp_helpremotelogin sp_remoteoption
```

`sp_addserver`

```sql
sp_addremotelogin sp_addserver sp_dropremotelogin sp_helpremotelogin sp_remoteoption
```

```sql
SET REMOTE_PROC_TRANSACTIONS
```

```sql
SET
REMOTE_PROC_TRANSACTIONS
```

```sql
sp_dbcmptlevel
ALTER DATABASE ... SET COMPATIBILITY_LEVEL
```

```sql
FOR XML
```

`RAW`

`AUTO`

```sql
sys.sp_db_selective_xml_index
ALTER INDEX ... DISABLE
```

```sql
sp_addumpdevice 'tape'
sp_addumpdevice 'disk'
ADDING TAPE DEVICE
```

```sql
sp_helpdevice sys.backup_devices sp_helpdevice
```

```sql
SET ANSI_NULLS OFF
```

```sql
ANSI_NULLS OFF
```

```sql
SET ANSI_PADDING OFF
```

```sql
ANSI_PADDING OFF
```

```sql
SET CONCAT_NULL_YIELDS_NULL OFF
```

```sql
CONCAT_NULL_YIELDS_NULL OFF
```

```sql
SET OFFSETS
```

`ANSI_NULLS`

`ANSI_PADDING`

`ON`

```sql
SET OFFSETS
```

```sql
SET ANSI_NULLS OFF
SET ANSI_PADDING OFF
SET CONCAT_NULL_YIELDS_
SET OFFSETS
ALTER DATABASE SET ANSI
ALTER DATABASE SET ANSI
ALTER DATABASE SET CONC
OFF
```

```sql
sp_addtype sp_droptype
CREATE TYPE
DROP TYPE sp_addtype sp_droptype
```

`TIMESTAMP`

`DEFAULT`

```sql
INSERT NULL
```

`TIMEST`

```sql
sp_attach_db sp_attach_single_file_db
CREATE DATABASE
```

```sql
FOR
ATTACH
```

```sql
FOR ATTACH_REBUILD_LOG
```

`sp_attach_db`

```sql
CREATE DEFAULT
DROP DEFAULT
```

```sql
sp_unbindefault
DEFAULT
```

```sql
CREATE TABLE
```

```sql
ALTER
TABLE
```

```sql
sp_bindefault sp_unbindefault
```

```sql
CREATE RULE
DROP RULE sp_bindrule sp_unbindrule
CHECK
```

```sql
CREATE TABLE
```

```sql
ALTER
TABLE
```

```sql
sp_bindrule sp_unbindrule
```

`sp_change_users_login`

```sql
ALTER USER
```

`sp_change_users_login`

```sql
sp_depends sys.dm_sql_referencing_entities
```

```sql
sys.dm_sql_referenced_entities sp_depends
```

```sql
sp_renamedb
MODIFY NAME
```

```sql
ALTER DATABASE sp_renamedb
```

`sp_getbindtoken`

`sp_getbindtoken`

`sp_bindsession`

`sp_bindsession`

```sql
sp_resetstatus
ALTER DATABASE SET
```

`ONLINE`

`EMERGENCY`

`sp_resetstatus`

`TORN_PAGE_DETECTION`

```sql
ALTER DATABASE
PAGE_VERIFY TORN_PAGE_DETECTION
```

```sql
ALTER DATABASE
ALTER DATABASE WITH TOR
```

`REBUILD`

```sql
ALTER INDEX
```

`REORGANIZE`

```sql
ALTER INDEX
```

`sys.dm_db_index_physical_stats`

`SCHEMA`

`TABLE`

`TYPE`

`XP_API`

```sql
sp_addextendedproc sp_dropextendedproc sp_helpextendedproc
```

```sql
sp_addextendedproc sp_dropextendedproc sp_helpextendedproc
```

```sql
xp_grantlogin xp_revokelogin xp_loginConfig
```

```sql
CREATE LOGIN
```

```sql
DROP LOGIN IsIntegratedSecurityOnly
```

```sql
SERVERPROPERTY xp_grantlogin xp_revokelogin xp_loginconfig
```

`sys.dm_exec_sql_text`

```sql
sp_indexoption
ALTER INDEX sp_indexoption
```

```sql
CREATE TABLE
```

```sql
ALTER TABLE
```

```sql
CREATE INDEX
```

`sp_configure`

`sp_configure`

`sp_configure`

`sp_configure`

`sp_configure`

`sp_configure`

`sp_configure`

```sql
start /high
... program.exe
```

`sp_configure`

`sp_configure`

`sp_configure`

```sql
sp_lock sys.dm_tran_locks sp_lock
```

`sys.index_columns`

```sql
CREATE ENDPOINT
```

```sql
ALTER ENDPOINT
```

```sql
FOR SOAP
```

`CREATE`

```sql
ALTER ENDPOINT
```

`sys.soap_endpoints`

```sql
sp_certify_removable sp_create_removable sp_detach_db sp_certify_removable sp_create_removable
```

```sql
sp_dbremove
DROP DATABASE sp_dbremove
```

```sql
ALTER LOGIN WITH SET CREDENTIAL
```

```sql
ALTER LOGIN ADD
```

```sql
DROP
CREDENTIAL
```

```sql
ALTER LOGIN WITH SET CR
```

```sql
sp_addapprole sp_dropapprole
CREATE APPLICATION ROLE
DROP APPLICATION ROLE sp_addapprole sp_dropapprole
```

```sql
sp_addlogin sp_droplogin
CREATE LOGIN
DROP LOGIN sp_addlogin sp_droplogin
```

```sql
sp_adduser sp_dropuser
CREATE USER
DROP USER sp_adduser sp_dropuser
```

```sql
sp_grantdbaccess sp_revokedbaccess
CREATE USER
DROP USER sp_grantdbaccess sp_revokedbaccess
```

```sql
sp_addrole sp_droprole
CREATE ROLE
DROP ROLE sp_addrole sp_droprole
```

```sql
sp_approlepassword sp_password
ALTER APPLICATION ROLE
ALTER LOGIN sp_approlepassword sp_password
```

```sql
sp_changeobjectowner
ALTER SCHEMA
```

```sql
ALTER AUTHORIZATION sp_changeobjectowner
```

`sp_control_dbmasterkey_password`

`sp_control_dbmasterkey_`

```sql
sp_defaultdb sp_defaultlanguage
ALTER LOGIN sp_defaultdb sp_defaultlanguage
```

```sql
sp_denylogin sp_grantlogin
ALTER LOGIN DISABLE
CREATE LOGIN sp_denylogin sp_grantlogin
```

```sql
sp_revokelogin
DROP LOGIN
```

```sql
sp_srvrolepermission sp_dbfixedrolepermission
```

```sql
sp_srvrolepermission sp_dbfixedrolepermissio
```

```sql
GRANT ALL
DENY ALL
REVOKE ALL
GRANT
```

`DENY`

`REVOKE`

`sys.fn_my_permissions`

```sql
EXECUTE AS
```

`DESX`

`DESX`

`SET`

```sql
SET FMTONLY
```

```sql
SET FMTONLY
```

`sp_configure`

`sp_configure`

`Microsoft.SQLServer.Management.Smo.Information`

```sql
Microsoft.SQLServer. Management.Smo.Settings
```

`Microsoft.SQLServer.Management.Smo.DatabaseOptions`

```sql
Microsoft.SqlServer.Management.Smo.DatabaseDdlTrigger.NotForReplication
```

`Microsoft.SqlServer.Management.Smo.Server`

`Microsoft.SqlServer.Management.Smo.Server`

`Microsoft.SqlServer.Management.Smo.Database`

`sp_db_increased_partitions`

`sp_db_increased_partiti`

```sql
sys.numbered_procedures sys.numbered_procedure_parameters
```

```sql
sys.dm_os_cluster_nodes sys.dm_io_cluster_shared_drives
```

```sql
sys.sql_dependencies sys.sql_expression_dependencies sys.sql_dependencies
```

`sp_db_vardecimal_storage_format`

`sp_db_vardecimal_storag`

`sp_estimated_rowsize_reduction_for_vardecimal`

```sql
sp_estimate_data_compression_savings sp_estimated_rowsize_re
```

`NOLOCK`

`READUNCOMMITTED`

`FROM`

`UPDATE`

`DELETE`

`NOLOCK`

`READUNCOMMITTED`

`FROM`

`NOLOCK`

`READUNCOMMITT`

`WITH`

`WITH`

`WITH`

```sql
::
```

```sql
SELECT <column_list> FROM sys.
<function_name>()
```

```sql
SELECT * FROM
::fn_virtualfilestats(2,1)
```

```sql
SELECT * FROM sys.fn_virtualfilestats(2,1)
```

`SELECT`

```sql
DROP INDEX
```

`ON`

```sql
DROP
INDEX
```

```sql
DROP INDEX
```

```sql
;
```

```sql
GROUP BY ALL
```

`UNION`

```sql
GROUP BY ALL
```

`ROWGUIDCOL`

`ROWGUIDCOL`

`DEFAULT`

`DEFAULT`

`DEFAULT`

```sql
ALTER DATABASE
```

```sql
MODIFY FILEGROUP READONLY
MODIFY FILEGROUP READWRITE
MODIFY FILEGROUP READ_ONLY
MODIFY FILEGROUP READ_WRITE
MODIFY FILEGROUP READON
MODIFY FILEGROUP READWR
```

```sql
sp_trace_create sp_trace_setevent sp_trace_setfilter sp_trace_setstatus
```

```sql
sys.traces sys.trace_events sys.trace_event_bindings
```

```sql
sp_trace_create sp_trace_setevent sp_trace_setfilter sp_trace_setstatus
```

```sql
sys.traces sys.trace_events sys.trace_event_binding sys.trace_categories sys.trace_columns sys.trace_subclass_valu
```

```sql
SET ROWCOUNT
```

`INSERT`

`UPDATE`

`DELETE`

`TOP`

```sql
SET ROWCOUNT
```

`OUTPUT`

`sp_setapprole`

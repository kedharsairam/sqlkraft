---
name: "sys.sp_grantlogin"
title: "sp_grantlogin"
category: "general"
description: "Creates a SQL Server login."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_grantlogin [ @loginame = ]
      N
      'loginame'
      [ ; ]
---

## Description

Creates a SQL Server login.

## Syntax

```sql
sp_grantlogin [ @loginame = ]
N
'loginame'
[ ; ]
```

## Remarks

Creates a SQL Server login.

The name of a Windows user or group.

, with no default. The Windows

user or group must be qualified with a Windows domain name in the form

for example,

(success) or

, which supports extra options. For information on creating

logins, see

CREATE LOGIN

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Removes the login entries from SQL Server for a Windows user or group created by using

The name of the Windows user or group.

, with no default.

can be any existing Windows user name or group in the form

(success) or

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Description

Occurs when a Windows login right is added or removed; for

Occurs when a property of a login, except passwords, is

modified; for

Occurs when a SQL Server login password is changed.

Passwords aren't recorded.

Occurs when a login is added or removed from a fixed server

Occurs when a login is added or removed as a database user

(Windows or SQL Server) to a database; for

Occurs when a login is added or removed as a database user

(fixed or user-defined) to a database; for

Occurs when a login is added or removed as a database user to

a database; for

Occurs when a password of an application role is changed.

Occurs when a statement permission (such as CREATE TABLE) is

Occurs when an object permission (such as SELECT) is used,

both successfully or unsuccessfully.

Occurs when a BACKUP or RESTORE command is issued.

Occurs when DBCC commands are issued.

Occurs when audit trace modifications are made.

Occurs when a CREATE, ALTER, and DROP object commands are

Occurs when OLE DB provider calls are made for distributed

queries and remote stored procedures.

Occurs when OLE DB

calls are made for

distributed queries and remote stored procedures.

Requires ALTER ANY LOGIN permission on the server.

sp_denylogin (Transact-SQL)

sp_grantlogin (Transact-SQL)

sp_revokelogin (Transact-SQL)

System stored procedures (Transact-SQL)

General extended stored procedures (Transact-SQL)

xp_loginconfig (Transact-SQL)

xp_logininfo (Transact-SQL)

## Examples

### Example 1

`sp_grantlogin`

### Example 2

```sql
CREATE LOGIN
```

### Example 3

```sql
Corporate\BobJ
```

### Example 4

```sql
CREATE
LOGIN [Corporate\BobJ]
FROM
WINDOWS;
GO
```

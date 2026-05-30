---
name: "In This Section"
title: "In This Section"
category: "predicates"
description: "Azure SQL Managed Instance"
tags: ["tsql", "predicates"]
pubDate: 2026-05-29
---

Article

•

03/03/2023

Applies to:

SQL Server

Azure SQL Managed Instance

This section describes the RESTORE statements for backups. In addition to the main RESTORE

{DATABASE | LOG} statement for restoring and recovering backups, a number of auxiliary

RESTORE statements help you manage your backups and plan your restore sequences. The

auxiliary RESTORE commands include: RESTORE FILELISTONLY, RESTORE HEADERONLY,

RESTORE LABELONLY, RESTORE REWINDONLY, and RESTORE VERIFYONLY.

## Description

RESTORE

(Transact-SQL)

Describes the RESTORE DATABASE and RESTORE LOG Transact-SQL statements used

to restore and recover a database from backups taken using the BACKUP command.

RESTORE DATABASE is used for databases under all recovery models. RESTORE LOG

is used only under the full and bulk-logged recovery models. RESTORE DATABASE

can also be used to revert a database to a database snapshot.

RESTORE

## Arguments

(Transact-SQL)

Documents the arguments described in the "Syntax" sections of the RESTORE

statement and of the associated set of auxiliary statements: RESTORE FILELISTONLY,

RESTORE HEADERONLY, RESTORE LABELONLY, RESTORE REWINDONLY, and

RESTORE VERIFYONLY. Most of the arguments are supported by only a subset of

）

Important

In previous versions of SQL Server, any user could obtain information about backup sets

and backup devices by using the RESTORE FILELISTONLY, RESTORE HEADERONLY,

RESTORE LABELONLY, and RESTORE VERIFYONLY Transact-SQL statements. Because they

reveal information about the content of the backup files, in SQL Server 2008 (10.0.x) and

later versions these statements require CREATE DATABASE permission. This requirement

secures your backup files and protects your backup information more fully than in

previous versions. For information about this permission, see

.



Expand table

#### Statement

## Description

these six statements. The support for each argument is indicated in the description

of the argument.

RESTORE

FILELISTONLY

(Transact-SQL)

Describes the RESTORE FILELISTONLY Transact-SQL statement, which is used to

return a result set containing a list of the database and log files contained in the

backup set.

RESTORE

HEADERONLY

(Transact-SQL)

Describes the RESTORE HEADERONLY Transact-SQL statement, which is used to

return a result set containing all the backup header information for all backup sets

on a particular backup device.

RESTORE

LABELONLY

(Transact-SQL)

Describes the RESTORE LABELONLY Transact-SQL statement, which is used to return

a result set containing information about the backup media identified by the given

backup device.

RESTORE

REWINDONLY

(Transact-SQL)

Describes the RESTORE REWINDONLY Transact-SQL statement, which is used to

rewind and close tape devices that were left open by BACKUP or RESTORE

statements executed with the NOREWIND option.

RESTORE

VERIFYONLY

(Transact-SQL)

Describes the RESTORE VERIFYONLY Transact-SQL statement, which is used to verify

the backup but does not restore it, and checks to see that the backup set is

complete and the entire backup is readable; does not attempt to verify the structure

of the data.

Back Up and Restore of SQL Server Databases

See Also

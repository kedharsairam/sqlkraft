---
title: "Move files"
topic: "collation"
description: "In SQL Server, you can move system and user databases by specifying the new file location in the clause of the ALTER DATABASE statement. Data,"
tags: ["collation","move-files"]
pubDate: "2025-12-01"
---

In SQL Server, you can move

system

and

user

databases by specifying the new file location in

the

clause of the

ALTER DATABASE

statement. Data, log, and full-text catalog files can

be moved in this way. This option might be useful in the following situations:

Failure recovery. For example, the database is in suspect mode, or is shut down, because

of a hardware failure.

Planned relocation.

Relocation for scheduled disk maintenance.

Description

Move user

databases

Describes the procedures for moving user database files and full-text catalog files

to a new location.

Move system

databases

Describes the procedures for moving system database files to a new location.

ALTER DATABASE (Transact-SQL)

CREATE DATABASE

Database detach and attach (SQL Server)

ﾉ

Expand table

`FILENAME`

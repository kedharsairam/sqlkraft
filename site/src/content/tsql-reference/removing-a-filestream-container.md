---
name: "Removing a FILESTREAM Container"
title: "Removing a FILESTREAM Container"
category: "statements"
description: "statement that modifies a table with any index in an offline filegroup"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

, or

statement that modifies a table with any index in an offline filegroup

will fail.

SIZE, MAXSIZE, and FILEGROWTH parameters cannot be set when a UNC path is specified for

the file.

SIZE and FILEGROWTH parameters cannot be set for memory optimized filegroups.

The keyword

will be removed in a future version of Microsoft SQL Server. Avoid using

in new development work, and plan to modify applications that currently use

READONLY. Use

instead.

The keyword

will be removed in a future version of Microsoft SQL Server. Avoid

using

in new development work, and plan to modify applications that currently use

to use

instead.

You can move system or user-defined data and log files by specifying the new location in

FILENAME. This may be useful in the following scenarios:

Failure recovery. For example, the database is in suspect mode or shutdown caused by

hardware failure.

Planned relocation.

Relocation for scheduled disk maintenance.

For more information, see

Move Database Files.

By default, data and log files are initialized by filling the files with zeros when you perform one

of the following operations:

Create a database.

Add files to an existing database.

Increase the size of an existing file.

Restore a database or filegroup.

Data files can be initialized instantaneously. This enables for fast execution of these file

operations. For more information, see

Database File Initialization.

`UPDATE`

`DELETE`

`READONLY`

`READONLY`

`READ_ONLY`

`READWRITE`

`READWRITE`

`READWRITE`

`READ_WRITE`

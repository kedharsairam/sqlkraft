---
title: "Instant file initialization"
topic: "collation"
description: |
  07/16/2025

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  In this article, you learn about instant file initialization (IFI) and how to enable it to speed up

  the growth for
tags:
  - "collation"
  - "instant-file-initialization"
pubDate: 2025-12-01
---

07/16/2025

SQL Server

Azure SQL Database

Azure SQL Managed Instance

In this article, you learn about instant file initialization (IFI) and how to enable it to speed up

the growth for your SQL Server database files.

By default, data and log files are initialized to overwrite any existing data left on the disk from

previously deleted files. Data and log files are first initialized by zeroing the files (filling with

zeros) when you perform the following operations:

Create a database.

Add data or log files, to an existing database.

Increase the size of an existing file (including autogrow operations).

Restore a database or filegroup.

In SQL Server, instant file initialization allows for faster execution of the previously mentioned

file operations, since it reclaims used disk space without filling that space with zeros. Instead,

old disk content is overwritten as new data is written to the files.

In Azure SQL Database and Azure SQL Managed Instance, instant file initialization is available

for transaction log files only.

2022 (16.x) and later versions, and Azure SQL Database and Azure SQL

Managed Instance.

Historically, transaction log files couldn't be initialized instantaneously. However, starting with

2022 (16.x) (all editions) and in Azure SQL Database and Azure SQL Managed

Instance, transaction log autogrowth events up to 64 MB can benefit from instant file

initialization. The default auto growth size increment for new databases is 64 MB. Transaction

log file autogrowth events larger than 64 MB can't benefit from instant file initialization.

Unlike instant file initialization for data files, which is prevented if transparent data encryption

(TDE) is enabled, instant file initialization is allowed for transaction log growth on databases

that have TDE enabled, because of how the transaction log file grows, and the fact that the

transaction log is written into in a serial fashion.

Instant file initialization is in use for General Purpose and Business Critical tiers of Azure

SQL Database, and Azure SQL Managed Instance, only to benefit the growth of

transaction log files.

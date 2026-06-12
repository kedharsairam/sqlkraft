---
title: "Files & filegroups"
topic: "collation"
description: "At a minimum, every SQL Server database has two operating system files: a data file and a log file."
tags: ["collation","files-filegroups"]
pubDate: 2025-12-01
---

At a minimum, every SQL Server database has two operating system files: a data file and a log

file. Data files contain data and objects such as tables, indexes, stored procedures, and views.

Log files contain the information that is required to recover all transactions in the database.

Data files can be grouped together in filegroups for allocation and administration purposes.

databases have three types of files, as shown in the following table.

Description

Contains startup information for the database and points to the other files in the

database. Every database has one primary data file. The recommended file name

extension for primary data files is.

Optional user-defined data files. Data can be spread across multiple disks by putting each

file on a different disk drive. The recommended file name extension for secondary data

files is.

The log holds information used to recover the database. There must be at least one log

file for each database. The recommended file name extension for transaction logs is.

For example, a simple database named

has one primary file that contains all data and

objects and a log file that contains the transaction log information. A more complex database

named

can be created that includes one primary file and five secondary files. The data

and objects within the database spread across all six files, and the four log files contain the

transaction log information.

By default, the data and transaction logs are put on the same drive and path to handle single-

disk systems. This choice might not be optimal for production environments. We recommend

that you put data and log files on separate disks.

files have two file name types:

: The name used to refer to the physical file in all Transact-SQL

statements. The logical file name must comply with the rules for SQL Server identifiers

ﾉ

Expand table

```sql.mdf.ndf.ldf
Sales
Orders logical_file_name
```

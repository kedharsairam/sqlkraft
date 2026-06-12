---
title: "Create, Alter, & Drop"
topic: "filestream"
description: |
  09/29/2025

  Applies to:

  SQL Server

  Describes how to create a new FileTable, or alter or drop an existing FileTable.

  A FileTable is a specialized user table that has a predefined and fixed schema. T
tags:
  - "filestream"
  - "create-alter-drop"
pubDate: 2025-12-01
---

09/29/2025

SQL Server

Describes how to create a new FileTable, or alter or drop an existing FileTable.

A FileTable is a specialized user table that has a predefined and fixed schema. This schema

stores FILESTREAM data, file and directory information, and file attributes. For information

about the FileTable schema, see

FileTable Schema.

You can create a new FileTable by using Transact-SQL or SQL Server Management Studio. Since

a FileTable has a fixed schema, you don't have to specify a list of columns. The simple syntax for

creating a FileTable lets you specify:

A directory name. In the FileTable folder hierarchy, this table-level directory becomes the

child of the database directory specified at the database level, and the parent of the files

or directories stored in the table.

The name of the collation to be used for file names in the

column of the FileTable.

The names to be used for the 3 primary key and unique constraints that are automatically

created.

Create a FileTable by calling the

CREATE TABLE

statement with the

option. Since a

FileTable has a fixed schema, you don't have to specify a list of columns. You can specify the

following settings for the new FileTable:

1. Specifies the directory that serves as the root directory for all the

files and directories stored in the FileTable. This name should be unique among all the

FileTable directory names in the database. Comparison for uniqueness is case-insensitive,

regardless of the current collation settings.

This value has a data type of

and uses a fixed collation of.

The directory name that you provide must comply with the requirements of the file

system for a valid directory name.

```sql
Name
AS FILETABLE
FILETABLE_DIRECTORY
Latin1_General_CI_AS_KS_WS
```

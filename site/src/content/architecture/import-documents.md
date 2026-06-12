---
title: "Import documents"
topic: "json-data"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  This article describes how to import JSON files into SQL Serv
tags:
  - "json-data"
  - "import-documents"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

This article describes how to import JSON files into SQL Server. JSON documents store many

types of data, for example, application logs, sensor data, and so forth. It's important to be able

to read the JSON data stored in files, load the data into SQL Server, and analyze it.

The examples in this article use a JSON file from

a GitHub sample

containing a list of books.

At the instance level, this feature requires membership of the

fixed server role, or

permissions.

For the database level, this feature requires

permissions.

Accessing Azure Blob Storage requires read-write access.

is a table-valued function that can read data from any file on the local drive

or network, if SQL Server has read access to that location. It returns a table with a single

column that contains the contents of the file. There are various options that you can use with

the

function, such as separators. But in the simplest case, you can just load

the entire contents of a file as a text value. (This single large value is known as a single

character large object, or SINGLE_CLOB.)

Here's an example of the

function that reads the contents of a JSON file and

returns it to the user as a single value:

reads the content of the file and returns it in.

You can also load the contents of the file into a local variable or into a table, as shown in the

following example:

```sql
ADMINISTER BULK OPERATIONS
ADMINISTER DATABASE BULK OPERATIONS
OPENROWSET(BULK)
OPENROWSET(BULK)
OPENROWSET(BULK)
OPENJSON(BULK)
BulkColumn
SELECT
BulkColumn
FROM
OPENROWSET(
BULK
'C:\JSON\Books\book.json'
, SINGLE_CLOB) as j;
```

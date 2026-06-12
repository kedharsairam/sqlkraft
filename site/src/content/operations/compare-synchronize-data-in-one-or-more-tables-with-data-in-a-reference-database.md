---
title: "Compare & Synchronize Data in One or More Tables with Data in a Reference Database"
topic: "ssb-diagnose"
description: |
  09/10/2025
          
            You can compare the data in a
          
            source
          
            database and a
          
            target
          
            database and specify which tables
          
            should be compared. The data can be reviewed to guide a decision about which changes to
          
            s
tags: ["ssb-diagnose","compare-synchronize-data-in-one-or-more-tables-with-data-in-a-reference-database"]
pubDate: 2025-12-01
---

You can compare the data in a

source

database and a

target

database and specify which tables

should be compared. The data can be reviewed to guide a decision about which changes to

synchronize. Then you would either update the target to synchronize the databases or export

the update script to the Transact-SQL editor or to a file.

Perhaps you might synchronize databases to update a staging server with a copy of the

production data. You might also synchronize one or more tables to populate them with

reference data from another database. Also, you could compare data before and after you run

tests as an additional form of verification.

You can compare data in two databases, but you can't specify a database project file or

for comparison because it doesn't contain data.

This section contains the following areas of information:

How to: Compare and synchronize the data of two databases with SQL Server Data Tools

How to: View Data Differences

When you compare data in a table or view, the table or view in the source database must share

several attributes with a table or view in the target database. Tables and views that don't meet

the following criteria aren't compared and don't appear on the second page of the

wizard:

Tables must have matching column names that have compatible data types. Names of

tables, views, and owners are case-sensitive.

Tables must have the same primary key, unique index, or unique constraint.

Views must have the same unique, clustered index.

You can compare a table with a view only if they have the same name.

Each object has a key or an index that determines the other objects to which it corresponds.

Each table or view can have more than one primary key, unique index, or unique constraint. So

you might want to specify which key, index, or constraint to use.

```cmd.dacpac
```

---
title: "Use the inserted & deleted Tables"
topic: "change-data-capture"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  DML trigger statements use two special tables: the

  deleted

  and

  inserted

  tables. SQL Serve
tags:
  - "change-data-capture"
  - "use-the-inserted-deleted-tables"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

DML trigger statements use two special tables: the

deleted

and

inserted

tables. SQL Server

automatically creates and manages these tables. You can use these temporary, memory-

resident tables to test the effects of certain data modifications and to set conditions for DML

trigger actions. You cannot directly modify the data in the tables or perform data definition

language (DDL) operations on the tables, such as CREATE INDEX.

In DML triggers, the inserted and deleted tables are primarily used to perform the following:

Extend referential integrity between tables.

Insert or update data in base tables underlying a view.

Test for errors and take action based on the error.

Find the difference between the state of a table before and after a data modification and

take actions based on that difference.

The

deleted

table stores copies of the affected rows in the trigger table before they were

changed by a DELETE or UPDATE statement (the trigger table is the table on which the DML

trigger runs). During the execution of a DELETE or UPDATE statement, the affected rows are

first copied from the trigger table and transferred to the deleted table.

The

inserted

table stores copies of the new or changed rows after an INSERT or UPDATE

statement. During the execution of an INSERT or UPDATE statement, the new or changed rows

in the trigger table are copied to the inserted table. The rows in the inserted table are copies of

the new or updated rows in the trigger table.

An update transaction is similar to a delete operation followed by an insert operation. During

the execution of an UPDATE statement, the following sequence of events occurs:

1. The original row is copied from the trigger table to the deleted table.

2. The trigger table is updated with the new values from the UPDATE statement.

3. The updated row in the trigger table is copied to the inserted table.

This allows you to compare the contents of the row before the update (in the deleted table)

with the new row values after the update (in the inserted table).

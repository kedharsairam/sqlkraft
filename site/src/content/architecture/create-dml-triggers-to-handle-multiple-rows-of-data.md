---
title: "Create DML Triggers to Handle Multiple Rows of Data"
topic: "change-data-capture"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  When you write the code for a DML trigger, consider that the statement that causes the trigge
tags:
  - "change-data-capture"
  - "create-dml-triggers-to-handle-multiple-rows-of-data"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

When you write the code for a DML trigger, consider that the statement that causes the trigger

to fire can be a single statement that affects multiple rows of data, instead of a single row. This

behavior is common for UPDATE and DELETE triggers because these statements frequently

affect multiple rows. The behavior is less common for INSERT triggers because the basic

INSERT statement adds only a single row. However, because an INSERT trigger can be fired by

an INSERT INTO (

table_name

) SELECT statement, the insertion of many rows may cause a single

trigger invocation.

Multirow considerations are especially important when the function of a DML trigger is to

automatically recalculate summary values from one table and store the results in another for

ongoing tallies.

The DML triggers in the following examples are designed to store a running total of a column

in another table of the

sample database.

The first version of the DML trigger works well for a single-row insert when a row of data is

loaded into the

table. An INSERT statement fires the DML trigger, and the

new row is loaded into the

table for the duration of the trigger execution. The

statement reads the

column value for the row and adds that value to the existing

value in the

column in the

table. The

clause makes sure

that the updated row in the

table matches the

of the

row in the

table.

７

Note

We do not recommend using cursors in triggers because they could potentially reduce

performance. To design a trigger that affects multiple rows, use rowset-based logic

instead of cursors.

```sql
AdventureWorks2025
PurchaseOrderDetail
UPDATE
LineTotal
SubTotal
PurchaseOrderHeader
WHERE
PurchaseOrderDetail
PurchaseOrderID
```

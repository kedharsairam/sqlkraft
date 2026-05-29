---
title: "Lesson 1: Converting a Table to a Hierarchical Structure"
topic: "tables"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  Customers who have tables using self joins to express hierarchical relationships can convert
  
tags:
  - "tables"
  - "lesson-1-converting-a-table-to-a-hierarchical-structure"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Customers who have tables using self joins to express hierarchical relationships can convert

their tables to a hierarchical structure using this lesson as a guide. It's relatively easy to migrate

from this representation to one using

. After migration, users will have a compact

and easy to understand hierarchical representation, which can be indexed in several ways for

efficient queries.

This lesson examines an existing table, creates a new table containing a

column,

populates the table with the data from the source table, and then demonstrates three indexing

strategies. This lesson contains the following topics:

To complete this tutorial, you need SQL Server Management Studio, access to a server that's

running SQL Server, and an AdventureWorks database.

Install

SQL Server Management Studio

.

Install

SQL Server 2022 Developer Edition

.

Download

AdventureWorks sample databases

.

For instructions on restoring databases in SSMS, see

Restore a Database Backup Using SSMS

.

The sample

database contains an

table in the

schema. To avoid changing the original table, this step makes a copy of the

table

named

. To simplify the example, you only copy five columns from the original

table. Then, you query the

table to review how the data is

structured in a table without using the

data type.

In a Query Editor window, run the following code to copy the table structure and data from the

table into a new table named

. Since the original table already uses

```sql
AdventureWorks2025
Employee
HumanResources
Employee
EmployeeDemo
HumanResources.EmployeeDemo
Employee
EmployeeDemo
```
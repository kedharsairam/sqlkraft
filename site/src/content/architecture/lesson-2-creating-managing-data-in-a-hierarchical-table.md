---
title: "Lesson 2: Creating & Managing Data in a Hierarchical Table"
topic: "tables"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  In Lesson 1, you modified an existing table to use the
  
  data type, and populated the
  
  column 
tags:
  - "tables"
  - "lesson-2-creating-managing-data-in-a-hierarchical-table"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

In Lesson 1, you modified an existing table to use the

data type, and populated the

column with the representation of the existing data. In this lesson, you start with a

new table, and insert data by using the hierarchical methods. Then, you query and manipulate

the data by using the hierarchical methods.

To complete this tutorial, you need SQL Server Management Studio, access to a server that's

running SQL Server, and an

database.

Install

SQL Server Management Studio (SSMS)

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

The following example creates a table named

, which includes employee data

together with their reporting hierarchy. The example creates the table in the

database, but that is optional. To keep the example simple, this table

includes only five columns:

is a

column that stores the hierarchical relationship.

is a computed column, based on the

column that stores each nodes

level in the hierarchy. It's used for a breadth-first index.

contains the typical employee identification number that is used for

applications such as payroll. In new application development, applications can use the

column and this separate

column isn't needed.

contains the name of the employee.

contains the title of the employee.

```sql
AdventureWorks2025
EmployeeOrg
AdventureWorks2025
OrgNode
OrgLevel
OrgNode
EmployeeID
OrgNode
EmployeeID
EmpName
Title
```
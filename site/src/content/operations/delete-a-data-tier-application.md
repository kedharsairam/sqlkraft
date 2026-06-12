---
title: "Delete a data-tier application"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  You can delete a registered data-tier application by using the Delete Data-tier Application

tags:
  - "ssms"
  - "delete-a-data-tier-application"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

You can delete a registered data-tier application by using the Delete Data-tier Application

wizard in SQL Server Management Studio. You can specify whether the associated database is

retained, detached, or dropped.

Limitations and Restrictions

,

Permissions

The Register Data-tier Application Wizard

When you delete a registered data-tier application (DAC) instance, you choose one of three

options specifying what is to be done with the database associated with the data-tier

application. All three options delete the DAC definition metadata from the database. The

options differ in what they do with the database associated with the data-tier application. The

wizard doesn't delete any of the instance-level objects associated with the DAC or database,

such as logins.

Delete

registration

The associated database remains intact.

Detach

database

The associated database is detached. The instance of the Database Engine can't

reference the database, but the data and log files are intact.

Delete

database

The associated database is dropped. The data and log files are deleted.

There's no automatic mechanism to restore the DAC definition metadata or the database after

you delete a DAC. How you can manually rebuild the DAC instance depends on the delete

option.

ﾉ

Expand table

ﾉ

Expand table

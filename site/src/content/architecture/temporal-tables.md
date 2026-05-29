---
title: "Temporal tables"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  Temporal tables (also known as system-versioned temporal tabl
tags:
  - "tables"
  - "temporal-tables"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

Temporal tables (also known as system-versioned temporal tables), are a database feature that

brings built-in support for providing information about data stored in the table at any point in

time, rather than only the data that is correct at the current moment in time.

Get started with system-versioned temporal tables

, and review

Temporal table usage scenarios

.

A system-versioned temporal table is a type of user table designed to keep a full history of

data changes, allowing easy point-in-time analysis. This type of temporal table is referred to as

a system-versioned temporal table, because the system manages the period of validity for each

row (that is, the Database Engine).

Every temporal table has two explicitly defined columns, each with a

data type.

These columns are referred to as

period

columns. These period columns are used exclusively by

the system to record the period of validity for each row, whenever a row is modified. The main

table that stores current data is referred to as the

current table

, or simply as the

temporal table

.

In addition to these period columns, a temporal table also contains a reference to another

table with a mirrored schema, called the

history table

. The system uses the history table to

automatically store the previous version of the row each time a row in the temporal table gets

updated or deleted. During temporal table creation, you can specify an existing history table

(which must be schema compliant) or let the system create a default history table.

Real data sources are dynamic and more often than not business decisions rely on insights that

analysts can get from data evolution. Use cases for temporal tables include:

Auditing all data changes and performing data forensics when necessary

Reconstructing state of the data as of any time in the past

Calculating trends over time

Maintaining a slowly changing dimension for decision support applications

Recovering from accidental data changes and application errors

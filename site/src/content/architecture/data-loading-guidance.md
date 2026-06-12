---
title: "Data loading guidance"
topic: "filestream"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Azure Synapse Analytics

  Analytics Platform System (PDW)

  SQL database in Microsoft

  Fabric

  Options and recommendations for lo
tags:
  - "filestream"
  - "data-loading-guidance"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

Options and recommendations for loading data into a columnstore index by using the

standard SQL bulk loading and trickle insert methods. Loading data into a columnstore index is

an essential part of any data warehousing process because it moves data into the index in

preparation for analytics.

New to columnstore indexes? See

Columnstore indexes - overview

and

Columnstore Index

Architecture.

Bulk loading

refers to the way large numbers of rows are added to a data store. It's the most

performant way to move data into a columnstore index because it operates on batches of

rows. Bulk loading fills rowgroups to maximum capacity and compresses them directly into the

columnstore. Only rows at the end of a load that don't meet the minimum of 102,400 rows per

rowgroup go to the deltastore.

To perform a bulk load, you can use

bcp Utility

,

Integration Services

, or select rows from a

staging table.

As the diagram suggests, a bulk load:

Doesn't presort the data. Data is inserted into rowgroups in the order it's received.

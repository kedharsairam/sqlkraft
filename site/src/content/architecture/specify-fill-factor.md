---
title: "Specify fill factor"
topic: "filestream"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  This article describes what fill factor is and how to specify a fill factor value for an inde
tags:
  - "filestream"
  - "specify-fill-factor"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This article describes what fill factor is and how to specify a fill factor value for an index using

SQL Server Management Studio or Transact-SQL.

The fill factor option is provided for fine-tuning index data storage and performance. When an

index is created or rebuilt, the fill factor value determines the percentage of space on each leaf-

level page to be filled with data, reserving the remainder on each page as free space for future

growth. For example, specifying a fill factor value of 80 means that 20 percent of each leaf-level

page will be left empty, providing space for data growth. The empty space is reserved on each

page of the index rather than at the end of the index.

The fill factor value is a percentage from 1 to 100, and the server-wide default is 0 which means

that the leaf-level pages are filled to capacity.

Performance Considerations

Security

SQL Server Management Studio

Transact-SQL

７

Note

Fill factor values 0 and 100 are the same in all respects.

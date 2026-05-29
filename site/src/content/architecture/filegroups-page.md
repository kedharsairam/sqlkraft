---
title: "Filegroups page"
topic: "collation"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Use this page to view the filegroups or add a new filegroup to the selected database. Filegroup
  
  types are separated into
  
  row
  
  filegroups, FILESTREAM 
tags:
  - "collation"
  - "filegroups-page"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Use this page to view the filegroups or add a new filegroup to the selected database. Filegroup

types are separated into

row

filegroups, FILESTREAM data, and memory-optimized filegroups.

Row filegroups contain regular data and log files. FILESTREAM data filegroups contain

FILESTREAM data files. These data files store information about how binary large object (BLOB)

data is stored on the file system when you are using FILESTREAM storage. The options are the

same for both types of filegroups.

If FILESTREAM is not enabled, the

section will not be available. You can enable

FILESTREAM storage by using

Server Properties (Advanced Page)

.

For information about how SQL Server uses row filegroups, see

Database Files and Filegroups

.

For more information about FILESTREAM data and filegroups, see

FILESTREAM (SQL Server)

.

Memory-optimized file groups are required for a database to contain one or more memory-

optimized tables.

Enter the name of the filegroup.

Displays the count of files in the filegroup.

Select to set the filegroup to a read-only status.

Select to make this filegroup the default filegroup. You can have one default filegroup for rows

and one default filegroup for FILESTREAM data.

Adds a new blank row to the grid listing filegroups for the database.

Removes the selected filegroup row from the grid.
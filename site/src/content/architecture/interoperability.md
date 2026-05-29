---
title: "Interoperability"
topic: "filestream"
description: |
  Article
  
  •
  
  03/03/2023
  
  Applies to:
  
  SQL Server
  
  Because FILESTREAM data is in the file system, this topic provides some considerations,
  
  guidelines, and limitations for using FILESTREAM with the foll
tags:
  - "filestream"
  - "interoperability"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

Because FILESTREAM data is in the file system, this topic provides some considerations,

guidelines, and limitations for using FILESTREAM with the following features in SQL Server:

SQL Server Integration Services (SSIS)

Distributed Queries and Linked Servers

Encryption

Database Snapshots

Replication

Log Shipping

Database Mirroring

Full-Text Indexing

Failover Clustering

SQL Server Express

Contained Databases

SQL Server Integration Services (SSIS) handles FILESTREAM data in the data flow like any other

BLOB data by using the DT_IMAGE SSIS data type.

You can use the Import Column transformation to load files from the file system into a

FILESTREAM column. You can also use the Export Column transformation to extract files from a

FILESTREAM column to another location in the file system.

You can work with FILESTREAM data through distributed queries and linked servers by treating

it as

data. You cannot use the FILESTREAM

function in distributed

SQL Server Integration Services (SSIS)
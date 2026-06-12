---
title: "Remote Blob Store (RBS)"
topic: "filestream"
description: |
  Article

  •

  11/29/2023

  Applies to:

  SQL Server

  SQL Server Remote BLOB Store (RBS) is an optional add-on component that lets database

  administrators store binary large objects in commodity storage s
tags:
  - "filestream"
  - "remote-blob-store-rbs"
pubDate: 2025-12-01
---

Article

•

11/29/2023

SQL Server

Remote BLOB Store (RBS) is an optional add-on component that lets database

administrators store binary large objects in commodity storage solutions instead of directly on

the main database server.

RBS is included on the SQL Server installation media, but is not installed by the SQL Server

Setup program. Search for RBS.msi on the installation media to locate the setup file.

If you do not have SQL Server installation media, you can download RBS at one of the

following locations:

version

2016 (13.x)

2016 (13.x) SP2 Feature Pack

2017 (14.x)

2017 (14.x) Feature Pack

2019 (15.x)

2019 (15.x) RBS download page

Storing BLOBs in the database can consume large amounts of file space and expensive server

resources. RBS transfers the BLOBs to a dedicated storage solution you choose and stores

references to the BLOBs in the database. This frees server storage for structured data, and frees

server resources for database operations.

Several RBS features support stored BLOBs management:

BLOBS are managed with ACID (atomic, consistent, isolatable, durable) transactions.

BLOBs are organized into collections.

Garbage collection, consistency checking, and other maintenance functions are included.

ﾉ

Expand table

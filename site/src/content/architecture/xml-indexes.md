---
title: "XML Indexes"
topic: "xml-data"
description: |
  Article

  •

  01/30/2024

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  XML indexes can be created on

  data type columns. They index all tags, values and paths

  over the XML i
tags:
  - "xml-data"
  - "xml-indexes"
pubDate: 2025-12-01
---

Article

•

01/30/2024

SQL Server

Azure SQL Database

Azure SQL Managed Instance

XML indexes can be created on

data type columns. They index all tags, values and paths

over the XML instances in the column and benefit query performance. Your application may

benefit from an XML index in the following situations:

Queries on XML columns are common in your workload. XML index maintenance cost

during data modification must be considered.

Your XML values are relatively large and the retrieved parts are relatively small. Building

the index avoids parsing the whole data at run time and benefits index lookups for

efficient query processing.

Starting with SQL Server 2022 (16.x) and later versions, and in Azure SQL Database and Azure

SQL Managed Instance, you can use

XML compression

to compress off-row XML data for both

XML columns and indexes. XML compression reduces data storage capacity requirements.

XML indexes fall into the following categories:

Primary XML index

Secondary XML index

The first index on the

type column must be the primary XML index. Using the primary XML

index, the following types of secondary indexes are supported: PATH, VALUE, and PROPERTY.

Depending on the type of queries, these secondary indexes might help improve query

performance.

XML instances are stored in

type columns as large binary objects (BLOBs). These XML

instances can be large, and the stored binary representation of

data type instances can be

up to 2 GB. Without an index, these binary large objects are shredded at run time to evaluate a

query. This shredding can be time-consuming. For example, consider the following query:

７

Note

You cannot create or modify an XML index unless the database options are set correctly

for working with the

data type. For more information, see.

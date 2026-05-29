---
title: "Selective XML Indexes (SXI)"
topic: "xml-data"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  Selective XML indexes are another type of XML index that is available to you in addition to
  
  ordinary X
tags:
  - "xml-data"
  - "selective-xml-indexes-sxi"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Selective XML indexes are another type of XML index that is available to you in addition to

ordinary XML indexes. The goals of the selective XML index feature are the following:

To improve the performance of queries over XML data stored in SQL Server.

To support faster indexing of large XML data workloads.

To improve scalability by reducing the storage costs of XML indexes.

The main limitation with ordinary XML indexes is that they index the entire XML document. This

leads to several significant drawbacks, such as decreased query performance and increased

index maintenance cost, mostly related to the storage costs of the index.

The selective XML index feature lets you promote only certain paths from the XML documents

to index. At index creation time, these paths are evaluated, and the nodes that they point to

are shredded and stored inside a relational table in SQL Server. This feature uses an efficient

mapping algorithm developed by Microsoft Research in collaboration with the SQL Server

product team. This algorithm maps the XML nodes to a single relational table, and achieves

exceptional performance while requiring only modest storage space.

The selective XML index feature also supports secondary selective XML indexes over nodes that

have been indexed by a selective XML index. These secondary selective indexes are efficient

and further improve the performance of queries.

Selective XML indexes provide the following benefits:

1. Greatly improved query performance over the XML data type for typical query loads.

2. Reduced storage requirements compared to ordinary XML indexes.

3. Reduced index maintenance costs compared to ordinary XML indexes.

4. No need to update applications to benefit from selective XML indexes.
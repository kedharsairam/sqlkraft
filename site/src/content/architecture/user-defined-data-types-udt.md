---
title: "User-Defined Data Types (UDT)"
topic: "xml-data"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  doesn't support common language runtime (CLR) user-defined data types (UDTs).
  
  To use
  
  with C
tags:
  - "xml-data"
  - "user-defined-data-types-udt"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

doesn't support common language runtime (CLR) user-defined data types (UDTs).

To use

with CLR user-defined data types, make sure that the data type has an XML

serialization, and use an explicit cast to XML in the

select clause.

FOR XML support for various SQL Server data types

Last updated on 11/18/2025

```sql
FOR XML
FOR XML
FOR XML
```
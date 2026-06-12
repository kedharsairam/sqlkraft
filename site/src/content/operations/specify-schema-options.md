---
title: "Specify schema options"
topic: "migration"
description: |
  Article

  •

  09/27/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This topic describes how to specify schema options in SQL Server by using SQL Server

  Management Studio or Transact-SQL. Wh
tags:
  - "migration"
  - "specify-schema-options"
pubDate: 2025-12-01
---

Article

•

09/27/2024

SQL Server

Azure SQL Managed Instance

This topic describes how to specify schema options in SQL Server by using SQL Server

Management Studio or Transact-SQL. When you are publishing a table or view, you can control

the object creation options that are replicated for the published object. You can set these

option when the article is created, and you can also change them at a later time. If you do not

explicitly specify these options for an article, a default set of options will be defined.

Limitations and Restrictions

Recommendations

Management Studio

Transact-SQL

If you change schema options after a publication is created, you must generate a new

snapshot.

７

Note

The default schema options when using replication stored procedures may differ from the

default options when articles are added using SQL Server Management Studio.

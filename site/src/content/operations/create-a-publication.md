---
title: "Create a publication"
topic: "migration"
description: |
  Article

  •

  09/27/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article describes how to create a publication in SQL Server by using SQL Server

  Management Studio, Transact-SQL, or R
tags:
  - "migration"
  - "create-a-publication"
pubDate: 2025-12-01
---

Article

•

09/27/2024

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes how to create a publication in SQL Server by using SQL Server

Management Studio, Transact-SQL, or Replication Management Objects (RMO).

Publication and article names can't include any of the following characters:

,

,

,

,

,

,

,

,

,

,

,

, or

. If objects in the database include any of these characters and

you want to replicate them, you must specify an article name that is different from the

object name in the

dialog box, which is available from the

page in the wizard.

When possible, prompt users to enter security credentials at runtime. If you must store

credentials, use the

cryptographic services

provided by the Microsoft Windows .NET

Framework.

Create publications and define articles with the New Publication Wizard. After a publication is

created, view and modify publication properties in the

dialog box. For information about creating a publication from an Oracle database, see

Create a

Publication from an Oracle Database

.

1. Connect to the Publisher in Microsoft SQL Server Management Studio, and then expand

the server node.

2. Expand the

folder, and then right-click the

folder.

3. Select

.

4. Follow the pages in the New Publication Wizard to:

```cmd
%
*
[
]
|
```

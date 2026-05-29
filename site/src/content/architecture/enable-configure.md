---
title: "Enable & Configure"
topic: "filestream"
description: |
  Article
  
  •
  
  09/29/2023
  
  Applies to:
  
  SQL Server
  
  Before you can start to use FILESTREAM, you must enable FILESTREAM on the instance of the
  
  SQL Server Database Engine. This topic describes how to enab
tags:
  - "filestream"
  - "enable-configure"
pubDate: 2025-12-01
---

Article

•

09/29/2023

Applies to:

SQL Server

Before you can start to use FILESTREAM, you must enable FILESTREAM on the instance of the

SQL Server Database Engine. This topic describes how to enable FILESTREAM by using SQL

Server Configuration Manager.

1. On the

menu, navigate to

, and

then select

SQL Server Configuration Manager

.

2. In the list of services, right-click

SQL Server Services

, and then select

.

3. In the

SQL Server Configuration Manager

snap-in, locate the instance of SQL Server on

which you want to enable FILESTREAM.

4. Right-click the instance, and then select

.

5. In the

SQL Server Properties

dialog box, select the

tab.

6. Select the

check box.

7. If you want to read and write FILESTREAM data from Windows, select

. Enter the name of the Windows share in the

box.

8. If remote clients must access the FILESTREAM data that is stored on this share, select

.

9. Select

.

10. In SQL Server Management Studio, select

to display the Query Editor.

11. In Query Editor, enter the following Transact-SQL code:

SQL

７

Note

On newer versions of Windows, follow these instructions to

.
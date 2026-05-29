---
title: "Connect to an existing database in SSDT"
topic: "ssb-diagnose"
description: |
  09/09/2025
  
  This article shows how a user can connect to an existing database in SQL Server Data Tools
  
  (SSDT). SSDT allows you to connect to an existing database, run queries with Transact-SQL (T-
  
  S
tags:
  - "ssb-diagnose"
  - "connect-to-an-existing-database-in-ssdt"
pubDate: 2025-12-01
---

09/09/2025

This article shows how a user can connect to an existing database in SQL Server Data Tools

(SSDT). SSDT allows you to connect to an existing database, run queries with Transact-SQL (T-

SQL), and view the results.

SSDT also offers you a plethora of features that you can use to work with your database. These

are explained in detail in the following sections. Let us understand how we can connect to an

existing database.

To Connect to an existing database, refer to the following steps:

Connect using SQL Server Object Explorer

Know about Authentication Types

Encrypt and Trust Server Certificate

SQL Server Object Explorer (SSOX)

is a tool available in SSDT for Visual Studio. It allows you to

connect to and manage SQL Server databases within Visual Studio. To connect to a database

using SQL Server Object Explorer in SSDT, follow these steps:

1.

: Make sure you have installed SSDT along with the appropriate

version of Visual Studio. Launch Visual Studio.

2.

: Go to the

menu and select

SQL Server Object

. Alternatively, you can use the shortcut

+

(backslash) and then type

+

.

3.

: In the SQL Server Object Explorer window, select the

SQL Server

button (it looks like a sheet with a

icon to its top left) or right-click on the

SQL Server

node and choose

.

4.

: In the

dialog box, enter the connection details

for the SQL Server instance you want to connect to. This includes the server name,

authentication method (for example, Windows Authentication or SQL Server

Authentication), login credentials if applicable, and Encryption Details. Once a SQL Server

instance is connected, it would automatically appear under the Recent Connection Option

in the

tab.
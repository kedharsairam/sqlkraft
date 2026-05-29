---
title: "Install SQL Server Full-Text Search"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  The following steps install

  Full-Text Search

  (

  ) on Linux. You can use Full-Text

  Search to run full-text queries against character-based data in SQL Server table
tags:
  - "linux-operations"
  - "install-sql-server-full-text-search"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

The following steps install

Full-Text Search

(

) on Linux. You can use Full-Text

Search to run full-text queries against character-based data in SQL Server tables.

For a list of features supported by the editions of SQL Server on Linux, see:

Editions and supported features of SQL Server 2025

Editions and supported features of SQL Server 2022

Editions and supported features of SQL Server 2019

Editions and supported features of SQL Server 2017

Install SQL Server Full-Text Search for your platform:

Use the following commands to install

on Red Hat Enterprise Linux.

Bash

If you already have

installed, update to the latest version using the

following commands:

Bash

）

Important

The supported Full-Text languages and document types have changed in SQL Server 2025

(17.x) on Linux. You must rebuild any existing indexes upgraded from SQL Server 2022

(16.x). For more information, see

.

７

Note

Before you install SQL Server Full-Text Search, first

. This step configures

the keys and repositories that you use when installing the

package.

Red Hat Enterprise Linux

```cmd
mssql-server-fts
mssql-server-fts
mssql-server-fts
mssql-server-fts
sudo yum install -y mssql-server-fts
```

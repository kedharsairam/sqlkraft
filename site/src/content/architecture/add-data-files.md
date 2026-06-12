---
title: "Add data files"
topic: "collation"
description: "This topic describes how to add data or log files to a database in SQL Server by using SQL Server Management Studio or Transact-SQL."
tags: ["collation","add-data-files"]
pubDate: 2025-12-01
---

This topic describes how to add data or log files to a database in SQL Server by using SQL

Server Management Studio or Transact-SQL.

Limitations and Restrictions

Security

Management Studio

Transact-SQL

You cannot add or remove a file while a BACKUP statement is running.

A maximum of 32,767 files and 32,767 filegroups can be specified for each database.

Requires ALTER permission on the database.

1. In

, connect to an instance of the SQL Server Database Engine and then

expand that instance.

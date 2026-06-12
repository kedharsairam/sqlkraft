---
title: "Manage properties"
topic: "collation"
description: "This topic describes how to view or change the properties of a database in SQL Server by using SQL Ser"
tags: ["collation","manage-properties"]
pubDate: "2025-12-01"
---

This topic describes how to view or change the properties of a database in SQL Server by using

Management Studio or Transact-SQL. After you change a database property, the

modification takes effect immediately.

Recommendations

Security

Management Studio

Transact-SQL

When AUTO_CLOSE is ON, some columns in the

sys.databases

catalog view and

DATABASEPROPERTYEX function will return NULL because the database is unavailable to

retrieve the data. To resolve this, open the database.

Requires ALTER permission on the database to change the properties of a database. Requires at

least membership in the Public database role to view the properties of a database.

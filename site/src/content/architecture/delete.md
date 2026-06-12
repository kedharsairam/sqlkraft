---
title: "Delete"
topic: "filestream"
description: "This topic describes how to delete (drop) an index in SQL Server by using SQL Server Managem"
tags: ["filestream","delete"]
pubDate: 2025-12-01
---

This topic describes how to delete (drop) an index in SQL Server by using SQL Server

Management Studio or Transact-SQL.

Limitations and Restrictions

Security

Management Studio

Transact-SQL

Indexes created as the result of a PRIMARY KEY or UNIQUE constraint cannot be deleted by

using this method. Instead, the constraint must be deleted. To remove the constraint and

corresponding index, use

ALTER TABLE

with the DROP CONSTRAINT clause in Transact-SQL. For

more information, see

Delete Primary Keys.

Requires ALTER permission on the table or view. This permission is granted by default to the

fixed server role and the

and

fixed database roles.

---
name: "Cursors"
title: "Cursors"
category: "data-types"
description: ""
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

cursor

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Microsoft SQL Server statements produce a complete result set, but there are times when the results are best processed one row at a time. Opening a cursor on a result set allows processing the result set one row at a time. You can assign a cursor to a variable or parameter with a data type.

Cursor operations are supported on these statements: CLOSE

CREATE PROCEDURE

DEALLOCATE

DECLARE CURSOR

DECLARE @local_variable

DELETE

FETCH

OPEN

UPDATE

SET

These system functions and system stored procedures also support cursors:

@@CURSOR_ROWS

CURSOR_STATUS

@@FETCH_STATUS sp_cursor_list sp_describe_cursor sp_describe_cursor_columns sp_describe_cursor_tables

Cursors

See Also

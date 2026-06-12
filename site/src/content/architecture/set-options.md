---
title: "Set Options"
topic: "filestream"
description: "This topic describes how to modify the properties of an index in SQL Server by using SQL Ser"
tags: ["filestream","set-options"]
pubDate: "2025-12-01"
---

This topic describes how to modify the properties of an index in SQL Server by using SQL

Server Management Studio or Transact-SQL.

Limitations and Restrictions

Security

Management Studio

Transact-SQL

The following options are immediately applied to the index by using the SET clause in the

ALTER INDEX statement: ALLOW_PAGE_LOCKS, ALLOW_ROW_LOCKS,

OPTIMIZE_FOR_SEQUENTIAL_KEY, IGNORE_DUP_KEY, and STATISTICS_NORECOMPUTE.

The following options can be set when you rebuild an index by using either ALTER INDEX

REBUILD or CREATE INDEX WITH DROP_EXISTING: PAD_INDEX, FILLFACTOR,

SORT_IN_TEMPDB, IGNORE_DUP_KEY, STATISTICS_NORECOMPUTE, ONLINE,

ALLOW_ROW_LOCKS, ALLOW_PAGE_LOCKS, MAXDOP, and DROP_EXISTING (CREATE

INDEX only).

Requires ALTER permission on the table or view.

---
name: "sys.dm_db_missing_index_groups"
title: "sys.dm_db_missing_index_groups"
category: "index"
description: "This DMV returns information about indexes that are missing in a specific index group. In Azure SQL Database, dynamic management views cannot expose information that would impact database containment or expose information about other databases the user has access to."
tags: ["index","dmv"]
pubDate: "2026-05-29"
syntax: "sys.dm_db_missing_index_groups"
---

## Description

This DMV returns information about indexes that are missing in a specific index group. In Azure SQL Database, dynamic management views cannot expose information that would impact database containment or expose information about other databases the user has access to. To avoid exposing this information, every row that contains data that doesn't belong to the connected tenant is filtered out. Identifies a missing index group. Identifies a missing index that belongs to the group specified by An index group contains only one index. Information returned by is updated when a query is optimized by the query optimizer, and is not persisted. Missing index information is kept only until the database engine is restarted.

## Syntax

`sys.dm_db_missing_index_groups`

## Remarks

This DMV returns information about indexes that are missing in a specific index group.

In Azure SQL Database, dynamic management views cannot expose information that would

impact database containment or expose information about other databases the user has access

to. To avoid exposing this information, every row that contains data that doesn't belong to the

connected tenant is filtered out.

Identifies a missing index group.

Identifies a missing index that belongs to the group specified by

An index group contains only one index.

Information returned by

is updated when a query is

optimized by the query optimizer, and is not persisted. Missing index information is kept only

until the database engine is restarted. It may be useful for database administrators to

periodically make backup copies of the missing index information if they want to keep it after

server recycling. Use the

sys.dm_os_sys_info

to find the last

database engine startup time.

Neither column of the output result set is a key, but together they form an index key.

The result set for this DMV is limited to 600 rows. Each row contains one missing index. If

you have more than 600 missing indexes, you should address the existing missing indexes

so you can then view the newer ones.

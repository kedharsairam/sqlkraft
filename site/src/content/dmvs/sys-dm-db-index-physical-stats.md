---
name: "sys.dm_db_index_physical_stats"
title: "sys.dm_db_index_physical_stats"
category: "index"
description: "SQL database in Microsoft Fabric Returns size and fragmentation information for the data and indexes of the specified table or view in the SQL Server Database Engine. For an index, one row is returned for each level of the B-tree in each partition. For a heap, one row is returned for the each partition. For large object (LOB) data, one row is returned for the of each partition."
tags: ["index", "dmv"]
pubDate: 2026-05-29
syntax: "IN_ROW_DATA"
---

## Description

SQL database in Microsoft Fabric Returns size and fragmentation information for the data and indexes of the specified table or view in the SQL Server Database Engine. For an index, one row is returned for each level of the B-tree in each partition. For a heap, one row is returned for the each partition. For large object (LOB) data, one row is returned for the of each partition. If row-overflow data exists in the table, one row is returned for the

## Syntax

`IN_ROW_DATA`

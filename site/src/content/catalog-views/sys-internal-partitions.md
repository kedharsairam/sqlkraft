---
name: "sys.internal_partitions"
title: "sys.internal_partitions"
category: "partitions"
description: "SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns one row for each rowset that tracks internal data for columnstore indexes on disk- based tables. These rowsets are internal to columnstore indexes and track deleted rows, rowgroup mappings, and delta store rowgroups. They track data for each table partition. Every table has at least one partition. The Database Engin"
tags: ["partitions", "catalog-view"]
pubDate: 2026-05-29
syntax: "COLUMN_STORE_DELETE_BITMAP"
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns one row for each rowset that tracks internal data for columnstore indexes on disk- based tables. These rowsets are internal to columnstore indexes and track deleted rows, rowgroup mappings, and delta store rowgroups. They track data for each table partition. Every table has at least one partition. The Database Engine re-creates the rowsets each time it

## Syntax

`COLUMN_STORE_DELETE_BITMAP`

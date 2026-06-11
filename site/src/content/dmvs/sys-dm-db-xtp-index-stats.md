---
name: "sys.dm_db_xtp_index_stats"
title: "sys.dm_db_xtp_index_stats"
category: "in-memory"
description: "Contains statistics collected since the last database restart. In-Memory OLTP (In-Memory Optimization) Using Indexes on Memory-Optimized Tables ID of the object to which this index Internal ID corresponding to the current Note: Applies to SQL Server 2016 (13.x)."
tags: ["in-memory", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_db_index_usage_stats"
---

## Description

Contains statistics collected since the last database restart. In-Memory OLTP (In-Memory Optimization) Using Indexes on Memory-Optimized Tables ID of the object to which this index Internal ID corresponding to the current Note: Applies to SQL Server 2016 (13.x). ID of the index. The index_id is unique Number of In-Memory OLTP index scans performed. Every select, insert, update, or delete requires an index scan.

## Syntax

`sys.dm_db_index_usage_stats`

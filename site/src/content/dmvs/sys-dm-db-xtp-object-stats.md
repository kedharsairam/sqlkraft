---
name: "sys.dm_db_xtp_object_stats"
title: "sys.dm_db_xtp_object_stats"
category: "in-memory"
description: "Reports the number rows affected by operations on each of the In-Memory OLTP objects since the last database restart. Statistics are updated when the operation executes, regardless of whether the transaction commits or was rolled back. system dynamic management view can help you identify which memory-optimized tables are changing the most."
tags: ["in-memory","dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_db_xtp_object_stats"
---

## Description

Reports the number rows affected by operations on each of the In-Memory OLTP objects since the last database restart. Statistics are updated when the operation executes, regardless of whether the transaction commits or was rolled back. system dynamic management view can help you identify which memory-optimized tables are changing the most. You may decide to remove unused or rarely used indexes on the table, as each index affects performance. If there are hash indexes,

## Syntax

`sys.dm_db_xtp_object_stats`

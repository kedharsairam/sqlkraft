---
name: "sys.dm_db_xtp_hash_index_stats"
title: "sys.dm_db_xtp_hash_index_stats"
category: "in-memory"
description: "These statistics are useful for understanding and tuning the bucket counts for . It can also be used to detect cases where the index key has many A large average chain length indicates that many rows are hashed to the same bucket. This If the number of empty buckets is low or the average and maximum chain lengths are similar, it is likely that the total bucket count is too low. This causes many di"
tags: ["in-memory", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_db_xtp_hash_index_stats"
---

## Description

These statistics are useful for understanding and tuning the bucket counts for . It can also be used to detect cases where the index key has many A large average chain length indicates that many rows are hashed to the same bucket. This If the number of empty buckets is low or the average and maximum chain lengths are similar, it is likely that the total bucket count is too low. This causes many different index

## Syntax

```sql
sys.dm_db_xtp_hash_index_stats
```

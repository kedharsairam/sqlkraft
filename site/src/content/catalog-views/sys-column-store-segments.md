---
name: "sys.column_store_segments"
title: "sys.column_store_segments"
category: "compatibility"
description: "Returns one row for each column segment in a columnstore index. There is one column segment per column per rowgroup. For example, a columnstore index with 10 rowgroups and 34 columns has 340 rows in this view. Indicates the partition ID."
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
syntax: "<hobt_id, partition_id, column_id, segment_id>"
---

## Description

Returns one row for each column segment in a columnstore index. There is one column segment per column per rowgroup. For example, a columnstore index with 10 rowgroups and 34 columns has 340 rows in this view. Indicates the partition ID.

## Syntax

```sql
<hobt_id, partition_id, column_id, segment_id>
```

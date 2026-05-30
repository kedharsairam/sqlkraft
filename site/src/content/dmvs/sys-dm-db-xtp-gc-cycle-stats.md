---
name: "sys.dm_db_xtp_gc_cycle_stats"
title: "sys.dm_db_xtp_gc_cycle_stats"
category: "in-memory"
description: "Outputs the current state of committed transactions that deleted one or more rows. The idle garbage collection thread wakes every minute or when the number of committed DML transactions exceeds an internal threshold since the last garbage collection cycle. As part of the garbage collection cycle, committed transactions move into one or more queues associated with generations. The transactions that"
tags: ["in-memory", "dmv"]
pubDate: 2026-05-29
---

## Description

Outputs the current state of committed transactions that deleted one or more rows. The idle garbage collection thread wakes every minute or when the number of committed DML transactions exceeds an internal threshold since the last garbage collection cycle. As part of the garbage collection cycle, committed transactions move into one or more queues associated with generations. The transactions that generated stale versions are grouped in a unit of 16

## Code Blocks

`cycle_id`

`ticks_at_cycle_start`

`ticks_at_cycle_end`

`base_generation`

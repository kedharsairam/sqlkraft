---
name: "sys.dm_xtp_gc_queue_stats"
title: "sys.dm_xtp_gc_queue_stats"
category: "execution"
description: "SQL database in Microsoft Fabric Outputs information about each garbage collection worker queue on the server, and various statistics about each. There is one queue per logical CPU. The main garbage collection thread (the Idle thread) tracks updated, deleted, and inserted rows for all transactions completed since the last invocation of the main garbage collection thread. When the garbage collectio"
tags: ["execution", "dmv"]
pubDate: 2026-05-29
---

## Description

SQL database in Microsoft Fabric Outputs information about each garbage collection worker queue on the server, and various statistics about each. There is one queue per logical CPU. The main garbage collection thread (the Idle thread) tracks updated, deleted, and inserted rows for all transactions completed since the last invocation of the main garbage collection thread. When the garbage collection thread wakes, it determines if the timestamp of the oldest active

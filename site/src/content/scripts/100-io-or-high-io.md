---
name: "100_ IO or High IO"
title: "100_ IO or High IO"
description: "first add these counters in performance monitor"
category: "troubleshooting"
tags: ["troubleshooting"]
pubDate: "2025-03-15"
---

```sql
--first add these counters in performance monitor
--Avg Disk Reads/sec (<=8 is good, >20 is bad)
--Avg Disk Writes/sec (<=1 is good, >4 is bad)
--Avg Disk Transfer
--Avg Disk Queue Length

--use the following command to analyse IO related metrics select * from sys.dm_io_virtual_file_stats
```

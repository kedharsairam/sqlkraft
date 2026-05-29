---
name: "To View List of Drives Participating in Cluster"
title: "To View List of Drives Participating in Cluster"
description: "SQL Server diagnostic script for high-availability operations."
category: high-availability
tags: ["high-availability"]
pubDate: 2025-03-15
---

```sql
select * from sys.dm_io_cluster_shared_drives
```

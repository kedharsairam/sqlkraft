---
name: "To Perform Force Failover in Mirroring"
title: "To Perform Force Failover in Mirroring"
description: "SQL Server diagnostic script for high-availability operations."
category: high-availability
tags: ["failover", "high-availability", "mirroring"]
pubDate: 2025-03-15
---

```sql
alter database databasename
set partner force_service_allow_data_loss
```

---
name: "To Break Mirroring"
title: "To Break Mirroring"
description: "if failover failed, use this command to break the mirroring"
category: high-availability
tags: ["high-availability", "mirroring"]
pubDate: 2025-03-15
---

```sql
--if failover failed, use this command to break the mirroring
alter database databasename set partner off
```

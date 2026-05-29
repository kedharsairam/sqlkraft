---
name: "To Get Role and Status of Machines in Mirroring"
title: "To Get Role and Status of Machines in Mirroring"
description: "SQL Server diagnostic script for high-availability operations."
category: high-availability
tags: ["high-availability", "mirroring"]
pubDate: 2025-03-15
---

```sql
select state_desc, role from sys.database_mirroring_endpoints
```

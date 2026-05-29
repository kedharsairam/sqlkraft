---
name: 'To Get List of Endpoints while Performing Mirro'
title: 'To Get List of Endpoints while Performing Mirro'
description: 'SQL Server diagnostic script for high-availability operations.'
category: high-availability
tags: ["high-availability"]
pubDate: 2025-03-15
---

```sql
select type_desc, port from sys.tcp_endpoints
```

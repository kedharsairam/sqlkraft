---
name: 'To View the List of Linked Servers'
title: 'To View the List of Linked Servers'
description: 'SQL Server diagnostic script for installation operations.'
category: installation
tags: ["installation"]
pubDate: 2025-03-15
---

```sql
SELECT * FROM sys.servers WHERE is_linked = 1
```

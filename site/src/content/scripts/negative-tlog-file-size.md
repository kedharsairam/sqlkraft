---
name: 'Negative TLog File Size'
title: 'Negative TLog File Size'
description: 'SQL Server diagnostic script for troubleshooting operations.'
category: troubleshooting
tags: ["troubleshooting"]
pubDate: 2025-03-15
---

```sql
dbcc updateusage (0) with count_rows
```

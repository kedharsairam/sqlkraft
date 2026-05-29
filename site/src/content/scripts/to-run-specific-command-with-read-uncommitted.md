---
name: "To Run Specific Command with Read Uncommitted"
title: "To Run Specific Command with Read Uncommitted"
description: "SQL Server diagnostic script for performance operations."
category: performance
tags: ["performance"]
pubDate: 2025-03-15
---

```sql
select * from tablename with (nolock)
--this type is called as HINT (nolock HINT)
```

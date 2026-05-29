---
name: "To Add Delay to Execute Command or Query"
title: "To Add Delay to Execute Command or Query"
description: "we need to add (waitfor delay 'hh:mm:ss')"
category: general
tags: ["general"]
pubDate: 2025-03-15
---

```sql
--we need to add (waitfor delay 'hh:mm:ss')
--ex:
			select * from table1
			waitfor delay '00:00:50'
--it will show output after 50 seconds
```

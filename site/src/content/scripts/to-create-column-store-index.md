---
name: "To Create Column Store Index"
title: "To Create Column Store Index"
description: "this one will only work from sql server 2014"
category: "index-maintenance"
tags: ["index-maintenance","indexing"]
pubDate: 2025-03-15
---

```sql
--this one will only work from sql server 2014
CREATE CLUSTERED COLUMNSTORE INDEX [indexname] ON [tablename]
([column1],[column2],[column3],[column4])
GO

--this one will only work from sql server 2012
CREATE NONCLUSTERED COLUMNSTORE INDEX [indexname] ON [tablename]
([column1],[column2],[column3],[column4])
GO
```

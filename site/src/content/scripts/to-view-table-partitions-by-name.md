---
name: "To View Table Partitions by Name"
title: "To View Table Partitions by Name"
description: "SQL Server diagnostic script for database operations."
category: database
tags: ["database", "table"]
pubDate: 2025-03-15
---

```sql
select Object_name(object_id) as TableName,*
from sys.partitions where object_id=object_id('tablename')
```

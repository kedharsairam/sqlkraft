---
name: "To View Allocation Units for Table by Name"
title: "To View Allocation Units for Table by Name"
description: "diagnostic script for database operations."
category: database
tags: ["database", "table"]
pubDate: 2025-03-15
---

```sql
select * from sys.system_internals_allocation_units where container_id=(select hobt_id from sys.partitions where object_id=object_id('tablename'))
```

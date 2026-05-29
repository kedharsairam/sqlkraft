---
name: 'To Check Database ID or Database Name'
title: 'To Check Database ID or Database Name'
description: 'for id:'
category: database
tags: ["database", "health-check"]
pubDate: 2025-03-15
---

```sql
--for id:
select db_id('databasename')

--for name:
select db_name(databaseid)
```

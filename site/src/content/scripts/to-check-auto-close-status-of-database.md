---
name: "To Check Auto Close status of Database"
title: "To Check Auto Close status of Database"
description: "for single database"
category: database
tags: ["database", "health-check"]
pubDate: 2025-03-15
---

```sql
--for single database select databaseproperty ('databasename', 'isautoclose')

--for all the databases in an instance select name, is_auto_close_on from sys.databases where is_auto_close_on = 1
```

---
name: "To Rename Logical Filename of a Database"
title: "To Rename Logical Filename of a Database"
description: "diagnostic script for database operations."
category: "database"
tags: ["database"]
pubDate: 2025-03-15
---

```sql
use databasename alter database databasename modify file (name = databasename, newname = newdatabasename) alter database databasename modify file (name = databaselogname, newname = newdatabaselogname)
```

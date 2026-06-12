---
name: "To Put Database in Offline State or Online Stat"
title: "To Put Database in Offline State or Online Stat"
description: "to set the database online"
category: "database"
tags: ["database"]
pubDate: "2025-03-15"
---

```sql
--to set the database online alter database databasename set online

--to set the database offline alter database databasename set offline with rollback immediate
--this last line will stop any uncommitted transactions.
```

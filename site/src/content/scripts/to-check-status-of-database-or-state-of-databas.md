---
name: "To Check Status of Database or State of Databas"
title: "To Check Status of Database or State of Databas"
description: "for a specific database"
category: "database"
tags: ["database","health-check"]
pubDate: 2025-03-15
---

```sql
--for a specific database select databasepropertyex ('databasename', 'status')

--for all databases select name, state_desc from sys.databases
--or sp_helpdb
```

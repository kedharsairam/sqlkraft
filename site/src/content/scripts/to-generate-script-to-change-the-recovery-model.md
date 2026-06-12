---
name: "To Generate Script to Change the Recovery Model"
title: "To Generate Script to Change the Recovery Model"
description: "modify the command accordingly"
category: "database"
tags: ["database"]
pubDate: 2025-03-15
---

```sql
--modify the command accordingly select 'ALTER DATABASE' + ' '+ name + ' '+'SET RECOVERY SIMPLE WITH NO_WAIT' from sys.databases where recovery_model_desc = 'FULL' and name not in ('model')
```

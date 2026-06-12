---
name: "sys.sp_purge_data"
title: "core.sp_purge_data"
category: "general"
description: "Removes data from the management data warehouse based on a retention policy. This procedure is executed daily by the SQL Server Agent job against the management data warehouse associated with the specified instance. You can use this stored procedure to perform an on-demand removal of data from the management data warehouse. The number of days to retain data in the m"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "'<computername>\\<instancename>'"
---

## Description

Removes data from the management data warehouse based on a retention policy. This procedure is executed daily by the SQL Server Agent job against the management data warehouse associated with the specified instance. You can use this stored procedure to perform an on-demand removal of data from the management data warehouse. The number of days to retain data in the management data warehouse tables.

## Syntax

```sql
<computername>\<instancename>
```

---
name: "Important List of Tables Participating in Repli"
title: "Important List of Tables Participating in Repli"
description: "Transactional Replication:"
category: replication
tags: ["replication", "table"]
pubDate: 2025-03-15
---

```sql
--Transactional Replication:
	--Publishing Database:
	select * from syspublications
	select * from sysarticles
	select * from syssubscriptions
	--Distribution Database:
	select * from MSRepl_Transactions
	select * from MSRepl_Commands
	select * from MSRepl_Errors

--Merge Replication:
MSmerge_contents
MSmerge_tombstone
MSmerge_genhistory
```

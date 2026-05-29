---
name: "To View List of Encrypted Databases"
title: "To View List of Encrypted Databases"
description: "SQL Server diagnostic script for security-audit operations."
category: security-audit
tags: ["database", "encryption", "security-audit"]
pubDate: 2025-03-15
---

```sql
select * from sys.dm_database_encryption_keys
where encryption_state = 3;
go

--note: by default if we encrypt any database, tempdb will also get encrypted.
```

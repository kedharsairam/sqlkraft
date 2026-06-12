---
name: "To View Size of Log in Database"
title: "To View Size of Log in Database"
description: "diagnostic script for database operations."
category: "database"
tags: ["database"]
pubDate: "2025-03-15"
---

```sql
SELECT [database_transaction_log_bytes_used]
FROM sys.dm_tran_database_transactions
WHERE [database_id] = DB_ID (N'databasename');
GO
```

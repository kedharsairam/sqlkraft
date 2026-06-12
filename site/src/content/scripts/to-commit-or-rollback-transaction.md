---
name: "To Commit or Rollback Transaction"
title: "To Commit or Rollback Transaction"
description: "COMMIT saves all changes made in a transaction permanently, while ROLLBACK undoes those changes. For example, COMMIT finalizes a new record, while ROLLBACK discards it."
category: "general"
tags: ["general"]
pubDate: 2025-03-15
---

```sql
--COMMIT saves all changes made in a transaction permanently, while ROLLBACK undoes those changes. For example, COMMIT finalizes a new record, while ROLLBACK discards it.
BEGIN TRAN;
INSERT INTO tablename VALUES ('value1');
COMMIT / ROLLBACK;
```

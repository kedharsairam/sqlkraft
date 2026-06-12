---
name: "To Identify When was Password got Changed"
title: "To Identify When was Password got Changed"
description: "diagnostic script for security-audit operations."
category: "security-audit"
tags: ["security-audit"]
pubDate: "2025-03-15"
---

```sql
SELECT name AS LoginName, modify_date AS LastPasswordChangeDate
FROM sys.sql_logins
WHERE name = 'YourLoginName'
```

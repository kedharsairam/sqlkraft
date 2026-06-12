---
name: "To Create Login"
title: "To Create Login"
description: "windows authentication:"
category: "security-audit"
tags: ["login","security-audit"]
pubDate: 2025-03-15
---

```sql
--windows authentication:
--single user mapping:
CREATE LOGIN [instance_name] FROM WINDOWS
GO
--group mapping:
CREATE LOGIN [instance_name] FROM WINDOWS
--builtin administrator mapping:
CREATE LOGIN [instance_name] FROM WINDOWS

--sql authentication:
CREATE LOGIN [loginname] WITH PASSWORD=N'[password]'
GO
```

---
name: 'To Find SID of Logins and Users'
title: 'To Find SID of Logins and Users'
description: 'for logins'
category: security-audit
tags: ["login", "security-audit", "user"]
pubDate: 2025-03-15
---

```sql
--for logins
select name, sid from sys.server_principals

--for users
select name, sid from sys.database_principals
```

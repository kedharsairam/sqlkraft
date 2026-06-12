---
name: "To Deny Permission or Revoke Permission to a Sp"
title: "To Deny Permission or Revoke Permission to a Sp"
description: "to block a permission:"
category: "security-audit"
tags: ["permissions","security-audit"]
pubDate: "2025-03-15"
---

```sql
--to block a permission:
Deny permissionname to loginname

--to take back the permission to a specific login:
revoke permissionname to loginname

--to take back the permission from all the logins which have got their permission from with grant from one to other like l1 > l2> l3:
revoke permissionname to loginname cascade
```

---
name: "To View Instance Level Settings"
title: "To View Instance Level Settings"
description: "for basic settings:"
category: security-audit
tags: ["security-audit"]
pubDate: 2025-03-15
---

```sql
--for basic settings:
sp_configure

--for advanced settings:
sp_configure 'show advanced options', 1
--then run the following to refresh the settings reconfigure
--and now if you run 'sp_configure', we can see all the settings
```

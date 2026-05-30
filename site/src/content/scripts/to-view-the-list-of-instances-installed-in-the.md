---
name: "To View the List of Instances Installed in the"
title: "To View the List of Instances Installed in the"
description: "SQL Server diagnostic script for installation operations."
category: installation
tags: ["installation"]
pubDate: 2025-03-15
---

```sql
DECLARE @intstances TABLE
( Value nvarchar(100),
InstanceNames nvarchar(100),
Data nvarchar(100))
Insert into @intstances
EXECUTE xp_regread
@rootkey = 'HKEY_LOCAL_MACHINE',
@key = 'SOFTWARE\Microsoft\Microsoft SQL Server',
@value_name = 'InstalledInstances'
Select InstanceNames from @intstances
```

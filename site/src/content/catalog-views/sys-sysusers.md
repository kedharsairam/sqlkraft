---
name: "sys.sysusers"
title: "sys.sysusers"
category: "security"
description: "SQL analytics endpoint in Microsoft Fabric Contains one row for each Microsoft Windows user, Windows group, Microsoft SQL Server user, or SQL Server role in the database. User ID, unique in this database. Overflows or returns NULL if the number of users and roles exceeds Identified for informational purposes only. Not supported. Future compatibility is not guarantee"
tags: ["security","catalog-view"]
pubDate: 2026-05-29
syntax: "SELECT * FROM sys.sysusers"
---

## Description

Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Contains one row for each Microsoft Windows user, Windows group, Microsoft SQL Server user, or SQL Server role in the database. User ID, unique in this database. Overflows or returns NULL if the number of users and roles exceeds Identified for informational purposes only. Not supported. Future compatibility is not guaranteed.

## Syntax

```sql
SELECT * FROM sys.sysusers
```

## Permissions

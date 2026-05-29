---
name: "sys.dm_db_missing_index_details"
title: "sys.dm_db_missing_index_details"
category: "index"
description: "SQL database in Microsoft Fabric Returns detailed information about missing indexes. In Azure SQL Database, dynamic management views cannot expose information that would impact database containment or expose information about other databases the user has access to. To avoid exposing this information, every row that contains data that doesn't belong to the connected tenant is filtered out. Identifi"
tags: ["index", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_db_missing_index_details"
---

## Description

SQL database in Microsoft Fabric Returns detailed information about missing indexes. In Azure SQL Database, dynamic management views cannot expose information that would impact database containment or expose information about other databases the user has access to. To avoid exposing this information, every row that contains data that doesn't belong to the connected tenant is filtered out. Identifies a particular missing index. The identifier is unique

## Syntax

```sql
sys.dm_db_missing_index_details
```

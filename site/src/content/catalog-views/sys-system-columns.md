---
name: "sys.system_columns"
title: "sys.system_columns"
category: "objects"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each column of system objects that have columns. ID of the object to which this column belongs. Name of the column. Is unique within the object. ID of the column. Is unique within the object. Column IDs might not be sequential. ID of the system-type of the column ID of the type of the column as defined by the user."
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: "sp_tableoption 'text in row'"
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each column of system objects that have columns. ID of the object to which this column belongs. Name of the column. Is unique within the object. ID of the column. Is unique within the object. Column IDs might not be sequential. ID of the system-type of the column ID of the type of the column as defined by the user. To return the name of the type, join to the

## Syntax

```sql
sp_tableoption 'text in row'
```

---
name: "sys.system_parameters"
title: "sys.system_parameters"
category: "compatibility"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains one row for each system object that has parameters."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains one row for each system object that has parameters. ID of the object to which this parameter belongs. Name of the parameter. Is unique within the If the object is a scalar function, the parameter name is an empty string in the row representing ID of the parameter. Is unique within the object. If the object is a scalar function,

## Code Blocks

`object_id`

`name`

`parameter_id`

```sql
parameter_id = 0
```

`system_type_id`

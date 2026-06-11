---
name: "sys.all_parameters"
title: "sys.all_parameters"
category: "compatibility"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Shows the union of all parameters that belong to user-defined or system objects."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Shows the union of all parameters that belong to user-defined or system objects. ID of the object to which this parameter belongs. Name of parameter. Is unique within the object. If the object is a scalar function, the parameter name is an empty string in the row representing ID of parameter. Is unique within the object. If the ID of the system type of the parameter.

## Code Blocks

`object_id`

`name`

`parameter_id`

```sql
parameter_id = 0
```

`system_type_id`

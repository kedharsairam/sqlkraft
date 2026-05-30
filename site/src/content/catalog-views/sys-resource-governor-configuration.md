---
name: "sys.resource_governor_configuration"
title: "sys.resource_governor_configuration"
category: "configuration"
description: "Returns the stored resource governor configuration. The object ID of the classifier function in This function is used to classify new sessions and uses rules to route the workload to the appropriate workload group. For more information, see Indicates the current state of resource governor: : SQL Server 2014 (12.x) and later. The maximum number of outstanding I/O requests per The catalog view displ"
tags: ["configuration", "catalog-view"]
pubDate: 2026-05-29
syntax: "classifier_function_id"
---

## Description

Returns the stored resource governor configuration. The object ID of the classifier function in This function is used to classify new sessions and uses rules to route the workload to the appropriate workload group. For more information, see Indicates the current state of resource governor: : SQL Server 2014 (12.x) and later. The maximum number of outstanding I/O requests per The catalog view displays resource governor configuration as stored in metadata. To see the

## Syntax

`classifier_function_id`

## Examples

### Example 1

`classifier_function_id`

### Example 2

`is_enabled`

### Example 3

`max_outstanding_io_per_volume`

### Example 4

```sql
VIEW ANY DEFINITION
```

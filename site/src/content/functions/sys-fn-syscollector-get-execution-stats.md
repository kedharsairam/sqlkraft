---
name: "sys.fn_syscollector_get_execution_stats"
title: "fn_syscollector_get_execution_stats"
category: "system"
description: "Returns detailed statistics about the collection set or package, including the number of error rows that are logged by a package data flow task. A data flow task is an Integration Services component that processes data. This data is in relational format, so it has an input and an output dataset consisting of rows. The statistics are calculated from entries in the syscollector_execution_stats view."
tags: ["system","function"]
pubDate: "2026-05-29"
syntax: "fn_syscollector_get_execution_stats ( log_id )"
---

## Description

Returns detailed statistics about the collection set or package, including the number of error rows that are logged by a package data flow task. A data flow task is an Integration Services component that processes data. This data is in relational format, so it has an input and an output dataset consisting of rows. The statistics are calculated from entries in the syscollector_execution_stats view. ## Syntax

```sql
fn_syscollector_get_execution_stats ( log_id )
```

---
name: "sys.fn_syscollector_get_execution_details"
title: "fn_syscollector_get_execution_details"
category: "system"
description: "Returns a portion of the SSIS log (sysssislog) matching the package_execution_id for the given package. The table contains one row for each logging entry that is generated at run time by packages or their tasks and containers. The local unique identifier for the execution log. The unique identifier of the logging entry."
tags: ["system","function"]
pubDate: 2026-05-29
syntax: "fn_syscollector_get_execution_details ( log_id )"
---

## Description

Returns a portion of the SSIS log (sysssislog) matching the package_execution_id for the given package. The table contains one row for each logging entry that is generated at run time by packages or their tasks and containers. The local unique identifier for the execution log. The unique identifier of the logging entry.

## Syntax

```sql
fn_syscollector_get_execution_details ( log_id )
```

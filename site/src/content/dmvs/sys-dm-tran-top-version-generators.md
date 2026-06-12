---
name: "sys.dm_tran_top_version_generators"
title: "sys.dm_tran_top_version_generators"
category: "io"
description: "Returns a virtual table for the objects that are producing the most versions in the version store. returns the top 256 aggregated record lengths that are is an inefficient view to run because this view queries the version store, and the version store can be very large."
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_tran_top_version_generators"
---

## Description

Analytics Platform System (PDW) Returns a virtual table for the objects that are producing the most versions in the version store. returns the top 256 aggregated record lengths that are is an inefficient view to run because this view queries the version store, and the version store can be very large. We recommend that you use this function to find the largest consumers of In Azure SQL Database, the values are unique within a

## Syntax

`sys.dm_tran_top_version_generators`

## Examples

### Example 1

```sql
VIEW SERVER STATE
```

### Example 2

```sql
##MS_ServerStateReader##
```

### Example 3

```sql
VIEW DATABASE STATE
```

### Example 4

```sql
##MS_ServerStateReader##
```

---
name: "sys.sp_reset_dtc_log"
title: "sp_reset_dtc_log"
category: "general"
description: "Clears the Microsoft Distributed Transaction Coordinator (MSDTC) log. or have CONTROL SERVER permissions."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_reset_dtc_log
      [ ; ]
---

## Description

Clears the Microsoft Distributed Transaction Coordinator (MSDTC) log. or have CONTROL SERVER permissions.

## Syntax

```sql
sp_reset_dtc_log
[ ; ]
```

## Examples

### Example 1

```sql
0
```

### Example 2

```sql
1
```

### Example 3

```sql
sp_reset_dtc_log
[ ; ]
```

### Example 4

```sql
EXECUTE sp_reset_dtc_log;
```

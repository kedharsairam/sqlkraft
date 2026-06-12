---
name: "sys.sp_flush_commit_table"
title: "sys.sp_flush_commit_table"
category: "general"
description: "to disk to help with change tracking cleanup. Specifies the current change tracking version."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_flush_commit_table
              [ @flush_ts = ] flush_ts
              [ , [ @cleanup_version = ] cleanup_version ]
              [ ; ]
---

## Description

to disk to help with change tracking cleanup. Specifies the current change tracking version.

## Syntax

```sql
sp_flush_commit_table
[ @flush_ts = ] flush_ts
[ , [ @cleanup_version = ] cleanup_version ]
[ ; ]
```

## Examples

### Example 1

`syscommittab`

### Example 2

`NULL`

### Example 3

`syscommittab`

### Example 4

`NULL`

### Example 5

```sql
0
```

### Example 6

```sql
1
```

### Example 7

```sql
sp_flush_commit_table
[ @flush_ts = ] flush_ts
[ , [ @cleanup_version = ] cleanup_version ]
[ ; ]
```

### Example 8

```sql
EXECUTE sys.sp_flush_commit_table 11;
GO
```

---
name: "sys.sp_dropextendedproc"
title: "sp_dropextendedproc"
category: "general"
description: "Drops an extended stored procedure."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropextendedproc [ @functname = ]
              N
              'functname'
              [ ; ]
---

## Description

Drops an extended stored procedure.

## Syntax

```sql
sp_dropextendedproc [ @functname = ]
N
'functname'
[ ; ]
```

## Examples

### Example 1

`sp_dropextendedproc`

### Example 2

`master`

### Example 3

`sp_dropextendedproc`

### Example 4

`EXECUTE`

### Example 5

`sp_dropextendedproc`

### Example 6

`sp_dropextendedproc`

### Example 7

`xp_hello`

### Example 8

```sql
USE master
;
GO
EXECUTE sp_dropextendedproc
'xp_hello'
;
```

### Example 9

```sql
EXECUTE sp_helpextendedproc xp_cmdshell;
GO
```

### Example 10

```sql
sp_addextendedproc sp_dropextendedproc sp_helpextendedproc
```

_(. and 18 more examples)_

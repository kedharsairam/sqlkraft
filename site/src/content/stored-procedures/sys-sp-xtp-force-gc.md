---
name: "sys.sp_xtp_force_gc"
title: "sys.sp_xtp_force_gc"
category: "general"
description: "Causes the in-memory engine to release memory related to deleted rows of in-memory data that are eligible for garbage collection, which haven't yet been released by the process. In cases where a large volume of in-memory data has been released, and where the memory isn't soon be needed for other in-memory data, this procedure can free up memory for other uses."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_xtp_force_gc
              [ [ @dbname = ]
              'database_name'
              ]
              [ ; ]
---

## Description

Causes the in-memory engine to release memory related to deleted rows of in-memory data that are eligible for garbage collection, which haven't yet been released by the process. In cases where a large volume of in-memory data has been released, and where the memory isn't soon be needed for other in-memory data, this procedure can free up memory for other uses.

## Syntax

```sql
sys.sp_xtp_force_gc
[ [ @dbname = ]
'database_name'
]
[ ; ]
```

## Examples

### Example 1

`sys.sp_xtp_force_gc`

### Example 2

```sql
@dbname = N'tempdb'
```

### Example 3

```sql
@dbname =
```

### Example 4

```sql
0
```

### Example 5

`sys.sp_xtp_force_gc`

### Example 6

`sys.dm_xtp_system_memory_consumers`

### Example 7

`sys.sp_xtp_checkpoint_force_garbage_collection`

### Example 8

```sql
EXECUTE sys.sp_xtp_force_gc N
'tempdb'
;
GO
```

### Example 9

```sql
EXECUTE sys.sp_xtp_force_gc;
GO
EXECUTE sys.sp_xtp_force_gc N
'tempdb'
;
GO
EXECUTE sys.sp_xtp_force_gc N
'tempdb'
;
GO
EXECUTE sys.sp_xtp_force_gc;
GO
EXECUTE sys.sp_xtp_force_gc;
GO
```

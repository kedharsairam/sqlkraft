---
name: "sys.sp_help_operator"
title: "sp_help_operator"
category: "general"
description: "Reports information about the operators defined for the server. isn't specified, information about all operators is returned. must be specified, but both can't be specified. The identification number of the operator for which information is requested. must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_operator
              [ [ @operator_name = ]
              N
              'operator_name'
              ]
              [ , [ @operator_id = ] operator_id ]
              [ ; ]
---

## Description

Reports information about the operators defined for the server. isn't specified, information about all operators is returned. must be specified, but both can't be specified. The identification number of the operator for which information is requested. must be specified, but both can't be specified.

## Syntax

```sql
sp_help_operator
[ [ @operator_name = ]
N
'operator_name'
]
[ , [ @operator_id = ] operator_id ]
[ ; ]
```

## Examples

### Example 1

`category_name`

### Example 2

`sp_help_operator`

### Example 3

`msdb`

### Example 4

`EXECUTE`

### Example 5

`msdb`

### Example 6

```sql
François Ajenstat
```

### Example 7

```sql
USE msdb;
GO
EXECUTE dbo.sp_help_operator @operator_name = N
'François Ajenstat'
;
GO
```

---
name: "sys.sp_syscollector_delete_collector_type"
title: "sp_syscollector_delete_collector_type"
category: "general"
description: "Deletes the definition of a collector type. The GUID for the collector type. @collector_type_uid , with a default of and must have a value if The name of the collector type."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_delete_collector_type
              [ [ @collector_type_uid = ]
              'collector_type_uid'
              ]
              [ , [ @name = ]
              N
              'name'
              ]
              [ ; ]
---

## Description

Deletes the definition of a collector type. The GUID for the collector type. @collector_type_uid , with a default of and must have a value if The name of the collector type.

## Syntax

```sql
sp_syscollector_delete_collector_type
[ [ @collector_type_uid = ]
'collector_type_uid'
]
[ , [ @name = ]
N
'name'
]
[ ; ]
```

## Remarks

Deletes the definition of a collector type.

The GUID for the collector type.

@collector_type_uid

, with a default of

and must have a value if

The name of the collector type.

, and must have a value if

@collector_type_uid

(success) or

@collector_type_uid

must have a value; both can't be

## Examples

### Example 1

```sql
USE msdb;
GO
EXECUTE sp_syscollector_delete_collector_type @collector_type_uid =
'302E93D1-
3424-4be7-AA8E-84813ECF2419'
;
```

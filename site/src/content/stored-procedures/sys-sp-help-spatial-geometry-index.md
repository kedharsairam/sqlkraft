---
name: "sys.sp_help_spatial_geometry_index"
title: "sp_help_spatial_geometry_index"
category: "general"
description: "Returns the names and values for a specified set of properties about a The result is returned in a table format. You can choose to return a core set of properties or all Spatial index stored procedures - arguments and properties role to access the procedure. Requires READ ACCESS permission on the server and the object. values aren't included in the return set."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_spatial_geometry_index
              [ @tabname = ]
              N
              'tabname'
              , [ @indexname = ]
              N
              'indexname'
              , [ @verboseoutput = ] verboseoutput
              , [ @query_sample = ] query_sample
              [ ; ]
---

## Description

Returns the names and values for a specified set of properties about a The result is returned in a table format. You can choose to return a core set of properties or all Spatial index stored procedures - arguments and properties role to access the procedure. Requires READ ACCESS permission on the server and the object. values aren't included in the return set.

## Syntax

```sql
sp_help_spatial_geometry_index
[ @tabname = ]
N
'tabname'
, [ @indexname = ]
N
'indexname'
, [ @verboseoutput = ] verboseoutput
, [ @query_sample = ] query_sample
[ ; ]
```

## Examples

### Example 1

`NULL`

### Example 2

```sql
sp_help_spatial_geometry_index
[ @tabname = ]
N
'tabname'
, [ @indexname = ]
N
'indexname'
, [ @verboseoutput = ] verboseoutput
, [ @query_sample = ] query_sample
[ ; ]
```

### Example 3

`sp_help_spatial_geometry_index`

### Example 4

`SIndx_SpatialTable_geometry_col2`

### Example 5

`geometry_col`

### Example 6

```sql
@qs
```

### Example 7

```sql
DECLARE
@qs
AS geometry =
'POLYGON((-90.0 -180.0, -90.0 180.0, 90.0 180.0, 90.0
-180.0, -90.0 -180.0))'
;
EXECUTE sp_help_spatial_geometry_index
'geometry_col'
,
'SIndx_SpatialTable_geometry_col2'
,
0,
@qs;
```

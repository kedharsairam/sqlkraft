---
name: "sys.sp_help_spatial_geography_index"
title: "sp_help_spatial_geography_index"
category: "general"
description: "Returns the names and values for a specified set of properties about a The result is returned in a table format. You can choose to return a core set of properties or all Transact-SQL syntax conventions Spatial index stored procedures - arguments and properties role to access the procedure. Requires READ ACCESS permission on the server and the object. . This example returns only the core properties"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_help_spatial_geography_index"
---

## Description

Returns the names and values for a specified set of properties about a The result is returned in a table format. You can choose to return a core set of properties or all Transact-SQL syntax conventions Spatial index stored procedures - arguments and properties role to access the procedure. Requires READ ACCESS permission on the server and the object. . This example returns only the core properties of the specified index.

## Syntax

`sp_help_spatial_geography_index`

## Examples

### Example 1

`sp_help_spatial_geography_index`

### Example 2

`SIndx_SpatialTable_geography_col2`

### Example 3

`geography_col`

### Example 4

```sql
@qs
```

### Example 5

```sql
sp_help_spatial_geography_index
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

### Example 6

```sql
DECLARE
@qs
AS
GEOGRAPHY =
'POLYGON((-90.0 -180, -90 180.0, 90 180.0, 90 -180, -90
-180.0))'
;
EXECUTE sp_help_spatial_geography_index
'geography_col'
,
'SIndx_SpatialTable_geography_col2'
,
0,
@qs;
```

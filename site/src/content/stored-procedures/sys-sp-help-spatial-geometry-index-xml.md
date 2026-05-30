---
name: "sys.sp_help_spatial_geometry_index_xml"
title: "sp_help_spatial_geometry_index_xml"
category: "general"
description: "Returns the names and values for a specified set of properties about a You can choose to return a core set of properties or all properties of the index. Results are returned in an XML fragment that displays the name and value of the properties Transact-SQL syntax conventions Spatial index stored procedures - arguments and properties User must be a member of the permission on the server and Propert"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_spatial_geometry_index_xml
  [ @tabname = ]
  N
  'tabname'
  , [ @indexname = ]
  N
  'indexname'
  , [ @verboseoutput = ] verboseoutput
  , [ @query_sample = ] query_sample
  , [ @xml_output = ]
  N
  'xml_output'
  OUTPUT
  [ ; ]
---

## Description

Returns the names and values for a specified set of properties about a You can choose to return a core set of properties or all properties of the index. Results are returned in an XML fragment that displays the name and value of the properties Transact-SQL syntax conventions Spatial index stored procedures - arguments and properties User must be a member of the permission on the server and Properties containing values aren't included in the XML return set.

## Syntax

```sql
sp_help_spatial_geometry_index_xml
[ @tabname = ]
N
'tabname'
, [ @indexname = ]
N
'indexname'
, [ @verboseoutput = ] verboseoutput
, [ @query_sample = ] query_sample
, [ @xml_output = ]
N
'xml_output'
OUTPUT
[ ; ]
```

## Remarks

Applies to:

Returns the names and values for a specified set of properties about a

spatial index.

You can choose to return a core set of properties or all properties of the index.

Results are returned in an XML fragment that displays the name and value of the properties

Transact-SQL syntax conventions

Spatial index stored procedures - arguments and properties

User must be a member of the

role. Requires

permission on the server and

the object.

Properties containing

values aren't included in the XML return set.

## Examples

### Example 1

`sp_help_spatial_geometry_index_xml`

### Example 2

`SIndx_SpatialTable_geometry_col2`

### Example 3

`geometry_col`

### Example 4

```sql
@qs
```

### Example 5

```sql
DECLARE
@qs
AS geometry =
'POLYGON((-90.0 -180.0, -90.0 180.0, 90.0 180.0, 90.0
-180.0, -90.0 -180.0))'
;
DECLARE
@x
AS
XML
;
EXECUTE sp_help_spatial_geometry_index_xml
'geometry_col'
,
'SIndx_SpatialTable_geometry_col2'
,
0,
@qs,
@x
OUTPUT
;
SELECT
@x.value(
'(/Primary_Filter_Efficiency/text())[1]'
,
'float'
);
```

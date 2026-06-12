---
name: "sys.sp_help_spatial_geography_index_xml"
title: "sp_help_spatial_geography_index_xml"
category: "general"
description: "Returns the name and value for a specified set of properties about a You can choose to return a core set of properties or all properties of the index. Results are returned in an XML fragment that displays the name and value of the properties Spatial index stored procedures - arguments and properties User must be assigned a role to access the procedure. Requires READ"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_help_spatial_geography_index_xml
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

Returns the name and value for a specified set of properties about a You can choose to return a core set of properties or all properties of the index. Results are returned in an XML fragment that displays the name and value of the properties Spatial index stored procedures - arguments and properties User must be assigned a role to access the procedure. Requires READ ACCESS permission on the server and the object. Properties containing values aren't included in the return set.

## Syntax

```sql
sp_help_spatial_geography_index_xml
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

Returns the name and value for a specified set of properties about a

spatial index.

You can choose to return a core set of properties or all properties of the index.

Results are returned in an XML fragment that displays the name and value of the properties

Spatial index stored procedures - arguments and properties

User must be assigned a

role to access the procedure. Requires READ ACCESS

permission on the server and the object.

Properties containing

values aren't included in the return set.

## Examples

### Example 1

`sp_help_spatial_geography_index_xml`

### Example 2

```sql
@qs
```

### Example 3

```sql
DECLARE
@qs
AS
GEOGRAPHY =
'POLYGON((-90.0 -180, -90 180.0, 90 180.0, 90 -180, -90
-180.0))'
;
DECLARE
@x
AS
XML
;
EXECUTE sp_help_spatial_geography_index_xml
'geography_col'
,
'SIndx_SpatialTable_geography_col2'
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

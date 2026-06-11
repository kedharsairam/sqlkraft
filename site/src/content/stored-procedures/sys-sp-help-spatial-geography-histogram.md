---
name: "sys.sp_help_spatial_geography_histogram"
title: "sp_help_spatial_geography_histogram"
category: "general"
description: "Facilitates the keying of grid parameters for a spatial index. The qualified or nonqualified name of the table for which the spatial index was specified. Quotation marks are required only if a qualified table is specified. If a fully qualified name, including a database name, is provided, the database name must be the name of the current The name of the spatial column specified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_spatial_geography_histogram
  [ @tabname = ]
  N
  'tabname'
  , [ @colname = ]
  N
  'colname'
  , [ @resolution = ] resolution
  [ , [ @sample = ] sample ]
  [ ; ]
---

## Description

Facilitates the keying of grid parameters for a spatial index. The qualified or nonqualified name of the table for which the spatial index was specified. Quotation marks are required only if a qualified table is specified. If a fully qualified name, including a database name, is provided, the database name must be the name of the current The name of the spatial column specified. The resolution of the bounding box. Valid values are from 10 to 5000.

## Syntax

```sql
sp_help_spatial_geography_histogram
[ @tabname = ]
N
'tabname'
, [ @colname = ]
N
'colname'
, [ @resolution = ] resolution
[ , [ @sample = ] sample ]
[ ; ]
```

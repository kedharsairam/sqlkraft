---
name: "sys.sp_help_spatial_geometry_histogram"
title: "sp_help_spatial_geometry_histogram"
category: "general"
description: "Facilitates the keying of bounding box and grid parameters for a spatial index. The qualified or nonqualified name of the table for which the spatial index is specified. Quotation marks are required only if a qualified table is specified. If a fully qualified name, including a database name, is provided, the database name must be the name of the current The name of the spatial column specified. Th"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_spatial_geometry_histogram
              [ @tabname = ]
              N
              'tabname'
              , [ @colname = ]
              N
              'colname'
              , [ @resolution = ] resolution
              , [ @xmin = ] xmin
              , [ @ymin = ] ymin
              , [ @xmax = ] xmax
              , [ @ymax = ] ymax
              [ , [ @sample = ] sample ]
              [ ; ]
---

## Description

Facilitates the keying of bounding box and grid parameters for a spatial index. The qualified or nonqualified name of the table for which the spatial index is specified. Quotation marks are required only if a qualified table is specified. If a fully qualified name, including a database name, is provided, the database name must be the name of the current The name of the spatial column specified. The resolution of the bounding box. Valid values are from 10 to 5000.

## Syntax

```sql
sp_help_spatial_geometry_histogram
[ @tabname = ]
N
'tabname'
, [ @colname = ]
N
'colname'
, [ @resolution = ] resolution
, [ @xmin = ] xmin
, [ @ymin = ] ymin
, [ @xmax = ] xmax
, [ @ymax = ] ymax
[ , [ @sample = ] sample ]
[ ; ]
```

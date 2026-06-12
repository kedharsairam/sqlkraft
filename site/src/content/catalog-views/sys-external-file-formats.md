---
name: "sys.external_file_formats"
title: "sys.external_file_formats"
category: "external"
description: "2016 (13.x) and later Azure SQL Database Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) Removes a PolyBase external file format."
tags: ["external","catalog-view"]
pubDate: "2026-05-29"
syntax: |
  -- Drop an external file format
      DROP
      EXTERNAL
      FILE
      FORMAT
      external_file_format_name
      [;]
---

## Description

2016 (13.x) and later Azure SQL Database Managed Instance Removes a PolyBase external file format.

## Syntax

```sql
-- Drop an external file format
DROP
EXTERNAL
FILE
FORMAT external_file_format_name
[;]
```

## Remarks

2016 (13.x) and later

Managed Instance

Analytics Platform System (PDW)

Removes a PolyBase external file format.

The name of the external file format to drop.

To view a list of external file formats use the

sys.external_file_formats

system view.

Requires ALTER ANY EXTERNAL FILE FORMAT.

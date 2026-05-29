---
name: 'sys.external_file_formats'
title: 'sys.external_file_formats'
category: 'external'
description: 'SQL Server 2016 (13.x) and later Azure SQL Database Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) Removes a PolyBase external file format. Transact-SQL syntax conventions The name of the external file format to drop. To view a list of external file formats use the sys.external_file_formats Requires ALTER ANY EXTERNAL FILE FORMAT.'
tags: ["external", "catalog-view"]
pubDate: 2026-05-29
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

SQL Server 2016 (13.x) and later Azure SQL Database Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) Removes a PolyBase external file format. Transact-SQL syntax conventions The name of the external file format to drop. To view a list of external file formats use the sys.external_file_formats Requires ALTER ANY EXTERNAL FILE FORMAT.

## Syntax

```sql
-- Drop an external file format
DROP
EXTERNAL
FILE
FORMAT
external_file_format_name
[;]
```

## Remarks

Applies to:

SQL Server 2016 (13.x) and later

Azure SQL Database

Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

Removes a PolyBase external file format.

Transact-SQL syntax conventions

The name of the external file format to drop.

To view a list of external file formats use the

sys.external_file_formats

system view.

Requires ALTER ANY EXTERNAL FILE FORMAT.

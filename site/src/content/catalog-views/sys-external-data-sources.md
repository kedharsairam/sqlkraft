---
name: 'sys.external_data_sources'
title: 'sys.external_data_sources'
category: 'external'
description: 'SQL Server 2016 (13.x) and later versions Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each external data source in the current database for SQL Server, Azure SQL Database, and Azure Synapse Analytics. Contains a row for each external data source on the server for Analytics Platform System Object ID for the external data Data source type displayed as a Data s'
tags: ["external", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  REMOTE_DATA_ARCHIVE
  4
---

## Description

SQL Server 2016 (13.x) and later versions Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each external data source in the current database for SQL Server, Azure SQL Database, and Azure Synapse Analytics. Contains a row for each external data source on the server for Analytics Platform System Object ID for the external data Data source type displayed as a Data source type displayed as a

## Syntax

```sql
REMOTE_DATA_ARCHIVE
4
```

## Permissions

SQL) 06/18/2025 Applies to: SQL Server 2016 (13.x) and later Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) Removes an external data source used for PolyBase and data virtualization features. Transact-SQL syntax conventions syntaxsql The name of the external data source to drop. To view a list of external data sources, use the system view. SQL Requires ALTER ANY EXTERNAL DATA SOURCE.

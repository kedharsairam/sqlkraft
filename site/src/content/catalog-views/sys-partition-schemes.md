---
name: "sys.partition_schemes"
title: "sys.partition_schemes"
category: "partitions"
description: "Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Contains a row for each Data Space that is a partition scheme, with sys.data_spaces (Transact-SQL) ID of partition function used in the scheme. For a list of columns that this view inherits, see sys.data_spaces (Transact-SQL) role. For more information, see Querying the SQL Server System Catalog FAQ"
tags: ["partitions", "catalog-view"]
pubDate: 2026-05-29
syntax: "sys.partition_schemes"
---

## Description

Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Contains a row for each Data Space that is a partition scheme, with sys.data_spaces (Transact-SQL) ID of partition function used in the scheme. For a list of columns that this view inherits, see sys.data_spaces (Transact-SQL) role. For more information, see Querying the SQL Server System Catalog FAQ

## Syntax

```sql
sys.partition_schemes
```

## Permissions

Article • 05/23/2023 Applies to: SQL Server Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric Contains a row for each Data Space that is a partition scheme, with = PS. Description Inherits columns from sys.data_spaces (Transact-SQL) . ID of partition function used in the scheme. For a list of columns that this view inherits, see sys.data_spaces (Transact-SQL) Requires membership in the role. For more information, see Metadata Visibility Configuration . Catalog Views (Transact-SQL) Querying the SQL Server System Catalog FAQ ﾉ Expand table See Also Article • 11/18/2022 Applies to: SQL Server Contains a row for each data space destination of a partition scheme. Description ID of the partition-scheme that is partitioning to the data space. For partitioned tables, this can be joined to in . ID (1-based ordinal) of the destination-mapping, unique within the partition scheme. ID of the data space to which data for this scheme's destination is being mapped. Requires membership in the role. For more information, see Metadata Visibility Configuration . Catalog Views (Transact-SQL) Create Partitioned Tables and Indexes sys.partition_schemes ﾉ Expand table See Also Modify a partition scheme sys.partition_functions (Transact-SQL) sys.partition_schemes (Transact-SQL) Last updated on 11/18/2025

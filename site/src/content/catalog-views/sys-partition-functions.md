---
name: "sys.partition_functions"
title: "sys.partition_functions"
category: "partitions"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each partition function in SQL Server. Name of the partition function. Is unique within the database. Partition function ID. Is unique within the database. Number of partitions created by the function. 1 = Boundary value is included in the RIGHT range of the : SQL Server 2012 (11.x) and later. 1 = Object is used fo"
tags: ["partitions", "catalog-view"]
pubDate: 2026-05-29
syntax: "ALTER PARTITION FUNCTION"
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each partition function in SQL Server. Name of the partition function. Is unique within the database. Partition function ID. Is unique within the database. Number of partitions created by the function. 1 = Boundary value is included in the RIGHT range of the : SQL Server 2012 (11.x) and later. 1 = Object is used for full-text index fragments.

## Syntax

```sql
ALTER PARTITION FUNCTION
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Contains a row for each partition function in SQL Server. Description Name of the partition function. Is unique within the database. Partition function ID. Is unique within the database. Function type. R = Range Function type. RANGE Number of partitions created by the function. For range partitioning. 1 = Boundary value is included in the RIGHT range of the boundary. 0 = LEFT. : SQL Server 2012 (11.x) and later. 1 = Object is used for full-text index fragments. 0 = Object is not used for full-text index fragments. Date the function was created. Date the function was last modified using an ALTER statement. Requires membership in the role. For more information, see Metadata Visibility Configuration . ﾉ Expand table

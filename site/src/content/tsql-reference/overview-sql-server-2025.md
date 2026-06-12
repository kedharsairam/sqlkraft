---
name: "Overview: SQL Server 2025"
title: "Overview: SQL Server 2025"
category: "statements"
description: "2016 (13.x) and later versions"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

2016 (13.x) and later versions

Analytics Platform System (PDW)

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

Creates an external data source for querying external data, used for PolyBase and data virtualization features.

This article provides the syntax, arguments, remarks, permissions, and examples for whichever SQL product you

choose.

In the following row, select the product name you're interested in, and only that product's information is displayed.

- SQL Server \*

SQL Managed

Instance

Azure Synapse

Analytics

Analytics Platform

System (PDW)

Microsoft Fabric Data Warehouse

Microsoft Fabric SQL database

Applies to

: SQL Server 2025 (17.x)

Creates an external data source for PolyBase queries. External data sources are used to establish connectivity and

support these primary use cases:

Data virtualization and data load using

PolyBase in SQL Server

Bulk load operations using

or

Supports Managed Identity connections for instances enabled by Azure Arc. For details, review

Connect to Azure

Storage with managed identity from PolyBase.

７

Note

This syntax varies in different versions of SQL Server. Use the version selector dropdown list to choose the

appropriate version. This content applies to SQL Server 2025 (17.x) and later versions.

```sql
BULK INSERT
```

`OPENROWSET`

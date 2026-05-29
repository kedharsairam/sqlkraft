---
name: "sys.dm_os_ring_buffers"
title: "sys.dm_os_ring_buffers"
category: "os"
description: "Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Each row represents a record in a ring buffer of a specific type. Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. Not nullable. The type of the ring buffer record. Not nullable. The time when a ring buffer record was added, in milliseconds since the computer started. No"
tags: ["os", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_os_ring_buffers"
---

## Description

Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Each row represents a record in a ring buffer of a specific type. Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. Not nullable. The type of the ring buffer record. Not nullable. The time when a ring buffer record was added, in milliseconds since the computer started. Not nullable. Identified for informational purposes only. Not supported unless described in the official Microsoft product documentation, or used as directed by Microsoft for diagnostic and troubleshooting purposes. Future compatibility is not guaranteed. Nullable. Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. Not nullable. SQL Server 2025 (17.x) Preview

## Syntax

```sql
sys.dm_os_ring_buffers
```

## Remarks

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Each row represents a record in a ring buffer of a specific type.

Identified for informational purposes only. Not supported. Future

compatibility is not guaranteed. Not nullable.

The type of the ring buffer record. Not nullable.

The time when a ring buffer record was added, in milliseconds

since the computer started. Not nullable.

Identified for informational purposes only. Not supported unless

described in the official Microsoft product documentation, or

used as directed by Microsoft for diagnostic and troubleshooting

purposes. Future compatibility is not guaranteed. Nullable.

Identified for informational purposes only. Not supported. Future

compatibility is not guaranteed. Not nullable.

SQL Server 2025 (17.x) Preview

The time when a ring buffer record was added, in the local time

of the Database Engine instance. Not nullable.

SQL Server 2025 (17.x) Preview

A ring buffer is a memory structure within the Database Engine that is limited to a fixed

number of records. As new records arrive, older records are removed.

Records in ring buffers contain diagnostic data for the Database Engine. Most ring buffer types

are used for internal purposes and aren't supported, unless described in the official Microsoft

product documentation. For example, you can

use ring buffers to obtain health information

about Always On availability groups

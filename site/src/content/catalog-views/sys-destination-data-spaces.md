---
name: "sys.destination_data_spaces"
title: "sys.destination_data_spaces"
category: "compatibility"
description: "Contains a row for each data space destination of a partition scheme."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "sys.partition_schemes"
---

## Description

Contains a row for each data space destination of a partition scheme. ID of the partition-scheme that is partitioning to the data space. For partitioned tables, this can be joined to ID (1-based ordinal) of the destination-mapping, unique within the ID of the data space to which data for this scheme's destination is being role. For more information, see Create Partitioned Tables and Indexes

## Syntax

`sys.partition_schemes`

## Permissions

Article • 11/18/2022 Applies to: SQL Server Contains a row for each data space destination of a partition scheme. Description ID of the partition-scheme that is partitioning to the data space. For partitioned tables, this can be joined to in . ID (1-based ordinal) of the destination-mapping, unique within the partition scheme. ID of the data space to which data for this scheme's destination is being mapped. Requires membership in the role. For more information, see Metadata Visibility Configuration . Catalog Views (Transact-SQL) Create Partitioned Tables and Indexes sys.partition_schemes ﾉ Expand table See Also

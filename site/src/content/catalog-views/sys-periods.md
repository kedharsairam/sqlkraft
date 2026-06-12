---
name: "sys.periods"
title: "sys.periods"
category: "compatibility"
description: "2016 (13.x) and later versions Returns a row for each table for which periods have been defined. The numeric value representing the type of period: The text description of the type of column: The id of the table containing the period_type column The id of the column that defines the lower period boundary The id of the column that defines the upper period boundary The visibility of the m"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

2016 (13.x) and later versions Returns a row for each table for which periods have been defined. The numeric value representing the type of period: The text description of the type of column: The id of the table containing the period_type column The id of the column that defines the lower period boundary The id of the column that defines the upper period boundary The visibility of the metadata in catalog views is limited to securables that a user either owns,

## Permissions

Article • 02/28/2023 x) and later versions Returns a row for each table for which periods have been defined. Description name Name of the period period_type The numeric value representing the type of period: 1 = system-time period period_type_desc The text description of the type of column: SYSTEM_TIME_PERIOD object_id The id of the table containing the period_type column start_column_id The id of the column that defines the lower period boundary end_column_id The id of the column that defines the upper period boundary The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. System Views (Transact-SQL) Object Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) sys.all_columns (Transact-SQL) sys.system_columns (Transact-SQL) Querying the SQL Server System Catalog FAQ Temporal Tables ﾉ Expand table See Also

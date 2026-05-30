---
name: "sys.change_tracking_tables"
title: "sys.change_tracking_tables"
category: "objects"
description: "SQL database in Microsoft Fabric Returns one row for each table in the current database that has change tracking enabled. ID of a table that has a change journal. The table can have a change journal even if change tracking is currently off. The table ID is unique within the database. Current state of change tracking on the table: Version of the database when change tracking began for the table. Th"
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: "sys.change_tracking_tables"
---

## Description

SQL database in Microsoft Fabric Returns one row for each table in the current database that has change tracking enabled. ID of a table that has a change journal. The table can have a change journal even if change tracking is currently off. The table ID is unique within the database. Current state of change tracking on the table: Version of the database when change tracking began for the table. This version is usually indicates when change tracking was

## Syntax

`sys.change_tracking_tables`

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Returns one row for each table in the current database that has change tracking enabled. Description object_id ID of a table that has a change journal. The table can have a change journal even if change tracking is currently off. The table ID is unique within the database. is_track_columns_updated_on Current state of change tracking on the table: 0 = OFF 1 = ON begin_version Version of the database when change tracking began for the table. This version is usually indicates when change tracking was enabled, but this value is reset if the table is truncated. cleanup_version Version up to which cleanup might have removed change tracking information. min_valid_version Minimum valid version of change tracking information that is available for the table. When obtaining changes from the table that is associated with this row, the value of last_sync_version must be greater than or equal to the version reported by this column. For more information, see CHANGE_TRACKING_MIN_VALID_VERSION (Transact-SQL) . The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . ﾉ Expand table SQL Here's the result set. Output This procedure must be run in a database that has change tracking enabled. When you run the stored procedure, one of the following scenarios happens: If the table doesn't exist or if change tracking isn't enabled, appropriate error messages are thrown. This stored procedure calls another internal stored procedure that cleans up contents from the change tracking side table that's based on the invalid cleanup version by using the dynamic management view. When it's running, it shows the information of total rows deleted (for every 5000 rows). This stored procedure is available in the following products: SQL Server 2016 (13.x) Service Pack 1 and later versions Azure SQL Database and Azure SQL Managed Instance Only a member of the server role or database role can execute this procedure.

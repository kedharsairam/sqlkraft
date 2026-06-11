---
name: "sys.database_scoped_configurations"
title: "sys.database_scoped_configurations"
category: "configuration"
description: "SQL Server 2016 (13.x) and later versions Azure SQL Database SQL Managed Instance Azure Synapse Analytics SQL analytics endpoint in Microsoft Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Contains one row per configuration."
tags: ["configuration", "catalog-view"]
pubDate: 2026-05-29
syntax: "ALTER DATABASE SCOPED CONFIGURATION"
---

## Description

SQL Server 2016 (13.x) and later versions Azure SQL Database SQL Managed Instance Azure Synapse Analytics SQL analytics endpoint in Microsoft Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Contains one row per configuration. ID of the configuration option. The name of the configuration option. For information about the possible configurations, see ALTER DATABASE SCOPED CONFIGURATION (Transact-SQL) The value set for this configuration option for the primary replica. The value set for this configuration option for the secondary Specifies whether the value set is the default value. Added in SQL Requires membership in the When NULL is returned as the value for , this means that the secondary is set to PRIMARY. Database scoped configuration settings will be carried over with the database. This means that

## Syntax

```sql
ALTER DATABASE SCOPED CONFIGURATION
```

## Remarks

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

SQL Managed Instance

Azure Synapse Analytics

SQL analytics endpoint in Microsoft

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Contains one row per configuration.

Description

ID of the configuration option.

The name of the configuration option. For information about the

possible configurations, see

ALTER DATABASE SCOPED

CONFIGURATION (Transact-SQL)

The value set for this configuration option for the primary replica.

The value set for this configuration option for the secondary

Specifies whether the value set is the default value. Added in SQL

Server 2017.

Requires membership in the

When NULL is returned as the value for

, this means that the secondary is

set to PRIMARY.

Database scoped configuration settings will be carried over with the database. This means that

when a given database is restored or attached, the existing configuration settings remain.

ALTER DATABASE SCOPED CONFIGURATION (Transact-SQL)

Expand table

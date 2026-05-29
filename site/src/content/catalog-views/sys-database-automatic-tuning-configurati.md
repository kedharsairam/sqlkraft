---
name: 'sys.database_automatic_tuning_configurati'
title: 'sys.database_automatic_tuning_configurati'
category: 'configuration'
description: 'SQL Server 2022 (16.x) and later versions'
tags: ["catalog-view", "configuration"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2022 (16.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric


## Returns the
Automatic plan correction

component of the

Automatic tuning

configuration

settings that are enabled for the current database.


## Description
The name of the automatic tuning configuration option. See

sp_configure_automatic_tuning

for the list of available configuration

options.

Indicates the desired option for the automatic tuning configuration.

Describes the automatic tuning configuration target type.

Indicates the query ID from Query Store that the automatic tuning

configuration option is operating on.

Textual description of the automatic tuning configuration option.

Indicates the state of the automatic tuning configuration option.

Requires the

permission.

Automatic tuning

ALTER DATABASE SET options (Transact-SQL)

sys.database_query_store_options (Transact-SQL)

sys.dm_db_tuning_recommendations (Transact-SQL)

sys.database_automatic_tuning_mode

sp_configure_automatic_tuning (Transact-SQL)

ﾉ

Expand table

Related content

Last updated on 11/18/2025

```sql
option
```

```sql
option_value
```

```sql
type
```

```sql
type_value
```

```sql
details
```

```sql
state
```

```sql
VIEW DATABASE STATE
```

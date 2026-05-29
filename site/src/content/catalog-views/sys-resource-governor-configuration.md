---
name: 'sys.resource_governor_configuration'
title: 'sys.resource_governor_configuration'
category: 'configuration'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "configuration"]
pubDate: 2026-05-29
---

Article

•

02/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance


## Returns the stored resource governor configuration.

## Description
The object ID of the classifier function in

sys.objects

. Not

nullable.

Note

This function is used to classify new sessions and uses

rules to route the workload to the appropriate workload

group. For more information, see

Resource governor

.

Indicates the current state of resource governor:

0 = is not enabled.

1 = is enabled.

Not nullable.

: SQL Server 2014 (12.x) and later.

The maximum number of outstanding I/O requests per

volume.

The catalog view displays resource governor configuration as stored in metadata. To see the

currently effective configuration, use

sys.dm_resource_governor_configuration

.

Requires the

permission to view contents.

ﾉ

Expand table

The following example shows how to get and compare the stored metadata values and the

currently effective values of resource governor configuration.

SQL

Resource governor catalog views (Transact-SQL)

Catalog Views (Transact-SQL)

sys.dm_resource_governor_configuration (Transact-SQL)

Resource governor

Related content

```sql
classifier_function_id
```

```sql
is_enabled
```

```sql
max_outstanding_io_per_volume
```

```sql
VIEW ANY DEFINITION
```

```sql
USE
master
;
-- Get the stored metadata
SELECT
OBJECT_SCHEMA_NAME(classifier_function_id)
AS
classifier_function_schema_name,
OBJECT_NAME(classifier_function_id)
AS
classifier_function_name
FROM
sys.resource_governor_configuration;
-- Get the currently effective configuration
SELECT
OBJECT_SCHEMA_NAME(classifier_function_id)
AS
classifier_function_schema_name,
OBJECT_NAME(classifier_function_id)
AS
classifier_function_name
FROM
sys.dm_resource_governor_configuration;
```

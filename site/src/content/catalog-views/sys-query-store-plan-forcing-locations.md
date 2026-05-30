---
name: "sys.query_store_plan_forcing_locations"
title: "sys.query_store_plan_forcing_locations"
category: "query-store"
description: "Contains information about Query Store plans that have been forced on secondary replicas , when Query Store for secondary replicas is enabled. You can use this information to determine what queries have plans forced on different replica sets. Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later versions, and in Azure SQL Database. For complete platform suppo"
tags: ["query-store", "catalog-view"]
pubDate: 2026-05-29
syntax: "plan_forcing_location_id"
---

## Description

Contains information about Query Store plans that have been forced on secondary replicas , when Query Store for secondary replicas is enabled. You can use this information to determine what queries have plans forced on different replica sets. Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later versions, and in Azure SQL Database. For complete platform support, see

## Syntax

```sql
plan_forcing_location_id
```

## Examples

### Example 1

```sql
plan_forcing_location_id
```

### Example 2

```sql
query_id
```

### Example 3

```sql
query_id
```

### Example 4

```sql
plan_id
```

### Example 5

```sql
plan_id
```

### Example 6

```sql
replica_group_id
```

### Example 7

```sql
force_plan_scope
```

### Example 8

```sql
replica_group_id
```

### Example 9

```sql
VIEW DATABASE STATE
```

### Example 10

```sql
sys.query_store_plan_forcing_locations
```

_(... and 1 more examples)_

---
name: "sys.sp_query_store_clear_message_queues"
title: "sp_query_store_clear_message_queues"
category: "general"
description: "Clears all queued (non-persisted) Query Store messages pending for the replica against which Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later versions, and in Azure SQL Database. For complete platform support, see Transact-SQL syntax conventions Requires the ALTER permission on the database. The following example clears all queued (non-persisted) Query S"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_query_store_clear_message_queues"
---

## Description

Clears all queued (non-persisted) Query Store messages pending for the replica against which Query Store for secondary replicas is supported starting in SQL Server 2025 (17.x) and later versions, and in Azure SQL Database. For complete platform support, see Transact-SQL syntax conventions Requires the ALTER permission on the database. The following example clears all queued (non-persisted) Query Store messages pending. The

## Syntax

```sql
sp_query_store_clear_message_queues
```

## Examples

### Example 1

```sql
sp_query_store_clear_message_queues
```

### Example 2

```sql
0
```

### Example 3

```sql
1
```

### Example 4

```sql
sp_query_store_clear_message_queues
[ ; ]
```

### Example 5

```sql
EXECUTE
sp_query_store_clear_message_queues;
```

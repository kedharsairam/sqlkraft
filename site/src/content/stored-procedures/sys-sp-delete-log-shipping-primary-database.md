---
name: 'sys.sp_delete_log_shipping_primary_database'
title: 'sp_delete_log_shipping_primary_database'
category: 'general'
description: 'This stored procedure removes log shipping of primary database including backup job, local and remote history. Only use this stored procedure after you remove the secondary databases Transact-SQL syntax conventions The name of the log shipping primary database. Identified for informational purposes only. Not supported. Future compatibility is not'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_delete_log_shipping_primary_secondary'
---

## Description

This stored procedure removes log shipping of primary database including backup job, local and remote history. Only use this stored procedure after you remove the secondary databases Transact-SQL syntax conventions The name of the log shipping primary database. Identified for informational purposes only. Not supported. Future compatibility is not

## Syntax

```sql
sp_delete_log_shipping_primary_secondary
```

## Examples

### Example 1

```sql
sp_delete_log_shipping_primary_database
```

### Example 2

```sql
master
```

### Example 3

```sql
log_shipping_monitor_primary
```

### Example 4

```sql
log_shipping_monitor_history_detail
```

### Example 5

```sql
log_shipping_monitor_error_detail
```

### Example 6

```sql
log_shipping_monitor_primary
```

### Example 7

```sql
log_shipping_monitor_history_detail
```

### Example 8

```sql
log_shipping_monitor_error_detail
```

### Example 9

```sql
log_shipping_primary_databases
```

### Example 10

```sql
sp_delete_log_shipping_alert_job
```


*(... and 3 more examples)*

---
name: "sys.sp_delete_log_shipping_primary_database"
title: "sp_delete_log_shipping_primary_database"
category: "general"
description: "This stored procedure removes log shipping of primary database including backup job, local and remote history. Only use this stored procedure after you remove the secondary databases The name of the log shipping primary database. Identified for informational purposes only. Not supported."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "sp_delete_log_shipping_primary_secondary"
---

## Description

This stored procedure removes log shipping of primary database including backup job, local and remote history. Only use this stored procedure after you remove the secondary databases The name of the log shipping primary database. Identified for informational purposes only. Not supported.

## Syntax

`sp_delete_log_shipping_primary_secondary`

## Examples

### Example 1

`sp_delete_log_shipping_primary_database`

### Example 2

`master`

### Example 3

`log_shipping_monitor_primary`

### Example 4

`log_shipping_monitor_history_detail`

### Example 5

`log_shipping_monitor_error_detail`

### Example 6

`log_shipping_monitor_primary`

### Example 7

`log_shipping_monitor_history_detail`

### Example 8

`log_shipping_monitor_error_detail`

### Example 9

`log_shipping_primary_databases`

### Example 10

`sp_delete_log_shipping_alert_job`

_(. and 3 more examples)_

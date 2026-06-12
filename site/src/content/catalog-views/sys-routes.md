---
name: "sys.routes"
title: "sys.routes"
category: "compatibility"
description: "This catalog views contains one row per route. Service Broker uses routes to locate the network Name of the route, unique within the database. Not NULLABLE. Identifier for the route. Not NULLABLE. Identifier for the database principal that owns the route."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "//Adventure-Works.com/Expenses"
---

## Description

This catalog views contains one row per route. Service Broker uses routes to locate the network Name of the route, unique within the database. Not NULLABLE. Identifier for the route. Not NULLABLE. Identifier for the database principal that owns the route.

## Syntax

```sql
//Adventure-Works.com/Expenses
```

## Permissions

Article • 02/28/2023 This catalog views contains one row per route. Service Broker uses routes to locate the network address for a service. Description Name of the route, unique within the database. Not NULLABLE. Identifier for the route. Not NULLABLE. Identifier for the database principal that owns the route. NULLABLE. Name of the remote service. NULLABLE. Identifier of the broker that hosts the remote service. NULLABLE. The date and time when the route expires. Notice that this value does not use the local time zone. Instead, the value shows the expiration time for UTC. NULLABLE. Network address to which Service Broker sends messages for the remote service. NULLABLE. For SQL Managed Instance, address must be local. Network address of the mirroring partner for the server specified in the address. NULLABLE. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. ﾉ Expand table

## Examples

### Example 1

`ExpenseRoute`

### Example 2

```sql
DROP
ROUTE route_name
[ ; ]
```

---
name: "sys.soap_endpoints"
title: "sys.soap_endpoints"
category: "compatibility"
description: "This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Returns one row for each endpoint in the server that carries a SOAP-type payload. For every row in this view, there's a corresponding row with the same catalog view that carries the HTTP configuration metadata."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Returns one row for each endpoint in the server that carries a SOAP-type payload. For every row in this view, there's a corresponding row with the same catalog view that carries the HTTP configuration metadata. For a list of columns that this view inherits, see

## Code Blocks

`endpoint_id`

`sys.http_endpoints`

```sql
https://tempuri.org
```

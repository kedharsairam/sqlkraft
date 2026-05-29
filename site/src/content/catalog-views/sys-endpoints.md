---
name: 'sys.endpoints'
title: 'sys.endpoints'
category: 'objects'
description: 'Indicates whether the endpoint is for administrative use.'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
Indicates whether the endpoint is for administrative use.

0 = Nonadministrative endpoint.

1 = Endpoint is an administrative endpoint.

Not nullable.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Requires VIEW SERVER SECURITY STATE permission on the server.

Endpoints Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Last updated on 03/03/2026


## Permissions for SQL Server 2022 and later
Related content

```sql
is_admin_endpoint
```

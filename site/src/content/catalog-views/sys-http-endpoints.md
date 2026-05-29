---
name: 'sys.http_endpoints'
title: 'sys.http_endpoints'
category: 'objects'
description: '1 = Integrated authentication is enabled using the'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
1 = Integrated authentication is enabled using the

AUTHENTICATION = INTEGRATED option.

Hint that is returned to the client as part of the HTTP

DIGEST authentication challenge. The value of the AUTH

REALM option.

Is NULL if not specified or if DIGEST authentication isn't

enabled.

Default login domain if you enable BASIC authentication.

The value of the DEFAULT LOGON DOMAIN option.

Is NULL if not specified or if BASIC authentication isn't

enabled.

1 = COMPRESSION = ENABLED option is set.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Requires VIEW SERVER SECURITY STATE permission on the server.

Catalog Views (Transact-SQL)

Endpoints Catalog Views (Transact-SQL)

Last updated on 03/03/2026


## Permissions for SQL Server 2022 and later
Related content

```sql
is_integrated_auth_enabled
```

```sql
authorization_realm
```

```sql
default_logon_domain
```

```sql
is_compression_enabled
```

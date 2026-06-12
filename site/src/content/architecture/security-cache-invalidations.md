---
title: "Security cache invalidations"
topic: "io-fundamentals"
description: "tokens. All different securables inside the database."
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

## Description

One per database

tokens. All different securables inside the database.

This section describes issues with the security cache.

Various scenarios can trigger security cache invalidations at either the database or server level.

When an invalidation occurs, all current cache entries are invalidated.

permission checks follow the full "No cache" workflow until the caches are repopulated.

active connections need to rebuild the cached entries.

this impact worse.

database are treated as server-wide invalidations,

affecting the caches in all databases on the instance.

2025 introduces a feature that invalidates caches for only a specific login. This

affected login are affected.

login L2 remain unaffected.

permission changes for individual logins. Group logins continue to experience server-level

invalidation.

security cache.

Specified

database

ﾉ

`ObjectPerm`

`ObjPerm`

`master`

```sql
CREATE/ALTER/DROP
APPLICATION ROLE
SYMMETRIC KEY
ASYMMETRIC KEY
AUTHORIZATION
CERTIFICATE
ROLE
SCHEMA
USER
```

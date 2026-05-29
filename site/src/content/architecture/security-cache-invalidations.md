---
title: 'Security cache invalidations'
topic: 'io-fundamentals'
description: 'tokens. All different securables inside the database.'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

## Description
One per database

tokens. All different securables inside the database.

This section describes issues with the security cache.

Various scenarios can trigger security cache invalidations at either the database or server level.

When an invalidation occurs, all current cache entries are invalidated. All future queries and

permission checks follow the full "No cache" workflow until the caches are repopulated.

Invalidation can significantly impact server performance, especially under high load, as all

active connections need to rebuild the cached entries. Repeated cache invalidations can make

this impact worse. Invalidations in the

database are treated as server-wide invalidations,

affecting the caches in all databases on the instance.

SQL Server 2025 introduces a feature that invalidates caches for only a specific login. This

means that when security cache entries are invalidated, only those entries belonging to the

affected login are affected. For instance, if you grant login L1 a new permission, the tokens for

login L2 remain unaffected.

As an initial step, this feature applies to the CREATE, ALTER and DROP login scenarios, and

permission changes for individual logins. Group logins continue to experience server-level

invalidation.

The table below lists all security Data Definition Language (DDL) actions that invalidate the

security cache.

Specified

database

ﾉ

Expand table

```sql
ObjectPerm
```

```sql
ObjPerm
```

```sql
master
```

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

---
title: 'Security cache stores'
topic: 'query-processing'
description: 'name. There''s one user token per database for a login.'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

## Description
name. There's one user token per database for a login.

Records all permissions for a securable object for a UserToken or SecContextToken.

Key is the class and ID of a securable object. The entry is a series of lists containing

audit IDs for each auditable operation on an object. Server audit is based on

permission checks, detailing each auditable operation a specific user has on a

particular object.

This cache stores query permission check results for individual queries, with one

entry per query plan. It's the most important and commonly used cache, as it's the

first thing checked during query execution. To prevent ad hoc queries from flooding

the cache, it only stores query permission check results if the query is executed three

times.

This records all permissions for an object in the database for all users within the

database. The difference between TokenPerm and ObjectPerm is that TokenPerm is

for a specific user, while ObjectPerm can be for all users in the database.

The tokens are stored inside different cache stores.


## Description
One big store which contains all of the following objects:

-

-

-

-

-

Access check result (ACR) store. Every login has their own separate security

context user store.

Access check result store

-

-

Every user has individual ACR user store. For example, two logins with five users

in two different databases amounts to two

and 10

different

.

ﾉ

Expand table

```sql
TokenPerm
```

```sql
TokenAudit
```

```sql
TokenAccessResult
```

```sql
ObjectPerm
```

```sql
TokenAndPermUserStore
```

```sql
SecContextToken
```

```sql
LoginToken
```

```sql
UserToken
```

```sql
TokenPerm
```

```sql
TokenAudit
SecCtxtACRUserStore
```

```sql
ACRUserStore
```

```sql
<unique id>
```

```sql
<db id>
```

```sql
<user id>
```

```sql
SecCtxtACRUserStore
```

```sql
ACRUserStore
```

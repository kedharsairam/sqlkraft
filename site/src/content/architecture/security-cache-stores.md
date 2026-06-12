---
title: "Security cache stores"
topic: "query-processing"
description: "name. There's one user token per database for a login."
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

## Description

name. There's one user token per database for a login.

Records all permissions for a securable object for a UserToken or SecContextToken.

Key is the class and ID of a securable object. The entry is a series of lists containing

audit IDs for each auditable operation on an object.

permission checks, detailing each auditable operation a specific user has on a

particular object.

entry per query plan.

first thing checked during query execution. To prevent ad hoc queries from flooding

times.

database.

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

-

-

Every user has individual ACR user store.

and 10

different.

ﾉ

`TokenPerm`

`TokenAudit`

`TokenAccessResult`

`ObjectPerm`

`TokenAndPermUserStore`

`SecContextToken`

`LoginToken`

`UserToken`

`TokenPerm`

```sql
TokenAudit
SecCtxtACRUserStore
```

`ACRUserStore`

```sql
<unique id>
```

```sql
<db id>
```

```sql
<user id>
```

`SecCtxtACRUserStore`

`ACRUserStore`

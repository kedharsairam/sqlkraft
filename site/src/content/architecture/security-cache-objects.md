---
title: "Security cache objects"
topic: "query-processing"
description: "7. Verify user permissions on all columns, for example, the permissions of the user on"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

7. Verify user permissions on all columns, for example, the permissions of the user on

and

.

8. Checks user permissions on all tables, such as

and

, and schema

## permissions on

and

.

9. Verifies database permissions.

SQL Server repeats the process for every single role that the user belongs to. Once all

## permissions are obtained, the server performs a check to ensure that the user has all the

necessary grants in the chain and not a single deny in the chain. After the permission check is

complete, the query execution begins.

For more information, review

Summary of the permission check algorithm

.

To simplify validation, SQL Server uses a security cache.

The security cache stores permissions for a user or a login for various securable objects in a

database or server. One of the benefits is that it speeds up query execution. Before SQL Server

executes a query, it checks if the user has the necessary permissions for different database

securables, such as schema-level permissions, table-level permissions, and column permissions.

To make the workflow explained in the previous section faster, SQL Server caches many

different objects inside security caches. Some of the objects that are cached include:

## Description

The server-wide security context for a principal is held within this structure. It

contains a hashtable of user tokens and serves as the starting point or base for all

other caches. Includes references to the login token, user token, audit cache, and

TokenPerm cache. Additionally, it acts as the base token for a login at the server

level.

Similar to the security context token. Contains details of server-level principals. The

login token includes various elements such as SID, login ID, login type, login name,

isDisabled status, and server fixed role membership. Additionally, it encompasses

special roles at the server level, such as sysadmin and security admin.

This structure is related to database-level principals. It includes details such as

username, database roles, SID, default language, default schema, ID, roles, and

ﾉ

Expand table

```sql
t1.Column1
```

```sql
t2.Column1
```

```sql
table1
```

```sql
table2
```

```sql
Schema1
```

```sql
Schema2
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

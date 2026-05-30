---
name: "Use compatibility level for backward compatibility"
title: "Use compatibility level for backward compatibility"
category: "statements"
description: "When a stored procedure executes, it uses the current compatibility level of the database in"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

When a stored procedure executes, it uses the current compatibility level of the database in

which it's defined. When the compatibility setting of a database is changed, all of its stored

procedures are automatically recompiled accordingly.

The

database compatibility level

setting provides backward compatibility with earlier versions

of SQL Server in what relates to Transact-SQL and query optimization behaviors only for the

specified database, not for the entire server.

Starting with compatibility mode 130, any new query plan affecting fixes and features have

been intentionally added only to the new compatibility level. This has been done in order to

minimize the risk during upgrades that arise from performance degradation due to query plan

changes potentially introduced by new query optimization behaviors.

From an application perspective, use the lower compatibility level as a safer migration path to

work around version differences, in the behaviors that are controlled by the relevant

compatibility level setting. The goal should still be to upgrade to the latest compatibility level

at some point in time, in order to inherit some of the new features such as

Intelligent query

processing in SQL databases

, but to do so in a controlled way.

For more information, including the recommended workflow for upgrading database

compatibility level, see

## Best Practices for upgrading database compatibility level

.

functionality introduced in a given SQL Server version is

protected by

compatibility level. This refers to functionality that was removed from the SQL Server

Database Engine. For example, the

hint was discontinued in SQL Server

2012 (11.x) and replaced with the

hint. Setting the database

compatibility level to 110 won't restore the discontinued hint. For more information on

discontinued functionality, see

Discontinued Database Engine functionality in SQL Server

.

introduced in a given SQL Server version

be protected by

compatibility level. This refers to behavior changes between versions of the SQL Server

Database Engine. Transact-SQL behavior is usually protected by compatibility level.

However, changed or removed system objects are

protected by compatibility level.

An example of a breaking change

by compatibility level is an implicit

conversion from

to

data types. Under database compatibility level

130, these show improved accuracy by accounting for the fractional milliseconds,

### not protected

```sql
FASTFIRSTROW
```

```sql
OPTION (FAST n )
```

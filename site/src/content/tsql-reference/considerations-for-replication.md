---
name: 'Considerations for replication'
title: 'Considerations for replication'
category: 'statements'
description: 'Under database compatibility level 110 and higher, any columns in remote tables of type'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Under database compatibility level 110 and higher, any columns in remote tables of type

that are referenced in a partitioned view are mapped as

.

Corresponding columns (in the same ordinal position in the select list) in the local tables

must be

. This is a change in behavior from earlier versions of SQL Server in

which any columns in remote tables of type

that are referenced in a

partitioned view are mapped as

and corresponding columns in local tables must

be of type

. For more information, see

ALTER DATABASE Compatibility Level

(Transact-SQL)

.

Any linked server in the partitioned view cannot be a loopback linked server. This is a

linked server that points to the same instance of SQL Server.

The setting of the

option is ignored for

,

, and

actions that

involve updatable partitioned views and remote tables.

When the member tables and partitioned view definition are in place, the SQL Server query

optimizer builds intelligent plans that use queries efficiently to access data from member

tables. With the

constraint definitions, the query processor maps the distribution of key

values across the member tables. When a user issues a query, the query processor compares

the map to the values specified in the

clause, and builds an execution plan with a

minimal amount of data transfer between member servers. Therefore, if some member tables

are located in remote servers, the instance of SQL Server resolves distributed queries so that

the amount of distributed data that has to be transferred is minimal.

To create partitioned views on member tables that are involved in replication, the following

considerations apply:

If the underlying tables are involved in merge replication or transactional replication with

updating subscriptions, ensure that the

column is also included in the

select list.

Any

actions into the partitioned view must provide a

value for the

column. Any UPDATE actions against the

column must

supply

as the value because the DEFAULT keyword cannot be used.

The replication of updates made by using the view is the same as when tables are

replicated in two different databases: the tables are served by different replication agents

and the order of the updates is not guaranteed.

### Applies to

```sql
SET ROWCOUNT
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
DELETE
```

```sql
CHECK
```

```sql
WHERE
```

```sql
INSERT
```

```sql
NEWID()
```

```sql
NEWID()
```

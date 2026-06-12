---
name: "sys.sp_changedistributor_password"
title: "sp_changedistributor_password"
category: "general"
description: "Changes the password for a Distributor. This stored procedure is executed at the Distributor on any database. If this is a remote Distributor, then it needs to be run on all the Publisher servers that are using this Distributor. If the distribution or Publisher database is in an availability group, then it needs to be run on all the Distributor and Publisher nodes."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_changedistributor_password"
---

## Description

Changes the password for a Distributor. This stored procedure is executed at the Distributor on any database. If this is a remote Distributor, then it needs to be run on all the Publisher servers that are using this Distributor. If the distribution or Publisher database is in an availability group, then it needs to be run on all the Distributor and Publisher nodes. It doesn't matter if the node is primary or secondary.

## Syntax

`sp_changedistributor_password`

## Permissions

SQL Only members of the fixed server role can execute. View and modify replication security settings Secure the Distributor sp_adddistributor (Transact-SQL) Replication stored procedures (Transact-SQL)
## Examples

### Example 1

`distributor_admin`

### Example 2

```sql
0
```

### Example 3

```sql
1
```

### Example 4

`sp_changedistributor_password`

### Example 5

```sql
sp_changedistributor_password [ @password = ]
N
'password'
[ ; ]
```

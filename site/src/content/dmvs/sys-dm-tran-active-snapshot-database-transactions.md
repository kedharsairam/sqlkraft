---
name: "sys.dm_tran_active_snapshot_database_transactions"
title: "sys.dm_tran_active_snapshot_database_transactions"
category: "io"
description: "Unique identification number assigned for the transaction. The transaction ID is primarily used to identify the transaction in locking operations. Transaction sequence number. This is a unique sequence number that is assigned to a transaction when it starts. Transactions that do not generate version records and do not use snapshot scans will not receive a transaction Sequence number that indicates"
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_tran_active_snapshot_database_transactions"
---

## Description

Unique identification number assigned for the transaction. The transaction ID is primarily used to identify the transaction in locking operations. Transaction sequence number. This is a unique sequence number that is assigned to a transaction when it starts. Transactions that do not generate version records and do not use snapshot scans will not receive a transaction Sequence number that indicates when the transaction

## Syntax

```sql
sys.dm_tran_active_snapshot_database_transactions
```

## Examples

### Example 1

```sql
VIEW SERVER STATE
```

### Example 2

```sql
##MS_ServerStateReader##
```

### Example 3

```sql
VIEW DATABASE STATE
```

### Example 4

```sql
##MS_ServerStateReader##
```

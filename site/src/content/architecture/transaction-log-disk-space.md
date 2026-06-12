---
title: "Transaction log disk space"
topic: "filestream"
description: ""
tags: ["filestream","transaction-log-disk-space"]
pubDate: "2025-12-01"
---

Large-scale index operations can generate large data loads that can cause the transaction log

to fill quickly. To make sure that the index operation can be rolled back, the transaction log

can't be truncated until the index operation has completed; however, the log can be backed up

during the index operation. Therefore, the transaction log must have sufficient room to store

both the index operation transactions and any concurrent user transactions for the duration of

the index operation.

This is true for both offline and online index operations. Because the underlying tables can't be

accessed during an offline index operation, there might be few user transactions and the log

might not grow as quickly. Online index operations don't prevent concurrent user activity,

therefore, large-scale online index operations combined with significant concurrent user

transactions can cause continuous growth of the transaction log without an option to truncate

the log.

When you run large-scale index operations, consider the following recommendations:

1. Make sure the transaction log is backed up and truncated before running large-scale

index operations online, and that the log has sufficient space to store the projected index

and user transactions.

2. Consider setting the

option to

for the index operation. This separates

the index transactions from the concurrent user transactions. The index transactions are

stored in the

transaction log, and the concurrent user transactions are stored in

the transaction log of the user database. This allows for the transaction log of the user

database to be truncated during the index operation if necessary. Additionally, if the

log isn't on the same disk as the user database log, the two logs aren't competing

for the same disk space.

７

Note

```sql
SORT_IN_TEMPDB
ON tempdb tempdb
```

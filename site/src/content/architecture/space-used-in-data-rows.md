---
title: "Space used in data rows"
topic: "query-processing"
description: "The online index build version store is used for online index builds."
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

The online index build version store is used for online index builds.

The common version store is used for all other data modification operations.

Row versions must be stored for as long as an active transaction needs to access them.

Periodically, a background thread removes row versions that are no longer needed and frees up

space in the version store. A long-running transaction prevents space in the version store from

being released if it meets any of the following conditions:

It uses row versioning-based isolation.

It uses triggers, MARS, or online index build operations.

It generates row versions.

If the version store is in

, and

runs out of space, the Database Engine forces the

version stores to shrink. During the shrink process, the longest running transactions that haven't

yet generated row versions are marked as victims. A message 3967 is generated in the error log

for each victim transaction. If a transaction is marked as a victim, it can no longer read the row

versions in the version store. When it attempts to read row versions, message 3966 is generated

and the transaction is rolled back. If the shrinking process succeeds, space becomes available in

. Otherwise,

runs out of space and the following occurs:

Write operations continue to execute but don't generate versions. An information message

(3959) appears in the error log, but the transaction that writes data isn't affected.

Transactions that attempt to access row versions that weren't generated because of a

full rollback and terminate with an error 3958.

７

Note

When a trigger is invoked inside a transaction, the row versions created by the trigger are

maintained until the end of the transaction, even though the row versions are no longer

needed after the trigger completes. This also applies to

transactions that use

row versioning. With this type of transaction, a transactionally consistent view of the

database is needed only for each statement in the transaction. This means that the row

versions created for a statement in the transaction are no longer needed after the statement

completes. However, row versions created by each statement in the transaction are

maintained until the transaction completes.

`tempdb`

`tempdb`

`tempdb`

`tempdb`

`tempdb`

```sql
READ COMMITTED
```

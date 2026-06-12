---
title: "and in temporary tables?"
topic: "query-processing"
description: "Is optimized locking enabled?"
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

See

Is optimized locking enabled?

If RCSI is enabled, use the

table hint to force blocking between two queries

when optimized locking is enabled.

No, because DML statements can't run on read-only replicas, and the corresponding row and

page locks aren't taken.

Not at this time.

Transaction locking and row versioning guide

Read committed snapshot isolation (RCSI)

sys.dm_tran_locks (Transact-SQL)

Accelerated database recovery

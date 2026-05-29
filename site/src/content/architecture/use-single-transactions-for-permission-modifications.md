---
title: "Use single transactions for permission modifications"
topic: "io-fundamentals"
description: "Given the high-level invalidation nature of security caches (database/server level), perform"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Given the high-level invalidation nature of security caches (database/server level), perform

security DDLs during nonbusiness hours when the server load is low. If a security cache

invalidation occurs during heavy workloads, there can be a noticeable performance impact on

the entire server as the security caches are repopulated.

Performing multiple security Data Definition Language (DDL) operations within the same

transaction can significantly increase the chance of encountering deadlocks with other active

connections To mitigate this risk, it's recommended to avoid executing multiple security DDLs

in a single transaction. Instead, execute security-related DDL operations in separate

transactions to minimize lock contention.

Get started with Database Engine permissions

Related content

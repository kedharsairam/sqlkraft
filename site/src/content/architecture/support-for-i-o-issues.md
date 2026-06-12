---
title: "Support for I/O issues"
topic: "io-fundamentals"
description: "When you enable write caching without proper safeguards, some storage subsystems"
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

When you enable write caching without proper safeguards, some storage subsystems

acknowledge write operations as complete before data is safely written to durable media. If a

power loss or system failure occurs, this condition can result in:

Data loss, where committed transactions are never persisted.

Database corruption due to broken write-order guarantees.

Microsoft fully supports SQL Server and SQL Server-based applications, but the device

manufacturer is responsible for support when the I/O solution causes problems. Symptoms

include, but aren't limited to:

Database corruption

Backup corruption

Unexpected data loss

Missing transactions

Unexpected I/O performance variances

）

Important

Disable write caching for SQL Server data and log drives unless you confirm through

hardware vendor documentation that:

The cache is battery-backed or uses persistent flash storage.

The drive guarantees durability across power outages and system crashes.

External UPS devices aren't sufficient because they might not protect against all failure

modes, such as a controller firmware fault.

７

Note

Microsoft doesn't certify or validate that third-party hardware or software products work

with SQL Server. Microsoft publishes environmental requirements, including I/O subsystem

and caching system requirements, to support transactional semantics. Third-party vendors

are responsible for verifying that their products meet these requirements. If a problem

occurs in a configuration that includes a third-party product, SQL Server support might ask

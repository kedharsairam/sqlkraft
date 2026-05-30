---
title: "Code guidelines"
topic: "query-processing"
description: "Bound sessions can be used to develop three-tier applications in which business logic is"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Bound sessions can be used to develop three-tier applications in which business logic is

incorporated into separate programs that work cooperatively on a single business transaction.

These programs must be coded to carefully coordinate their access to a database. Because the

two sessions share the same locks, the two programs must not try to modify the same data at the

same time. At any point in time, only one session can be doing work as part of the transaction;

there can be no parallel execution. The transaction can only be switched between sessions at

well-defined yield points, such as when all DML statements have completed and their results

have been retrieved.

It's important to keep transactions as short as possible. When a transaction is started, a database

management system (DBMS) must hold many resources until the end of the transaction to

protect the atomicity, consistency, isolation, and durability (ACID) properties of the transaction. If

data is modified, the modified rows must be protected with exclusive locks that prevent any other

transaction from reading the rows, and exclusive locks must be held until the transaction is

committed or rolled back. Depending on transaction isolation level settings,

statements

might acquire locks that must be held until the transaction is committed or rolled back. Especially

in systems with many users, transactions must be kept as short as possible to reduce locking

contention for resources between concurrent connections. Long-running, inefficient transactions

might not be a problem with small numbers of users, but they're highly problematic in a system

with thousands of users. Beginning with SQL Server 2014 (12.x), the Database Engine supports

delayed durable transactions. Delayed durable transactions might improve scalability and

performance, but they don't guarantee durability. For more information, see

Control Transaction

Durability

.

These are the guidelines for coding efficient transactions:

Don't require input from users during a transaction. Get all required input from users before

a transaction is started. If additional user input is required during a transaction, roll back the

current transaction and restart the transaction after the user input is supplied. Even if users

respond immediately, human reaction times are vastly slower than computer speeds. All

resources held by the transaction are held for an extremely long time, which has the

potential to cause blocking problems. If users don't respond, the transaction remains active,

locking critical resources until they respond, which might not happen for several minutes or

even hours.

```sql
SELECT
```

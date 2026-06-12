---
title: "Transaction basics"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

Azure

Synapse Analytics

Analytics Platform System (PDW)

In any database, mismanagement of transactions often leads to contention and performance

problems in systems that have many users. As the number of users that access the data increases,

it becomes important to have applications that use transactions efficiently. This guide describes

locking and row versioning mechanisms the Database Engine uses to ensure the integrity of each

transaction and provides information on how applications can control transactions efficiently.

７

Note

is a Database Engine feature introduced in 2023 that drastically reduces

lock memory, and the number of locks required for concurrent writes. This article is updated

to describe the Database Engine behavior with and without optimized locking.

For more information and to learn where optimized locking is available, see.

To determine if optimized locking is enabled on your database, see

Optimized locking introduces significant changes to some sections of this article, including:

### Atomicity

### Consistency

### Isolation

### Durability

A transaction is a sequence of operations performed as a single logical unit of work. A logical unit

of work must exhibit four properties, called the atomicity, consistency, isolation, and durability

(ACID) properties, to qualify as a transaction.

A transaction must be an atomic unit of work; either all of its data modifications are performed,

or none of them are performed.

When completed, a transaction must leave all data in a consistent state. In a relational database,

all rules must be applied to the transaction's modifications to maintain all data integrity. All

internal data structures, such as B-tree indexes or doubly linked lists, must be correct at the end

of the transaction.

Modifications made by concurrent transactions must be isolated from the modifications made by

any other concurrent transactions. A transaction either recognizes data in the state it was in

before another concurrent transaction modified it, or it recognizes the data after the second

transaction has completed, but it doesn't recognize an intermediate state. This is referred to as

serializability because it results in the ability to reload the starting data and replay a series of

transactions to end up with the data in the same state it was in after the original transactions

were performed.

After a fully durable transaction has completed, its effects are permanently in place in the system.

The modifications persist even in the event of a system failure. SQL Server 2014 (12.x) and later

enable delayed durable transactions. Delayed durable transactions commit before the transaction

log record is persisted to disk. For more information on delayed transaction durability, see the

Control Transaction Durability.

Applications are responsible for starting and ending transactions at points that enforce the

logical consistency of the data. The application must define the sequence of data modifications

７

Note

Documentation uses the term B-tree generally in reference to indexes. In rowstore indexes,

the Database Engine implements a B+ tree. This does not apply to columnstore indexes or

indexes on memory-optimized tables. For more information, see the

and Azure

SQL index architecture and design guide.

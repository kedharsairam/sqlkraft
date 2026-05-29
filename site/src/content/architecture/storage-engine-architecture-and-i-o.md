---
title: 'Storage engine architecture and I/O'
topic: 'io-fundamentals'
description: 'SQL Server internals and architecture'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

SQL Server internals and architecture

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

The following guides are available. They discuss general concepts and apply to all versions of

SQL Server, unless stated otherwise in the respective guide.

Concurrency, locking, and contention

Storage engine architecture and I/O

Query execution and optimization

Memory, threads, and internal scheduling

High availability, migration, and validation

Connectivity and authentication

Use these guides to understand how SQL Server manages concurrent access to data and

internal structures, and how to diagnose contention-related issues.


## Description
Transaction locking and row

versioning guide

Explains the locking and row versioning mechanisms that SQL Server uses

to preserve transaction integrity. Describes how applications can

efficiently control transactions.

Deadlocks guide

Deep dive on Database Engine deadlocks that competing locks cause.

Explains how deadlocks form and how SQL Server detects and breaks

them.

Diagnose and resolve latch

contention on SQL Server

Focuses on identifying and resolving latch contention (notably page latch

contention) in high-concurrency SQL Server workloads.

Diagnose and resolve

spinlock contention on SQL

Server

In-depth guide on identifying and resolving spinlock contention in high-

concurrency SQL Server workloads.

ﾉ

Expand table

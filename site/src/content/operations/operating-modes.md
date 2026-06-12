---
title: "Operating Modes"
topic: "high-availability"
description: "This topic describes the synchronous and asynchronous operating modes for database mirroring sessions. This section introduces a few terms that are c"
tags: ["high-availability","operating-modes"]
pubDate: "2025-12-01"
---

This topic describes the synchronous and asynchronous operating modes for database

mirroring sessions.

This section introduces a few terms that are central to this topic.

High-performance mode

The database mirroring session operates asynchronously and uses only the principal server and

mirror server. The only form of role switching is forced service (with possible data loss).

High-safety mode

The database mirroring session operates synchronously and, optionally, uses a witness, as well

as the principal server and mirror server.

Transaction safety

A mirroring-specific database property that determines whether a database mirroring session

operates synchronously or asynchronously. There are two safety levels: FULL and OFF.

Witness

For use only with high-safety mode, an optional instance of SQL Server that enables the mirror

server to recognize whether to initiate an automatic failover. Unlike the two failover partners,

the witness does not serve the database. Supporting automatic failover is the only role of the

witness.

This section describes how asynchronous database mirroring works, when it is appropriate to

use high-performance mode, and how to respond if the principal server fails.

７

Note

For an introduction to database mirroring, see.

---
title: "Closing packets"
topic: "query-processing"
description: "This article presents examples of a network trace that captures the sequence during when a"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Article

•

06/06/2024

This article presents examples of a network trace that captures the sequence during when a

Transmission Control Protocol (TCP) connection between a client application and the SQL

Server Database Engine (the server) is closed. Understanding these patterns is crucial for

diagnosing network behavior, identifying pooling strategies, and optimizing connection

management in web or service applications.

This article provides examples for normal TCP connections, and Multiple Active Result Sets

(MARS) connections. MARS is a feature of SQL Server, introduced with SQL Server 2005 (9.x),

that allows multiple commands to be executed on a connection without having to clean up the

results from the first command, before running the second command. MARS is achieved

through session multiplexing (SMUX).

This section describes several examples of closing a network connection.

The client IP address is

The server IP address is

This example shows a normal connection close sequence. Note the low frame numbers

and time offsets. This sequence is most likely a pooled connection closure. This should

occur within 30 seconds of the beginning of the trace, or you might also see keep-alive

packets.

Normal connections

```sql
10.10.10.104
```

```sql
10.10.10.22
```

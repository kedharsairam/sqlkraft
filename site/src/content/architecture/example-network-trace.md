---
title: "Example network trace"
topic: "query-processing"
description: "This article presents several examples of a network trace that captures various handshakes and"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

09/07/2025

This article presents several examples of a network trace that captures various handshakes and

authentication sequences during the Transmission Control Protocol (TCP) connection

establishment process between a client application and the SQL Server Database Engine (the

server).

For information about closing connections, see

Trace the network connection close sequence

on the Database Engine

.

You can connect to the Database Engine with

authentication (using

or

authentication), or

SQL

authentication.

This article also describes Multiple Active Result Sets (MARS) connections. MARS is a feature of

SQL Server, introduced with SQL Server 2005 (9.x), that allows multiple commands to be

executed on a connection without having to clean up the results from the first command,

before running the second command. MARS is achieved through session multiplexing (SMUX).

This process describes a normal login process using SQL authentication, showing each

step of the conversation between the client and server through a detailed network trace

analysis. The example network trace delineates the following steps:

1. TCP three-way handshake

2. Driver handshake

3. SSL/TLS handshake

4. Login packet exchange

5. Login confirmation

6. Execute a command and read the response

7. TCP four-way closing handshake

This exchange is allocated 1 second regardless of the

setting in the

connection string.

SQL authentication

```sql
Login Timeout
```

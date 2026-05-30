---
title: "Context vs. regular connections"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  If you're connecting to a remote server, always use regular connections rather than context

  connections. If you need to connect to the same server on
tags:
  - "clr-integration"
  - "context-vs-regular-connections"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

If you're connecting to a remote server, always use regular connections rather than context

connections. If you need to connect to the same server on which the stored procedure or

function is running, use the context connection in most cases. This method has benefits such as

running in the same transaction space, and not having to reauthenticate.

Additionally, using the context connection typically results in better performance and less

resource usage. The context connection is an in-process-only connection, so it can contact the

server

directly

by bypassing the network protocol and transport layers to send Transact-SQL

statements and receive results. The authentication process is bypassed, as well. The following

figure shows the primary components of the

managed provider, and how the

different components interact with each other when using a regular connection versus the

context connection.

The context connection follows a shorter code path and involves fewer components, so you

can expect requests and results to get to and from the server faster than in a regular

connection. Query execution time on the server is the same for context and regular

connections.

`SqlClient`

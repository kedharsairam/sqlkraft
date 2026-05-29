---
title: "Integration & transactions"
topic: "clr-integration"
description: |
  Article
  
  •
  
  12/30/2024
  
  Applies to:
  
  SQL Server
  
  The
  
  namespace provides a transaction framework that is fully integrated
  
  with ADO.NET and SQL Server common language runtime (CLR) integration.
  
  and A
tags:
  - "clr-integration"
  - "integration-transactions"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

The

namespace provides a transaction framework that is fully integrated

with ADO.NET and SQL Server common language runtime (CLR) integration.

and ADO.NET work together to extend and simplify the use of local and

distributed transactions in managed applications.

For more information about transactions and the .NET Framework, see

Transaction Processing

.

Description

Transaction promotion

Describes the ability to promote transactions, and how to use this feature.

Access the current

transaction

Describes how to access a transaction currently running in-process on SQL

Server.

Use System.Transactions

Describes how to use the

application programming

interface (API) in your managed application.

Transaction lifetimes

Describes the difference in lifetime between transactions started in Transact-

SQL stored procedures and transactions started in CLR applications.

Data access from CLR database objects

７

Note

A CLR user-defined procedure (UDP) can't establish a connection to the same server it's

running on (a loopback connection) and enlist in the same transaction. If this is attempted,

the connection attempt will be blocked and control will not be passed back to the UDP.

This will result in a timeout error (Msg 1206) on the UDP.

ﾉ

Expand table

```sql
System.Transactions
System.Transactions
System.Transactions
```
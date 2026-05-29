---
title: "Context Connection"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  The problem of internal data access is a fairly common scenario. That is, you wish to access the

  same server on which your common language runtime (CL
tags:
  - "clr-integration"
  - "context-connection"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

The problem of internal data access is a fairly common scenario. That is, you wish to access the

same server on which your common language runtime (CLR) stored procedure or function is

executing. One option is to create a connection using

,

specify a connection string that points to the local server, and open the connection. This

method requires specifying credentials for logging in. The connection is in a different database

session than the stored procedure or function, it might have different

options, it's in a

separate transaction, it doesn't see your temporary tables, and so on.

If your managed stored procedure or function code is executing in the SQL Server process, it's

because someone connected to that server and executed a SQL statement to invoke it. You

probably want the stored procedure or function to execute in the context of that connection,

along with its transaction,

options, and so on. This is called the context connection.

The context connection lets you execute Transact-SQL statements in the same context that

your code was invoked in the first place. In order to obtain the context connection, you must

use the "context connection" connection string keyword, as in the following example.

Description

Context connections vs. regular connections

Describes the differences between regular and context

connections.

Restrictions on context connections and regular

connections

Describes the restrictions on regular and context

connections.

C#

ﾉ

Expand table

```sql
System.Data.SqlClient.SqlConnection
SET
SET
using(SqlConnection connection = new SqlConnection("context connection=true"))
{
connection.Open();
// Use the connection
}
```

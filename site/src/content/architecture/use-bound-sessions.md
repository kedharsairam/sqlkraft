---
title: "Use bound sessions"
topic: "io-fundamentals"
description: "Bound sessions ease the coordination of actions across multiple sessions on the same server."
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Bound sessions ease the coordination of actions across multiple sessions on the same server.

Bound sessions allow two or more sessions to share the same transaction and locks, and can

work on the same data without lock conflicts. Bound sessions can be created from multiple

sessions within the same application or from multiple applications with separate sessions.

To participate in a bound session, a session calls

sp_getbindtoken

or

srv_getbindtoken

(through

Open Data Services) to get a bind token. A bind token is a character string that uniquely identifies

each bound transaction. The bind token is then sent to the other sessions to be bound with the

current session. The other sessions bind to the transaction by calling

, using the

bind token received from the first session.

Bind tokens must be transmitted from the application code that makes the first session to the

application code that subsequently binds their sessions to the first session. There's no Transact-

SQL statement or API function that an application can use to get the bind token for a transaction

started by another process. Some of the methods that can be used to transmit a bind token

include the following:

If the sessions are all initiated from the same application process, bind tokens can be stored

in global memory or passed into functions as a parameter.

If the sessions are made from separate application processes, bind tokens can be

transmitted using interprocess communication (IPC), such as a remote procedure call (RPC)

or dynamic data exchange (DDE).

Bind tokens can be stored in a table in an instance of the Database Engine that can be read

by processes wanting to bind to the first session.

The Database Engine doesn't support independently manageable nested transactions. A

commit of an inner transaction decrements

but has no other effects. A rollback

of an inner transaction always rolls back the outer transaction, unless a

exists and

is specified in the

statement.

７

Note

A session must have an active user transaction in order for

or

to succeed.

### Local bound session

### Distributed bound session

```sql
sp_bindsession
```

```sql
@@TRANCOUNT
```

```sql
ROLLBACK
```

```sql
sp_getbindtoken
```

```sql
srv_getbindtoken
```

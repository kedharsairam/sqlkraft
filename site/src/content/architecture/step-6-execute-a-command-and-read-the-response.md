---
title: "Step 6. Execute a command and read the response"
topic: "query-processing"
description: ""
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

Otherwise, you see a response packet, which either confirms the login (has the login

token), or returns a

error message to the client.

Here's an example of what you might see in the packet hexadecimal data for a successful

login:

Output

Commands are sent as either a

or a

packet. The former

executes plain Transact-SQL statements, and the latter executes stored procedures. You

might see TCP continuation packets if the command is lengthy, or in the Response packet

if more than a few rows are returned.

Output

`ACK`

```sql
Login Failed
```

```sql.C.h.a.n.g.e.d.d.a.t.a.b.a.s.e.c.o.n.t.e.x.t.t.o.'.A.d.v.e.n.t.u.r.e.W.o.r.ks'
```

```sql
TDS:SQLBatch
```

```sql
TDS:RPCRequest
```

```sql
6136 116.5932948 10.10.10.10 10.10.10.120 TLS:TLS Rec Layer-1 SSL
Application Data {TLS:328, SSLVersionSelector:327, TDS:326, TCP:325, IPv4:3
```

```sql
Frame Time Offset Source IP Dest IP Description
----- ----------- ------------ ------------ ----------------------------------
-----------------------------------------------------------------
6137 116.5962248 10.10.10.120 10.10.10.10 TDS:Response, Version = 7.1 (0x71000001), SPID = 96, PacketID = 1, Flags=.AP., SrcPort=1433, Ds
```

```sql
Frame Time Offset Source IP Dest IP Description
----- ----------- ------------ ------------ ----------------------------------
-----------------------------------------------------------------
6138 116.5991538 10.10.10.10 10.10.10.120 TDS:SQLBatch, Version = 7.1 (0x71000001), SPID = 0, PacketID = 1, Flags=.AP., SrcPort=60123, Ds
6139 116.5991538 10.10.10.120 10.10.10.10 TDS:Response, Version = 7.1
```

---
title: "Transact-SQL statements and closing packets"
topic: "query-processing"
description: "This example shows closing a nonpooled connection, after two Transact-SQL statements. If"
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

Output

This example shows closing a nonpooled connection, after two Transact-SQL statements. If

this connection was nonpooled, you could also see keep-alive packets associated with

sending the connection back into the connection pool, instead of the closing packets

immediately following the last response from the server. We recommend pooling

connections in any sort of web or service application to allow connection reuse.

Connection pooling reduces the number of connections to the server, and minimizes the

cost and delay associate with new connections.

Output

```sql
Frame Offset Source IP Dest IP Description
----- --------- ------------ ------------ ------------------------------------
---------------------------------------
50 4.1529661 10.10.10.104 10.10.10.22 TCP:Flags=.A.F, SrcPort=4657,
DstPort=1433, PayloadLen=0, Seq=413460761
51 4.1529661 10.10.10.22 10.10.10.104 TCP:Flags=.A., SrcPort=1433,
DstPort=4657, PayloadLen=0, Seq=280398321
52 4.1529661 10.10.10.22 10.10.10.104 TCP:Flags=.A.F, SrcPort=1433,
DstPort=4657, PayloadLen=0, Seq=280398321
54 4.2330441 10.10.10.104 10.10.10.22 TCP:Flags=.A., SrcPort=4657,
DstPort=1433, PayloadLen=0, Seq=413460761
```

```sql
Frame Offset Source IP Dest IP Description
----- --------- ------------ ------------ ------------------------------------
---------------------------------------
364 9.1949581 10.10.10.104 10.10.10.22 TDS:SQLBatch, Version = 7.300000,
SPID = 0, PacketID = 1, Flags=.AP., S
365 9.1949581 10.10.10.22 10.10.10.104 TDS:Response, Version = 7.300000,
SPID = 130, PacketID = 1, Flags=.AP.,
366 9.3043331 10.10.10.104 10.10.10.22 TDS:SQLBatch, Version = 7.300000,
SPID = 0, PacketID = 1, Flags=.AP., S
```

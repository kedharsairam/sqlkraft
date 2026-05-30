---
title: "Idle or pooled connection being closed"
topic: "io-fundamentals"
description: "The connection is closed 10 seconds after the previous keep-alive exchange (see"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

The connection is closed 10 seconds after the previous keep-alive exchange (see

column).

Output

７

Note

The parser mistakenly marks the initial

packet (Frame 1881) as a keep-alive

packet, because the previous keep-alive packet. However, it is initializing the

connection closure.

Related content

Enabling Multiple Active Result Sets

Using MARS in ADO.NET

Using MARS in OLE DB

Trace the network authentication process to the Database Engine

```sql
Delta
```

```sql
367 9.3072631  10.10.10.22 10.10.10.104 TDS:Response, Version = 7.300000,
SPID = 130, PacketID = 1, Flags=...AP...,
375 9.4078491 10.10.10.104  10.10.10.22 TCP:Flags=...A...F, SrcPort=4647,
DstPort=1433, PayloadLen=0, Seq=157672648
376 9.4078491  10.10.10.22 10.10.10.104 TCP:Flags=...A...., SrcPort=1433,
DstPort=4647, PayloadLen=0, Seq=192890973
379 9.4078491  10.10.10.22 10.10.10.104 TCP:Flags=...A...F, SrcPort=1433,
DstPort=4647, PayloadLen=0, Seq=192890973
397 9.5221071 10.10.10.104  10.10.10.22 TCP:Flags=...A...., SrcPort=4647,
DstPort=1433, PayloadLen=0, Seq=157672649
```

```sql
ACK+FIN
```

```sql
ACK
```

```sql
Frame Offset     Delta      Source IP   Dest IP     Description
----- ---------- ---------- ----------- ----------- --------------------------
---------------------------------------
1314 16.3641802  0.0000000 10.10.10.45 10.10.10.51 TCP:[Keep
alive]Flags=...A...., SrcPort=51708, DstPort=1433, Payl
1317 16.3677083  0.0035281 10.10.10.51 10.10.10.45 TCP:[Keep alive
ack]Flags=...A...., SrcPort=1433, DstPort=51708,
1327 16.4269375  0.0592292 10.10.10.51 10.10.10.45 TCP:[Keep
alive]Flags=...A...., SrcPort=1433, DstPort=51708, Payl
1328 16.4269637  0.0000262 10.10.10.45 10.10.10.51 TCP:[Keep alive
ack]Flags=...A...., SrcPort=51708, DstPort=1433,
1881 26.7918499 10.3648862 10.10.10.45 10.10.10.51 TCP:[Keep alive
ack]Flags=...A...F, SrcPort=51708, DstPort=1433,
1886 26.7929474  0.0010975 10.10.10.51 10.10.10.45 TCP:Flags=...A....,
SrcPort=1433, DstPort=51708, PayloadLen=0, Se
1888 26.7929474  0.0000000 10.10.10.51 10.10.10.45 TCP:Flags=...A...F,
SrcPort=1433, DstPort=51708, PayloadLen=0, Se
1890 26.7929947  0.0000473 10.10.10.45 10.10.10.51 TCP:Flags=...A....,
SrcPort=51708, DstPort=1433, PayloadLen=0, Se
```

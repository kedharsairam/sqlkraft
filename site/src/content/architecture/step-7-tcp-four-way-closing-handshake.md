---
title: "Step 7. TCP four-way closing handshake"
topic: "query-processing"
description: "Microsoft drivers use the four-way handshake to close connections. Many third-party"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Microsoft drivers use the four-way handshake to close connections. Many third-party

drivers just reset the connection to close it, making it more difficult to distinguish between

a normal and abnormal close.

The four-way handshake consists of the client sending a

packet to the server, which

the server responds to with an

. The server then sends its own

packet, which the

client acknowledges (

).

If the server sends a

packet first, it's an abnormal closing, most commonly seen in the

SSL/TLS handshake if the client and server can't negotiate the secure channel.

Output

Related content

Trace the network connection close sequence on the Database Engine

Connect to the Database Engine

Configure SQL Server to listen on a specific TCP port

```sql
FIN
```

```sql
ACK
```

```sql
FIN
```

```sql
ACK
```

```sql
FIN
```

```sql
(0x71000001), SPID = 96, PacketID = 1, Flags=...AP..., SrcPort=1433, Ds
6266  116.8032558 10.10.10.10  10.10.10.120 TCP:Flags=...A...., SrcPort=60123,
DstPort=1433, PayloadLen=0, Seq=4050702956, Ack=4095168204, Win=
```

```sql
Frame Time Offset Source IP    Dest IP      Description
----- ----------- ------------ ------------ ----------------------------------
-----------------------------------------------------------------
6362  116.9097008 10.10.10.10  10.10.10.120 TCP:Flags=...A...F, SrcPort=60123,
DstPort=1433, PayloadLen=0, Seq=4050702956, Ack=4095168204, Win=
6363  116.9097008 10.10.10.120 10.10.10.10  TCP:Flags=...A...., SrcPort=1433,
DstPort=60123, PayloadLen=0, Seq=4095168204, Ack=4050702957, Win=
6364  116.9097008 10.10.10.120 10.10.10.10  TCP:Flags=...A...F, SrcPort=1433,
DstPort=60123, PayloadLen=0, Seq=4095168204, Ack=4050702957, Win=
6366  116.9106778 10.10.10.10  10.10.10.120 TCP:Flags=...A...., SrcPort=60123,
DstPort=1433, PayloadLen=0, Seq=4050702957, Ack=4095168205, Win=
```

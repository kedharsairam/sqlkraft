---
title: "Step 1. TCP three-way handshake"
topic: "query-processing"
description: ""
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

The client IP address is

The server IP address is

All TCP conversations start with a

packet (

flag set) sent from the client to the server.

In Frame

, the client uses an ephemeral port (dynamically assigned by the operating

system) and connects to the server port, in this case port. The server replies with its

own

packet with the

flag also set. Finally, the client responds with an

packet

to let the server know it received its

packet.

This step establishes a basic TCP connection, the same way a

command would. The

operating system mediates this part of the conversation. At this point, the client and server

know nothing about each other.

Output

In this step, the

warnings are benign and are an indicator that

checksum

offload

is enabled. That is, they're added at a lower level in the network stack than the

trace is taken. In the absence of other information, this warning indicates whether the

network trace was taken on the client or the server. In this case, it appears on the initial

packet, so the trace was taken on the client.

```sql
10.10.10.10
```

```sql
10.10.10.120
```

`SYN`

```sql
S
```

```sql
6127
```

```sql
1433
```

`SYN`

`ACK`

`ACK`

`SYN`

`telnet`

```sql
[Bad CheckSum]
```

`SYN`

```sql
Frame Time Offset Source IP Dest IP Description
----- ----------- ------------ ------------ ----------------------------------
-----------------------------------------------------------------
6127 116.5776698 10.10.10.10 10.10.10.120 TCP:Flags=.S., SrcPort=60123,
DstPort=1433, PayloadLen=0, Seq=4050702293, Ack=0, Win=8192 ( Ne
6128 116.5776698 10.10.10.120 10.10.10.10 TCP:Flags=.A.S., SrcPort=1433,
DstPort=60123, PayloadLen=0, Seq=4095166896, Ack=4050702294, Win=
6129 116.5786458 10.10.10.10 10.10.10.120 TCP:Flags=.A., SrcPort=60123,
DstPort=1433, PayloadLen=0, Seq=4050702294, Ack=4095166897, Win=
```

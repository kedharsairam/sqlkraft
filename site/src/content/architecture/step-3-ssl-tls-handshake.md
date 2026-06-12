---
title: "Step 3. SSL/TLS handshake"
topic: "query-processing"
description: "Both the client driver and SQL Server need to know a bit about each other."
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

Both the client driver and SQL Server need to know a bit about each other. In this

handshake, the driver sends some information and requirements to the server. This

information includes whether to encrypt data packets, whether to use Multiple Active

Result Sets (MARS), its version number, whether to use federated authentication, the

connection GUID, and so on.

The server responds with its information, such as whether it requires authentication. This

sequence happens before any sort of security negotiation is performed.

Output

The SSL/TLS handshake begins with the Client Hello packet and then the Server Hello

packet, plus some extra packets related to Secure Channel. This step is where the security

key is negotiated for encrypting packets. Normally, just the login packet is encrypted, but

the client or the server could require data packets to be encrypted as well. Choosing the

version of TLS happens at this stage of the login. The client or server can close the

connection at this stage if the TLS versions don't line up, or they don't have any cipher

suites in common.

```sql
Frame Time Offset Source IP Dest IP Description
----- ----------- ------------ ------------ ----------------------------------
-----------------------------------------------------------------
6130 116.5786458 10.10.10.10 10.10.10.120 TDS:Prelogin, Version = 7.1 (0x71000001), SPID = 0, PacketID = 0, Flags=.AP., SrcPort=60123, Ds
6131 116.5805998 10.10.10.120 10.10.10.10 TDS:Response, Version = 7.1 (0x71000001), SPID = 0, PacketID = 1, Flags=.AP., SrcPort=1433, Dst
```

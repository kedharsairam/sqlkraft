---
title: "Step 7. TCP four-way closing handshake"
topic: "query-processing"
description: "Microsoft drivers use the four-way handshake to close connections. Many third-party"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

Microsoft drivers use the four-way handshake to close connections. Many third-party

drivers just reset the connection to close it, making it more difficult to distinguish between

a normal and abnormal close.

The four-way handshake consists of the client sending a

packet to the server, which

the server responds to with an. The server then sends its own

packet, which the

client acknowledges (

).

If the server sends a

packet first, it's an abnormal closing, most commonly seen in the

SSL/TLS handshake if the client and server can't negotiate the secure channel.

Output

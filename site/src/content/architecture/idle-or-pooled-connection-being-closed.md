---
title: "Idle or pooled connection being closed"
topic: "io-fundamentals"
description: "The connection is closed 10 seconds after the previous keep-alive exchange (see"
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
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

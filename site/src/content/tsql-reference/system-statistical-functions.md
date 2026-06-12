---
name: "System Statistical Functions"
title: "System Statistical Functions"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

The following scalar functions return statistical information about the system:

@@CONNECTIONS

@@PACK_RECEIVED

@@CPU_BUSY

@@PACK_SENT fn_virtualfilestats

@@TIMETICKS

@@IDLE

@@TOTAL_ERRORS

@@IO_BUSY

@@TOTAL_READ

@@PACKET_ERRORS

@@TOTAL_WRITE

All system statistical functions are nondeterministic. This means these functions do not always return the same results every time they are called, even with the same set of input values. For more information about function determinism, see

Deterministic and Nondeterministic

Functions.

Built-in Functions (Transact-SQL)

See Also

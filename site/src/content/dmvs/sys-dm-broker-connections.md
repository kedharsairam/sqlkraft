---
name: "sys.dm_broker_connections"
title: "sys.dm_broker_connections"
category: "io"
description: "Returns a row for each Service Broker network connection. The following table provides more Identifier of the SQL Server Network Interface (SNI) connection used by this connection for TCP/IP communications."
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: |
  NEW
  CONNECTING
  CONNECTED
  LOGGED_IN
  CLOSED
  connect_time
---

## Description

Returns a row for each Service Broker network connection. The following table provides more Identifier of the SQL Server Network Interface (SNI) connection used by this connection for TCP/IP communications. Current state of the connection. Possible Current state of the connection. Possible Date and time at which the connection was Date and time at which login for the Name of the Windows Authentication

## Syntax

```sql
NEW
CONNECTING
CONNECTED
LOGGED_IN
CLOSED connect_time
```

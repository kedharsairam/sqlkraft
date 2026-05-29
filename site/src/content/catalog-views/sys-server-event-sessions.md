---
name: 'sys.server_event_sessions'
title: 'sys.server_event_sessions'
category: 'objects'
description: 'Value determines whether or not session is started'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
Value determines whether or not session is started

automatically when the server starts. The default is

. Not

nullable. Can be one of:

(

). The session doesn't start when the server starts.

(

). The event session starts when the server starts.

: SQL Server 2025 (17.x) Preview and later versions.

The value that determines the maximum duration of an event

session once it's started, in seconds. Set to

when

is not specified or is set to

. For more

information, see

Time-bound event sessions

.

SQL Server 2019 (15.x) and previous versions require

permission on the

server.

SQL Server 2022 (16.x) and later versions require

permission on

the server.

System catalog views (Transact-SQL)

Extended Events Catalog Views (Transact-SQL)

Extended Events overview

Related content

```sql
startup_state
```

```sql
0
```

```sql
0
```

```sql
OFF
```

```sql
1
```

```sql
ON
```

```sql
max_duration
```

```sql
0
```

```sql
MAX_DURATION
```

```sql
UNLIMITED
```

```sql
VIEW SERVER STATE
```

```sql
VIEW SERVER PERFORMANCE STATE
```

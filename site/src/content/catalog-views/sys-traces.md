---
name: 'sys.traces'
title: 'sys.traces'
category: 'objects'
description: 'Size of each buffer (KB).'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
Size of each buffer (KB).

Last trace file position. This value is null when the trace is a

rowset trace.

Rowset trace reader session ID. This value is null when the trace is

a file trace.

Trace start time.

Time the last event fired.

Total number of events that occurred.

Total number of events dropped.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Requires ALTER TRACE permission on the server.

Object Catalog Views (Transact-SQL)

sys.trace_categories (Transact-SQL)

sys.trace_columns (Transact-SQL)

sys.trace_events (Transact-SQL)

sys.trace_event_bindings (Transact-SQL)

sys.trace_subclass_values (Transact-SQL)

Last updated on 03/25/2026

Related content

```sql
buffer_size
```

```sql
file_position
```

```sql
reader_spid
```

```sql
start_time
```

```sql
last_event_time
```

```sql
event_count
```

```sql
dropped_event_count
```

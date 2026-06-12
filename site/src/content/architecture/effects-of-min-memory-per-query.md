---
title: "Effects of min memory per query"
topic: "query-processing"
description: "### Server configuration: min memory"
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

## Server configuration: min memory

## per query

and

options are specified in megabytes. For

more information including recommendations on how to set these memory configurations, see

Server memory configuration options.

The following list describes the approximate amount of memory used by different objects in. The amounts listed are estimates and can vary depending on the environment and

how objects are created:

Lock (as maintained by the Lock Manager): 64 bytes + 32 bytes per owner

User connection: Approximately (3 \*

network_packet_size

- 94 KB)

The

network packet size

is the size of the tabular data stream (TDS) packets that are used to

communicate between applications and the Database Engine. The default packet size is 4 KB,

and is controlled by the network packet size configuration option.

When multiple active result sets (MARS) are enabled, the user connection is approximately (3 +

3 \*

num_logical_connections

) \* network_packet_size + 94 KB.

The

configuration option establishes the minimum amount of memory

(in kilobytes) that will be allocated for the execution of a query. This is also known as the

minimum memory grant. All queries must wait until the minimum memory requested can be

secured, before execution can start, or until the value specified in the query wait server

configuration option is exceeded. The wait type that is accumulated in this scenario is.

）

Important

Don't set the

server configuration option too high, especially on

very busy systems, because doing so could lead to:

Increased competition for memory resources.

Decreased concurrency by increasing the amount of memory for every single query,

even if the required memory at runtime is lower that this configuration.

For recommendations on using this configuration, see.

```sql
min server memory (MB)
```

```sql
max server memory (MB)
```

```sql
min memory per query
```

`RESOURCE_SEMAPHORE`

```sql
min memory per query
```

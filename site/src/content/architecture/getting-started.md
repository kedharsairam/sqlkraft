---
title: "Getting started"
topic: "tables"
description: "2016 (13.x) and later versions Azure SQL Managed Instance Depending on your scenario, you can either create new system-"
tags: ["tables","getting-started"]
pubDate: "2025-12-01"
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

Depending on your scenario, you can either create new system-versioned temporal tables, or

modify existing ones by adding temporal attributes to the existing table schema. When the

data in temporal table is modified, the system builds version history transparently to

applications and end users. As a result, working with temporal tables doesn't require any

change to the way table is modified or how the latest (current) state of the data is queried.

In addition to regular data modification and querying, temporal tables also provide convenient

and easy ways to get insights from data history through extended Transact-SQL syntax. Every

system-versioned table has a history table assigned, which is transparent to users. However,

you can optimize workload performance, or the storage footprint, by creating more indexes or

choosing different storage options.

The following diagram depicts typical workflow with temporal tables:

This section is divided into the following five articles:

Create a system-versioned temporal table

Modify data in a system-versioned temporal table

Query data in a system-versioned temporal table

Change the schema of a system-versioned temporal table

Stop system-versioning on a system-versioned temporal table

Temporal tables

Temporal table system consistency checks

Partition with temporal tables

Temporal table considerations and limitations

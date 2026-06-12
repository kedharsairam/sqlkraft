---
title: "Usage scenarios"
topic: "tables"
description: ""
tags: ["tables","usage-scenarios"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

System-versioned temporal tables are useful in scenarios that require tracking history of data

changes. We recommend that you consider temporal tables in the following use cases, for

major productivity benefits.

You can use temporal system-versioning on tables that store critical information, to keep track

of what changed and when, and to perform data forensics at any point in time.

Temporal tables allow you to plan for data audit scenarios in the early stages of the

development cycle, or to add data auditing to existing applications or solutions when you need

it.

The following diagram shows an

table with the data sample including current

(marked with a blue color) and historical row versions (marked with a gray color).

The right-hand portion of the diagram visualizes row versions on a time axis, and the rows you

select with different types of querying on temporal table, with or without the

clause.

If you identify information that needs data auditing, create database tables as system-

versioned temporal tables. The following example illustrates a scenario with a table called



```sql
Employee
SYSTEM_TIME
```

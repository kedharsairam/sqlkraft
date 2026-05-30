---
name: "Validation statements"
title: "Validation statements"
category: "statements"
description: "1000 database pages that"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Description

1000 database pages that

are checked.

Database repairs are performed during this phase if

,

, or

is specified, and there are system table errors that must

be repaired.

Progress reported at the

individual repair level.

The counter is updated for

each repair that is

completed.

SQL Server Service Broker objects are checked during this

phase.

Note:

This phase isn't executed when

is

executed.

Progress isn't reported.

The consistency of database catalogs is checked during

this phase.

Note: This phase isn't executed when

is

executed.

Progress isn't reported.

The logical consistency of any indexed views present in

the database is checked during this phase.

Progress reported at the

level of the individual

database view that is being

checked.

DBCC INPUTBUFFER

DBCC SHOWCONTIG

DBCC OPENTRAN

DBCC OUTPUTBUFFER

DBCC PROCCACHE

DBCC SHOW_STATISTICS

DBCC SQLPERF

DBCC TRACESTATUS

DBCC USEROPTIONS

DBCC CHECKALLOC

### Applies to

```sql
DBCC SYS
REPAIR
```

`REPAIR_FAST`

`REPAIR_REBUILD`

`REPAIR_ALLOW_DATA_LOSS`

```sql
DBCC SSB
CHECK
```

```sql
DBCC CHECKTABLE
```

```sql
DBCC
CHECKCATALOG
```

```sql
DBCC CHECKTABLE
```

```sql
DBCC IVIEW
CHECK
```

---
title: "Trace flag 1204 and trace flag 1222"
topic: "query-processing"
description: ""
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

### Deadlock extended event

When deadlocks occur and trace flag 1204 or trace flag 1222 is enabled, deadlock details are

reported in the SQL Server error log. Trace flag 1204 reports deadlock information formatted

by each node involved in the deadlock. Trace flag 1222 formats deadlock information, first by

processes and then by resources. It's possible to enable both trace flags to obtain two

representations of the same deadlock event.

In addition to defining the properties of trace flags 1204 and 1222, the following table also

shows the similarities and differences.

Output

format

Output is captured in the SQL Server

error log.

Focused on the

nodes involved

in the deadlock.

Each node has a

dedicated

section, and the

final section

describes the

deadlock victim.

## Returns information in an

XML-like format that doesn't

conform to an XML Schema

Definition (XSD) schema. The

format has three major

sections. The first section

declares the deadlock victim.

The second section describes

each process involved in the

deadlock. The third section

describes the resources that

are synonymous with nodes in

trace flag 1204.

Identifying

attributes

Identifies the

session ID thread in cases of parallel

processes. The entry

,

where

is replaced by the SPID

value, represents the main thread. The

entry

, where

is

replaced by the SPID value and

is

greater than 0, represents the

execution context for the same SPID.

Represents

the entry number

in the deadlock

chain.

The lock

owner can be

part of these

lists:

Represents

the physical memory address

of the task (see

sys.dm_os_tasks

) that was

selected as a deadlock victim.

The value might be zero in the

case of an unresolved

deadlock.

Represents

）

Important

Avoid using trace flags 1204 and 1222 on workload-intensive systems that are

experiencing deadlocks. Using these trace flags might introduce performance issues.

Instead, use the

to capture the necessary information.

ﾉ

Expand table

(

for trace flag 1222).

Identifies the batch from which code

execution is requesting or holding a

lock. When Multiple Active Result Sets

(MARS) is disabled, the BatchID value

is 0. When MARS is enabled, the value

for active batches is 1 to

n. If there are

no active batches in the session,

BatchID is 0.

Specifies the type of lock for a

particular resource that is requested,

granted, or waited on by a thread.

Mode can be Intent Shared (

),

Shared (

), Update (

), Intent

Exclusive (

), Shared with Intent

Exclusive (

), and Exclusive (

).

(

for trace flag 1222). Lists

the line number in the current batch of

statements that was being executed

when the deadlock occurred.

(

for trace flag

1222). Lists all the statements in the

current batch.

Enumerates the

current owners

of the resource.

Enumerates the

current owners

that are trying to

convert their

locks to a higher

level.

Enumerates

current new lock

requests for the

resource.

Describes the

type of

statement

(

,

,

, or

) on which

the threads have

## permissions.

Specifies

the participating

thread that the

Database Engine

chooses as the

victim to break

the deadlock

cycle. The chosen

thread and all of

its execution

contexts are

terminated.

Represents the

two or more

the Transact-SQL call stack

that is being executed at the

time the deadlock occurs.

Represents deadlock

priority.

Log space used by

the task.

The ID of the

transaction that has control of

the request.

State of the task. For

more information, see

sys.dm_os_tasks.

The resource

needed by the task.

Time in milliseconds

waiting for the resource.

The scheduler

associated with this task. See

sys.dm_os_schedulers.

The name of the

workstation.

The current

transaction isolation level.

The ID of the

transaction that has control of

the request.

The ID of the

database.

The last

time a client process started

batch execution.

The last

execution

contexts from

the same SPID

that are involved

in the deadlock

cycle.

time a client process

completed batch execution.

and

The set options

on this session. These values

are bitmasks representing the

options usually controlled by

statements such as

and.

For more information, see

@@OPTIONS.

Represents the HoBT (heap or

B-tree) ID.

Resource

attributes

identifies the single row within a

table on which a lock is held or

requested. RID is represented as RID:. For

example,.

identifies the table on which a

lock is held or requested.

is

represented as. For example,.

Identifies the key range within an

index on which a lock is held or

requested. KEY is represented as KEY:

(

index key hash value

).

For example,.

Identifies the page resource on

which a lock is held or requested.

is represented as. For example,.

Identifies the extent structure.

is represented as. For example,.

None exclusive

to this trace flag.

None exclusive to this trace

flag.

```sql
SPID:<x> ECID:<x>.
```

```sql
SPID:<x> ECID:0
```

```sql
<x>
```

```sql
SPID:<x> ECID:<y>
```

```sql
<x>
```

```sql
<y>
```

`Node`

`Lists`

```sql
deadlock victim
```

`executionstack`

`BatchID`

`sbid`

`Mode`

`IS`

```sql
S
```

```sql
U
```

`IX`

`SIX`

```sql
X
```

```sql
Line #
```

`line`

```sql
Input Buf
```

`inputbuf`

```sql
Grant List
```

```sql
Convert List
```

```sql
Wait List
```

```sql
Statement Type
```

`SELECT`

`INSERT`

`UPDATE`

`DELETE`

```sql
Victim Resource
Owner
```

```sql
Next Branch
```

`priority`

`logused`

```sql
owner id
```

`status`

`waitresource`

`waittime`

`schedulerid`

`hostname`

`isolationlevel`

`Xactid`

`currentdb`

`lastbatchstarted`

`lastbatchcompleted`

`clientoption1`

`clientoption2`

`SET`

```sql
SET
NOCOUNT
```

```sql
SET XACTABORT
```

`associatedObjectId`

`RID`

```sql
db_id:file_id:page_no:row_no
```

```sql
RID: 6:1:20789:0
```

`OBJECT`

`OBJECT`

```sql
OBJECT:
db_id:object_id
```

```sql
TAB:
6:2009058193
```

`KEY`

```sql
db_id:hobt_id
```

```sql
KEY:
6:72057594057457664 (350007a4d329)
```

`PAG`

`PAG`

```sql
PAG:
db_id:file_id:page_no
```

```sql
PAG: 6:1:20789
```

`EXT`

`EXT`

```sql
EXT:
db_id:file_id:extent_no
```

```sql
EXT: 6:1:9
```

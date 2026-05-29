---
title: 'Optimized locking and deadlocks'
topic: 'locking'
description: 'The second update statement in'
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

### Session A

### Session B

### Session A

### Session B

### Session A

### Session B

### Session A

### Session B

### Session A

The second update statement in

is blocked by

on the

.

and

are now mutually blocking one another. Neither transaction can

proceed, as they each need a resource that is locked by the other.

After a few seconds, the deadlock monitor identifies that the transactions in

and

are mutually blocking one another, and that neither can make progress. You see a

deadlock occur, with

chosen as the deadlock victim.

completes

successfully. An error message appears in the query window of

with text similar to

the following example:

Output

If a deadlock isn't raised, verify that

is enabled in your sample

database. Deadlocks can occur in any database configuration, but this example requires that

is enabled.

You can view the details of the deadlock in the

target of the

event

session, which is enabled and active by default in SQL Server and Azure SQL Managed Instance.

Consider the following query:

SQL

You can view the XML in the

column inside SSMS, by selecting the cell that

appears as a hyperlink. Save this output as a

file, close, then reopen the

file in SSMS

for visual deadlock graph. The deadlock graph should look something like the following image.

With

optimized locking

, page and row locks aren't held until the end of transaction. They are

released as soon as a row is updated. Additionally, if

is enabled,

update (

) locks aren't used. As a result, the likelihood of deadlocks is reduced.

The previous example doesn't cause a deadlock when optimized locking is enabled because it

relies on the update (

) locks.

The following example can be used to cause a deadlock on a database that has optimized

locking enabled.

First, create an example table and add data.

SQL



The following T-SQL batches, executed in sequence in two separate sessions, create a

deadlock.

In session 1:

SQL

In session 2:

SQL

In session 1:

SQL

In session 2:

SQL

In this case, each session holds an exclusive (

) lock on its own transaction ID (TID) resource,

and is waiting on the shared (

) lock on the other TID, resulting in a deadlock.

The following abbreviated deadlock report contains elements and attributes specific to

optimized locking. Under each resource in the deadlock report

, each

element reports the underlying resources and TID lock information of each

member of a deadlock.

XML

Extended Events overview

sys.dm_tran_locks (Transact-SQL)

Deadlock Graph Event Class

Deadlocks with Read Repeatable Isolation Level

Lock:Deadlock Chain Event Class

Lock:Deadlock Event Class

SET DEADLOCK_PRIORITY (Transact-SQL)

Analyze and prevent deadlocks in Azure SQL Database and SQL database in Fabric

Open, view, and print a deadlock file in SQL Server Management Studio (SSMS)

Last updated on 11/18/2025

Related content

```sql
SalesLT.ProductDescription
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
ring_buffer
```

```sql
system_health
```

```sql
FROM
SalesLT.ProductDescription
AS
pd
INNER
JOIN
SalesLT.ProductModelProductDescription
AS
pmpd
ON
pd.ProductDescriptionID = pmpd.ProductDescriptionID
INNER
JOIN
SalesLT.ProductModel
AS
pm
ON
pmpd.ProductModelID = pm.ProductModelID
INNER
JOIN
SalesLT.Product
AS
p
ON
pm.ProductModelID = p.ProductModelID
WHERE
p.Color =
'Red'
;
Msg 1205, Level 13, State 51, Line 7
Transaction (Process ID 51) was deadlocked on lock resources with another process
and has been chosen as the deadlock victim. Rerun the transaction.
WITH
cteDeadLocks ([Deadlock_XML])
AS
(
SELECT
CAST
(target_data
AS
XML
)
AS
[Deadlock_XML]
FROM
sys.dm_xe_sessions
AS
xs
INNER
JOIN
sys.dm_xe_session_targets
AS
xst
ON
xs.[address] = xst.event_session_address
WHERE
xs.[
name
] =
'system_health'
AND
xst.target_name =
'ring_buffer'
)
SELECT
x.Graph.query(
'(event/data/value/deadlock)[1]'
)
AS
Deadlock_XML,
x.Graph.value(
'(event/data/value/deadlock/process-
list/process/@lastbatchstarted)[1]'
,
'datetime2(3)'
)
AS
when_occurred,
DB_Name(x.Graph.value(
'(event/data/value/deadlock/process-
```

```sql
Deadlock_XML
```

```sql
.xdl
```

```sql
.xdl
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
U
```

```sql
U
```

```sql
list/process/@currentdb)[1]'
,
'int'
))
AS
DB
--Current database of the first listed
process
FROM
(
SELECT
Graph.query(
'.'
)
AS
Graph
FROM
cteDeadLocks
AS
c
CROSS
APPLY
c.
[Deadlock_XML].nodes(
'RingBufferTarget/event[@name="xml_deadlock_report"]'
)
AS
Deadlock_Report(Graph))
AS
x
ORDER
BY
when_occurred
DESC
;
```

```sql
CREATE
TABLE
t2
(
a
INT
PRIMARY
KEY
NOT
NULL
,
b
INT
NULL
);
INSERT
INTO
t2
VALUES
(1, 10),
(2, 20),
(3, 30);
```

```sql
X
```

```sql
S
```

```sql
<resource-list>
```

```sql
<xactlock>
```

```sql
BEGIN
TRANSACTION
xactA;
UPDATE
t2
SET
b = b + 10
WHERE
a = 1;
BEGIN
TRANSACTION
xactB;
UPDATE
t2
SET
b = b + 10
WHERE
a = 2;
UPDATE
t2
SET
b = b + 100
WHERE
a = 2;
UPDATE
t2
SET
b = b + 20
WHERE
a = 1;
```

```sql
<deadlock>
<victim-list>
<victimProcess
id
=
"process12994344c58"
/>
</victim-list>
<process-list>
<process
id
=
"process12994344c58"
taskpriority
=
"0"
logused
=
"272"
waitresource
=
"XACT: 23:2476:0 KEY: 23:72057594049593344 (8194443284a0)"
waittime
=
"447"
ownerId
=
"3234906"
transactionname
=
"xactA"
lasttranstarted
=
"2025-10-
08T21:36:34.063"
XDES
=
"0x12984ba0480"
lockMode
=
"S"
schedulerid
=
"2"
kpid
=
"204928"
status
=
"suspended"
spid
=
"95"
sbid
=
"0"
ecid
=
"0"
priority
=
"0"
trancount
=
"2"
lastbatchstarted
=
"2025-10-08T21:36:40.857"
lastbatchcompleted
=
"2025-10-
08T21:36:34.063"
lastattention
=
"2025-10-08T21:36:11.340"
clientapp
=
"Microsoft SQL
Server Management Studio - Query"
hostname
=
"WS1"
hostpid
=
"23380"
loginname
=
"user1"
isolationlevel
=
"read committed (2)"
xactid
=
"3234906"
currentdb
=
"23"
currentdbname
=
"AdventureWorksLT"
lockTimeout
=
"4294967295"
clientoption1
=
"671090784"
clientoption2
=
"390200"
>
<inputbuf>
UPDATE t2
SET b = b + 20
WHERE a = 1;
</inputbuf>
</process>
<process
id
=
"process1299c969828"
taskpriority
=
"0"
logused
=
"272"
waitresource
=
"XACT: 23:2477:0 KEY: 23:72057594049593344 (61a06abd401c)"
waittime
=
"3083"
ownerId
=
"3234886"
transactionname
=
"xactB"
lasttranstarted
=
"2025-10-
08T21:36:30.303"
XDES
=
"0x12995c84480"
lockMode
=
"S"
schedulerid
=
"2"
kpid
=
"63348"
status
=
"suspended"
spid
=
"88"
sbid
=
"0"
ecid
=
"0"
priority
=
"0"
trancount
=
"2"
lastbatchstarted
=
"2025-10-08T21:36:38.223"
lastbatchcompleted
=
"2025-10-
08T21:36:30.303"
lastattention
=
"1900-01-01T00:00:00.303"
clientapp
=
"Microsoft SQL
Server Management Studio - Query"
hostname
=
"WS1"
hostpid
=
"23380"
loginname
=
"user1"
isolationlevel
=
"read committed (2)"
xactid
=
"3234886"
currentdb
=
"23"
currentdbname
=
"AdventureWorksLT"
lockTimeout
=
"4294967295"
clientoption1
=
"671090784"
clientoption2
=
"390200"
>
<inputbuf>
UPDATE t2
SET b = b + 100
WHERE a = 2;
</inputbuf>
</process>
</process-list>
<resource-list>
<xactlock
xdesIdLow
=
"2476"
xdesIdHigh
=
"0"
dbid
=
"23"
id
=
"lock1299fa06c00"
mode
=
"X"
>
<UnderlyingResource>
<keylock
hobtid
=
"72057594049593344"
dbid
=
"23"
objectname
=
"e6fc405e-1ee8-49df-
a2b3-54ee0151d851.dbo.t2"
indexname
=
"PK__t2__3BD0198ED3CBA65E"
/>
</UnderlyingResource>
<owner-list>
<owner
id
=
"process1299c969828"
mode
=
"X"
/>
</owner-list>
<waiter-list>
<waiter
id
=
"process12994344c58"
mode
=
"S"
requestType
=
"wait"
/>
</waiter-list>
</xactlock>
```

```sql
<xactlock
xdesIdLow
=
"2477"
xdesIdHigh
=
"0"
dbid
=
"23"
id
=
"lock129940b2380"
mode
=
"X"
>
<UnderlyingResource>
<keylock
hobtid
=
"72057594049593344"
dbid
=
"23"
objectname
=
"e6fc405e-1ee8-49df-
a2b3-54ee0151d851.dbo.t2"
indexname
=
"PK__t2__3BD0198ED3CBA65E"
/>
</UnderlyingResource>
<owner-list>
<owner
id
=
"process12994344c58"
mode
=
"X"
/>
</owner-list>
<waiter-list>
<waiter
id
=
"process1299c969828"
mode
=
"S"
requestType
=
"wait"
/>
</waiter-list>
</xactlock>
</resource-list>
</deadlock>
```

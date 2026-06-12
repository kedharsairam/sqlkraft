---
title: "Deadlock extended event"
topic: "locking"
description: "and continue. The 1205 (deadlock victim) error records information about the type of resources"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

and continue. The 1205 (deadlock victim) error records information about the type of resources

involved in a deadlock.

By default, the Database Engine chooses the transaction running the transaction that is the

least expensive to roll back as the deadlock victim. Alternatively, a user can specify the priority

of sessions in a deadlock situation using the

statement.

can be set to

,

, or

, or alternatively can be set to any

integer value in the range from -10 to 10. In certain cases, the Database Engine might opt to

alter the deadlock priority for a short duration to achieve better concurrency.

The deadlock priority defaults to

, or 0. If two sessions have different deadlock priorities,

the transaction on the session with the lower priority is chosen as the deadlock victim. If both

sessions have the same deadlock priority, the transaction that is least expensive to roll back is

chosen. If sessions involved in the deadlock cycle have the same deadlock priority and the

same cost, a victim is chosen randomly. A task that is rolling back can't be chosen as a

deadlock victim.

When working with common language runtime (CLR), the deadlock monitor automatically

detects deadlocks for synchronization resources (monitors, reader/writer lock, and thread join)

accessed inside managed procedures. However, the deadlock is resolved by throwing an

exception in the procedure that was selected to be the deadlock victim. It's important to

understand that the exception doesn't automatically release resources currently owned by the

victim; the resources must be explicitly released. Consistent with exception behavior, the

exception used to identify a deadlock victim can be caught and dismissed.

To view deadlock information, the Database Engine provides monitoring tools in the form of

the

extended event, two trace flags, and the deadlock graph event in SQL

Profiler.

The

extended event is the recommended method for capturing deadlock

information.

In SQL Server 2012 (11.x) and later versions, the

extended event should

be used instead of the deadlock graph event class in SQL Trace or SQL Profiler.

The

system_health

event session captures

events by default. These events

contain the deadlock graph. Because the

session is enabled by default, you

don't need to configure a separate event session to capture deadlock information.

The deadlock graph captured typically has three distinct nodes:. The deadlock victim process identifier. Information on all the processes involved in the deadlock. Information about the resources involved in the deadlock.

You can view the

target data of the

session in Management Studio.

If any

events occurred, Management Studio presents a graphical

depiction of the tasks and resources involved in a deadlock, as seen in the following example:

The following query can view all deadlock events captured by the

target of the

session:

Here's the result set.



The following example shows an example of the output from the

column:

XML

```sql
SET DEADLOCK_PRIORITY
```

`DEADLOCK_PRIORITY`

`LOW`

`NORMAL`

`HIGH`

`NORMAL`

`xml_deadlock_report`

`xml_deadlock_report`

`xml_deadlock_report`

`xml_deadlock_report`

`system_health`

```sql
victim-list
```

```sql
process-list
```

```sql
resource-list
```

`event_file`

`system_health`

`xml_deadlock_report`

`ring_buffer`

`system_health`

```sql
SELECT xdr.value(
'@timestamp'
,
'datetime'
)
AS deadlock_time,
xdr.query(
'.'
)
AS event_data
FROM (
SELECT
CAST ([target_data]
AS
XML
)
AS target_data
FROM sys.dm_xe_session_targets
AS xt
INNER
JOIN sys.dm_xe_sessions
AS xs
ON xs.address = xt.event_session_address
WHERE xs.name = N
'system_health'
AND xt.target_name = N
'ring_buffer'
)
AS
XML_Data
CROSS
APPLY
Target_Data.nodes(
'RingBufferTarget/event[@name="xml_deadlock_report"]'
)
AS
XEventData(xdr)
ORDER
BY deadlock_time
DESC
;
```

`event_data`

```sql
<event name
=
"xml_deadlock_report"
package
=
"sqlserver"
timestamp
=
"2022-02-
18T08:26:24.698Z"
>
<data name
=
"xml_report"
>
<type name
=
"xml"
package
=
"package0"
/>
<value>
<deadlock>
<victim-list>
<victimProcess id
=
"process27b9b0b9848"
/>
</victim-list>
<process-list>
<process id
=
"process27b9b0b9848"
taskpriority
=
"0"
logused
=
"0"
waitresource
=
"KEY: 5:72057594214350848 (1a39e6095155)"
waittime
=
"1631"
ownerId
=
"11088595"
transactionname
=
"SELECT"
lasttranstarted
=
"2022-02-
18T00:26:23.073"
XDES
=
"0x27b9f79fac0"
lockMode
=
"S"
schedulerid
=
"9"
kpid
=
"15336"
status
=
"suspended"
spid
=
"62"
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
"0"
lastbatchstarted
=
"2022-02-18T00:26:22.893"
lastbatchcompleted
=
"2022-02-
18T00:26:22.890"
lastattention
=
"1900-01-01T00:00:00.890"
clientapp
=
"SQLCMD"
hostname
=
"ContosoServer"
hostpid
=
"7908"
loginname
=
"CONTOSO\user"
isolationlevel
=
"read committed (2)"
xactid
=
"11088595"
currentdb
=
"5"
lockTimeout
=
"4294967295"
clientoption1
=
"538968096"
clientoption2
=
"128056"
>
<executionStack>
<frame procname
=
"AdventureWorks2022.dbo.p1"
line
=
"3"
stmtstart
=
"78"
stmtend
=
"180"
sqlhandle
=
"0x0300050020766505ca3e07008ba80000010000000000000000000000000000000000000
00000000000000000"
>
SELECT c2, c3 FROM t1 WHERE c2 BETWEEN @p1 AND @p1+
</frame>
<frame procname
=
"adhoc"
line
=
"4"
stmtstart
=
"82"
stmtend
=
"98"
sqlhandle
=
"0x020000006263ec01ebb919c335024a072a2699958d3fcce600000000000000000000000
00000000000000000"
>
unknown
</frame>
</executionStack>
<inputbuf>
SET NOCOUNT ON
WHILE (1=1)
BEGIN
EXEC p1 4
END
</inputbuf>
</process>
<process id
=
"process27b9ee33c28"
taskpriority
=
"0"
logused
=
"252"
waitresource
=
"KEY: 5:72057594214416384 (e5b3d7e750dd)"
waittime
=
"1631"
ownerId
=
"11088593"
transactionname
=
"UPDATE"
lasttranstarted
=
"2022-02-
18T00:26:23.073"
XDES
=
"0x27ba15a4490"
lockMode
=
"X"
schedulerid
=
"6"
kpid
=
"5584"
```

```sql
status
=
"suspended"
spid
=
"58"
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
"2022-02-18T00:26:22.890"
lastbatchcompleted
=
"2022-02-
18T00:26:22.890"
lastattention
=
"1900-01-01T00:00:00.890"
clientapp
=
"SQLCMD"
hostname
=
"ContosoServer"
hostpid
=
"15316"
loginname
=
"CONTOSO\user"
isolationlevel
=
"read committed (2)"
xactid
=
"11088593"
currentdb
=
"5"
lockTimeout
=
"4294967295"
clientoption1
=
"538968096"
clientoption2
=
"128056"
>
<executionStack>
<frame procname
=
"AdventureWorks2022.dbo.p2"
line
=
"3"
stmtstart
=
"76"
stmtend
=
"150"
sqlhandle
=
"0x03000500599a5906ce3e07008ba80000010000000000000000000000000000000000000
00000000000000000"
>
UPDATE t1 SET c2 = c2+1 WHERE c1 = @p
</frame>
<frame procname
=
"adhoc"
line
=
"4"
stmtstart
=
"82"
stmtend
=
"98"
sqlhandle
=
"0x02000000008fe521e5fb1099410048c5743ff7da04b2047b00000000000000000000000
00000000000000000"
>
unknown
</frame>
</executionStack>
<inputbuf>
SET NOCOUNT ON
WHILE (1=1)
BEGIN
EXEC p2 4
END
</inputbuf>
</process>
</process-list>
<resource-list>
<keylock hobtid
=
"72057594214350848"
dbid
=
"5"
objectname
=
"AdventureWorks2022.dbo.t1"
indexname
=
"cidx"
id
=
"lock27b9dd26a00"
mode
=
"X"
associatedObjectId
=
"72057594214350848"
>
<owner-list>
<owner id
=
"process27b9ee33c28"
mode
=
"X"
/>
</owner-list>
<waiter-list>
<waiter id
=
"process27b9b0b9848"
mode
=
"S"
requestType
=
"wait"
/>
</waiter-list>
</keylock>
<keylock hobtid
=
"72057594214416384"
dbid
=
"5"
objectname
=
"AdventureWorks2022.dbo.t1"
indexname
=
"idx1"
id
=
"lock27afa392600"
mode
=
"S"
associatedObjectId
=
"72057594214416384"
>
<owner-list>
<owner id
=
"process27b9b0b9848"
mode
=
"S"
/>
</owner-list>
<waiter-list>
<waiter id
=
"process27b9ee33c28"
mode
=
"X"
requestType
=
"wait"
/>
</waiter-list>
</keylock>
</resource-list>
</deadlock>
</value>
</data>
</event>
```

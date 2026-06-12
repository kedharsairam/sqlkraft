---
title: "Trace flag 1222 example"
topic: "query-processing"
description: "The following example shows the output when trace flag 1222 is turned on."
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

The following example shows the output when trace flag 1222 is turned on. In this case, one

table is a heap with no indexes, and the other table is a heap with a nonclustered index. In the

second table, the index key is being updated when the deadlock occurs.

Output

```sql
Node:1
RID: 6:1:20789:0 CleanCnt:3 Mode:X Flags: 0x2
Grant List 0:
Owner:0x0315D6A0 Mode: X
Flg:0x0 Ref:0 Life:02000000 SPID:55 ECID:0 XactLockInfo: 0x04D9E27C
SPID: 55 ECID: 0 Statement Type: UPDATE Line #: 6
Input Buf: Language Event:
BEGIN TRANSACTION
EXEC usp_p2
Requested By:
ResType:LockOwner Stype:'OR'Xdes:0x03A3DAD0
Mode: U SPID:54 BatchID:0 ECID:0 TaskProxy:(0x04976374) Value:0x315d200 Cost:
(0/868)
Node:2
KEY: 6:72057594057457664 (350007a4d329) CleanCnt:2 Mode:X Flags: 0x0
Grant List 0:
Owner:0x0315D140 Mode: X
Flg:0x0 Ref:0 Life:02000000 SPID:54 ECID:0 XactLockInfo: 0x03A3DAF4
SPID: 54 ECID: 0 Statement Type: UPDATE Line #: 6
Input Buf: Language Event:
BEGIN TRANSACTION
EXEC usp_p1
Requested By:
ResType:LockOwner Stype:'OR'Xdes:0x04D9E258
Mode: U SPID:55 BatchID:0 ECID:0 TaskProxy:(0x0475E374) Value:0x315d4a0 Cost:
(0/380)
Victim Resource Owner:
ResType:LockOwner Stype:'OR'Xdes:0x04D9E258
Mode: U SPID:55 BatchID:0 ECID:0 TaskProxy:(0x0475E374) Value:0x315d4a0 Cost:
(0/380)
```

```sql
deadlock-list deadlock victim=process689978 process-list process id=process6891f8 taskpriority=0 logused=868 waitresource=RID: 6:1:20789:0 waittime=1359 ownerId=310444 transactionname=user_transaction lasttranstarted=2022-02-05T11:22:42.733 XDES=0x3a3dad0 lockMode=U schedulerid=1 kpid=1952 status=suspended spid=54
```

```sql
sbid=0 ecid=0 priority=0 transcount=2 lastbatchstarted=2022-02-05T11:22:42.733 lastbatchcompleted=2022-02-05T11:22:42.733 clientapp=Microsoft SQL Server Management Studio - Query hostname=TEST_SERVER hostpid=2216 loginname=DOMAIN\user isolationlevel=read committed (2) xactid=310444 currentdb=6 lockTimeout=4294967295 clientoption1=671090784 clientoption2=390200 executionStack frame procname=AdventureWorks2022.dbo.usp_p1 line=6 stmtstart=202 sqlhandle=0x0300060013e6446b027cbb00c69600000100000000000000
UPDATE T2 SET COL1 = 3 WHERE COL1 = 1;
frame procname=adhoc line=3 stmtstart=44 sqlhandle=0x01000600856aa70f503b8104000000000000000000000000
EXEC usp_p1 inputbuf
BEGIN TRANSACTION
EXEC usp_p1 process id=process689978 taskpriority=0 logused=380 waitresource=KEY: 6:72057594057457664 (350007a4d329) waittime=5015 ownerId=310462 transactionname=user_transaction lasttranstarted=2022-02-05T11:22:44.077 XDES=0x4d9e258 lockMode=U schedulerid=1 kpid=3024 status=suspended spid=55 sbid=0 ecid=0 priority=0 transcount=2 lastbatchstarted=2022-02-05T11:22:44.077 lastbatchcompleted=2022-02-05T11:22:44.077 clientapp=Microsoft SQL Server Management Studio - Query hostname=TEST_SERVER hostpid=2216 loginname=DOMAIN\user isolationlevel=read committed (2) xactid=310462 currentdb=6 lockTimeout=4294967295 clientoption1=671090784 clientoption2=390200 executionStack frame procname=AdventureWorks2022.dbo.usp_p2 line=6 stmtstart=200 sqlhandle=0x030006004c0a396c027cbb00c69600000100000000000000
UPDATE T1 SET COL1 = 4 WHERE COL1 = 1;
frame procname=adhoc line=3 stmtstart=44 sqlhandle=0x01000600d688e709b85f8904000000000000000000000000
EXEC usp_p2 inputbuf
BEGIN TRANSACTION
EXEC usp_p2 resource-list ridlock fileid=1 pageid=20789 dbid=6 objectname=AdventureWorks2022.dbo.T2 id=lock3136940 mode=X associatedObjectId=72057594057392128 owner-list owner id=process689978 mode=X waiter-list waiter id=process6891f8 mode=U requestType=wait keylock hobtid=72057594057457664 dbid=6 objectname=AdventureWorks2022.dbo.T1 indexname=nci_T1_COL1 id=lock3136fc0 mode=X associatedObjectId=72057594057457664 owner-list owner id=process6891f8 mode=X waiter-list waiter id=process689978 mode=U requestType=wait
```

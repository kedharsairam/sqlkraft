---
title: "PreConnect:Completed Event Class"
topic: "event-classes"
description: "The PreConnect:Completedevent class indicates when a LOGON trigger or the Resource Governor"
tags: ["event-classes","preconnectcompleted-event-class"]
pubDate: "2025-12-01"
---

The PreConnect:Completedevent class indicates when a LOGON trigger or the Resource

Governor classifier function finishes execution.

Description

EventClass

216

27

No

SPID

The ID of server process that fires this event.

12

Yes

EventSubClass

1 for the user-defined classifier function.

21

Yes

StartTime

The time when the user-defined classifier

function starts.

14

Yes

EndTime

The time when the user-defined classifier

function starts.

15

Yes

Duration

The amount of time, in microseconds, used

by the classifier function.

13

Yes

ObjectID

The ID of the user-defined classifier object.

22

Yes

CPU

CPU usage in milliseconds.

18

Yes

Reads

The number of logical reads.

16

Yes

Writes

The number of logical writes.

17

Yes

GroupID

The ID of the classified workload group.

66

Yes

Error

The last error number if the user-defined

classifier function fails to execute.

31

Yes

State

The state of the last error.

30

Yes

TargetUserName

The return value (workload group name) for

the user-defined classifier function if the

system can not find a corresponding active

group. Otherwise, this column is set to NULL.

39

Yes

ﾉ

Expand table

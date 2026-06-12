---
title: "Background Job Error Event Class"
topic: "event-classes"
description: "The event class occurs when a background job has terminated abnormally."
tags: ["event-classes","background-job-error-event-class"]
pubDate: 2025-12-01
---

The

event class occurs when a background job has terminated

abnormally. This condition might require the attention of a system administrator.

Description

ID of the database specified by job. Determine

the value for a database by using the DB_ID

function.

3

Yes

Name of the database in which the user

statement is running.

35

Yes

Error number of the last attempt

(

1 only).

31

Yes

Type of event = 193.

27

No

The sequence of a given event within the

request.

51

No

Type of event subclass.

1 = Background job giving up after failure.

2 = Background job dropped - queue is full.

3 = Background job returned an error.

21

Yes

ID for the index on the object affected by the

event. To determine the index ID for an object,

use the

column of the

system

table.

24

Yes

Number of tries attempted by the job

(

1 only).

25

Yes

Job sequence number.

55

Yes

ﾉ

Expand table

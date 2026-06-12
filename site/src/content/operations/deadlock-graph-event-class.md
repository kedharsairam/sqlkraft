---
title: "Deadlock Graph Event Class"
topic: "event-classes"
description: "2016 (13.x) and later versions Azure SQL Managed Instance The event class provides an XML description of a deadlock. T"
tags: ["event-classes","deadlock-graph-event-class"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

The

event class provides an XML description of a deadlock. This class occurs

simultaneously with the

event class.

Description

Type of event = 148.

27

No

Sequence of a given event within the request.

51

No

Indicates whether the event occurred on a

system process or a user process. 1 = system, 0

= user. This value is always 1 for this event.

60

Yes

Name of the login of the user (either the

Microsoft SQL Server security login or the

Microsoft Windows login credentials in the

form of DOMAIN\username). This value is

always the system user for this event.

11

Yes

Security identification number (SID) of the

logged-in user. You can find this information in

the sys.server_principals catalog view. Each SID

is unique for each login in the server. This value

is always the SID of the system user for this

event.

41

Yes

Name of the instance of SQL Server being

traced.

26

No

Login name of the user who originated the

session. For example, if you connect to SQL

Server using Login1 and execute a statement as

Login2,

shows Login1 and

shows Login2. This column displays

both SQL Server and Windows logins.

64

Yes

ID of the session on which the event occurred.

12

Yes

ﾉ

Expand table

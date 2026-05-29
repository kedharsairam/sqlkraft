---
title: "Audit Broker Login Event Class"
topic: "event-classes"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL Server creates an

  event to report audit messages related to Service

  Broker transport security.

  D
tags:
  - "event-classes"
  - "audit-broker-login-event-class"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL Server creates an

event to report audit messages related to Service

Broker transport security.

Description

Unused in this event class.

10

Yes

Unused in this event class.

9

Yes

SQL Server Profiler displays the name of the

database if the

data column is

captured in the trace and the server is available.

Determine the value for a database by using the

DB_ID function.

3

Yes

The type of event class captured. Always

for

.

27

No

Sequence number for this event.

51

No

The type of event subclass, providing further

information about each event class. The table

below lists the event subclass values for this

event.

21

Yes

Remote broker authentication level. Supported

authentication method configured on the

remote broker endpoint. When more than one

method is available, the accepting (target)

endpoint determines which method is tried first.

Possible values are:

. No authentication method is configured.

. Requires NTLM authentication.

. Requires Kerberos authentication.

36

No

ﾉ

Expand table

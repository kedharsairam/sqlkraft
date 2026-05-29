---
title: "Possible cause of failures"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  Physical, operating system, or SQL Server problems can cause a failure in a database mirroring

  session. Database mirroring does not regularly check th
tags:
  - "high-availability"
  - "possible-cause-of-failures"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

Physical, operating system, or SQL Server problems can cause a failure in a database mirroring

session. Database mirroring does not regularly check the components on which Sqlservr.exe

relies to verify whether they are functioning correctly or have failed. However, for some types

of failures, the affected component reports an error to Sqlservr.exe. An error reported by

another component is called a

hard error

. To detect other failures that would otherwise go

unnoticed, database mirroring implements its own time-out mechanism. When a mirroring

time-out occurs, database mirroring assumes that a failure has occurred and declares a

soft

error

. However, some failures that happen at the SQL Server instance level do not cause

mirroring to time-out and can go undetected.

The speed of error detection and, therefore, the reaction time of the mirroring session to a

failure, depends on whether the error is hard or soft. Some hard errors, such as network failures

are reported immediately. However, in some cases, component-specific time-out periods can

delay the reporting of some hard errors. For soft errors, the length of the mirroring time-out

period determines the speed of error detection. By default, this period is 10 seconds. This is the

minimum recommended value.

Possible causes of hard errors include (but are not limited to) the following conditions:

A broken connection or wire

A bad network card

A router change

Changes in the firewall

）

Important

Failures in databases other than the mirrored database are not detectable in a database

mirroring session. Moreover, a data disk failure is unlikely to be detected, unless the

database is restarted because of a data disk failure.

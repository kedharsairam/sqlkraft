---
title: "Possible failures during sessions between replicas"
topic: "high-availability"
description: |
  Article

  •

  07/04/2023

  Applies to:

  SQL Server

  Physical, operating system, or SQL Server problems can cause a failure in a session between

  two availability replicas. An availability replica doesn't
tags:
  - "high-availability"
  - "possible-failures-during-sessions-between-replicas"
pubDate: 2025-12-01
---

Article

•

07/04/2023

Applies to:

SQL Server

Physical, operating system, or SQL Server problems can cause a failure in a session between

two availability replicas. An availability replica doesn't regularly check the components on

which

relies to verify whether they are functioning correctly or have failed.

However, for some types of failures, the affected component reports an error to

.

An error reported by another component is called a

hard error

.

To detect other failures that would otherwise go unnoticed, Always On availability groups

implement their own session-timeout mechanism. The session-timeout period is specified in

seconds. This time-out period is the maximum time that a server instance waits to receive a

PING message from another instance before considering that other instance to be

disconnected. When a session timeout occurs between two availability replicas, the availability

replicas assume that a failure has occurred and declares a

soft error

.

The speed of error detection and, therefore, the reaction time to a failure, depends on whether

the error is hard or soft. Some hard errors, such as network failures are reported immediately.

However, in some cases, component-specific time-out periods can delay the reporting of some

hard errors. For soft errors, the length of the session-timeout period determines the speed of

error detection. By default, this period is 10 seconds. This is the minimum recommended value.

Possible causes of hard errors include (but aren't limited to) the following conditions:

A broken connection or wire

A bad network card

A router change

Changes in the firewall

Endpoint reconfiguration

）

Important

Failures in databases other than the primary database are not detectable. Moreover, a

data disk failure is unlikely to be detected unless the database is restarted because of a

data disk failure.

```cmd
sqlservr.exe sqlservr.exe
```

---
title: "Monitoring"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  This section introduces Database Mirroring Monitor and the

  system stored

  procedures, explains how database mirroring monitoring works (including the

tags:
  - "high-availability"
  - "monitoring"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

This section introduces Database Mirroring Monitor and the

system stored

procedures, explains how database mirroring monitoring works (including the

, and summarizes the information that you can monitor about database

mirroring sessions. Additionally, this section introduces how to define warning thresholds for a

set of predefined database mirroring events and how to set up alerts on any database

mirroring event.

You can monitor a mirrored database during a mirroring session to verify whether and how

well data is flowing. To set up and manage monitoring for one or more of the mirrored

databases on a server instance, you can use either Database Mirroring Monitor or the

system stored procedures.

A database mirroring monitoring job,

, operates in the

background, independently of Database Mirroring Monitor. SQL Server Agent calls

at regular intervals, the default is once a minute, and the job calls a

stored procedure that updates mirroring status. If you use SQL Server Management Studio to

start a mirroring session,

is created automatically. However, if

you only use ALTER DATABASE

<database_name>

SET PARTNER to start mirroring, you must

create the job by running a stored procedure.

Monitoring Mirroring Status

Additional Sources of Information About a Mirrored Database

To set up and manage monitoring for one or more of the mirrored databases on a server

instance, you can use either Database Mirroring Monitor or the

system stored

procedures. You can monitor a mirrored database during a mirroring session to verify whether

and how well data is flowing.

Specifically, monitoring a mirrored database enables you to:

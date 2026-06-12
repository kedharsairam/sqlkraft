---
title: "Issue Element"
topic: "ssb-diagnose"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  Reports an issue that was found by the

  utility. The

  XML output file

  has one Issue element per issue reported.

  Description

  Identifies which categor
tags:
  - "ssb-diagnose"
  - "issue-element"
pubDate: 2025-12-01
---

Article

•

03/03/2023

SQL Server

Reports an issue that was found by the

utility. The

XML output file

has one Issue element per issue reported.

Description

Identifies which category of problem the Issue element is reporting:

Reports a configuration issue found when you analyze a Service Broker

configuration.

Reports an issue that has prevented

from completing its analysis.

Correct the problem and rerun.

Reports a SQL Server Profiler event found when you run a

check. Events

are only reported if

is specified.

Identifies the error number for the message.

Identifies the instance of the Database Engine in which the problem was found. If the

problem was in a default instance, the server attribute only has the computer name. If the

problem was in a named instance, the server attribute is in the form

ComputerName\InstanceName.

ﾉ

Expand table

```cmd
<Issue type="."
code="."
server="."
database="."
object=".">.
</Issue>
```

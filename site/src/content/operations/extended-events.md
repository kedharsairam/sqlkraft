---
title: "Extended events"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  SQL Server defines Extended Events that are specific to availability groups. You can monitor

  these Extended Events in a session to help with root-caus
tags:
  - "high-availability"
  - "extended-events"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

SQL Server defines Extended Events that are specific to availability groups. You can monitor

these Extended Events in a session to help with root-cause diagnosis when you troubleshoot

an availability group. You can view the availability group Extended Events using the following

query:

SQL

The

Extended Events session is created automatically when you create the

availability group, and captures a subset of the availability group related events. This session is

preconfigured as a useful and convenient tool to help you get started quickly while

troubleshooting an availability group. The Create Availability Group Wizard automatically starts

the session on every participating availability replica configured in the wizard.

To view the definition of the

session:

1. In the

, expand

,

, and then

.

2. Right-click

, then point to

, then point to

,

and then select

.

）

Important

If you did not create the availability group using the

, the

session may not be automatically started. If the session is not started, it

cannot capture event data when an unexpected issue occurs. You should manually start

the session and configure the session to start automatically by configuring the session

properties.

```cmd
alwayson_health
alwayson_health
SELECT
*
FROM
sys.dm_xe_objects
WHERE
name
LIKE
'%hadr%'
;
alwayson_health
```

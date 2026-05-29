---
title: 'Hot add CPU'
topic: 'query-processing'
description: 'Microsoft Windows uses a numeric priority system that ranges from 1 through 31 to schedule'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Microsoft Windows uses a numeric priority system that ranges from 1 through 31 to schedule

threads for execution. Zero is reserved for operating system use. When several threads are

waiting to execute, Windows dispatches the thread with the highest priority.

By default, each instance of SQL Server is a priority of 7, which is referred to as the normal

priority. This default gives SQL Server threads a high enough priority to obtain sufficient CPU

resources without adversely affecting other applications.

The

priority boost

configuration option can be used to increase the priority of the threads from

an instance of SQL Server to 13. This is referred to as high priority. This setting gives SQL Server

threads a higher priority than most other applications. Thus, SQL Server threads will generally

be dispatched whenever they are ready to run and are not preempted by threads from other

applications. This can improve performance when a server is running only instances of SQL

Server and no other applications. However, if a memory-intensive operation occurs in SQL

Server, however, other applications aren't likely to have a high-enough priority to preempt the

SQL Server thread.

If you are running multiple instances of SQL Server on a computer, and turn on priority boost

for only some of the instances, the performance of any instances running at normal priority can

be adversely affected. Also, the performance of other applications and components on the

server can decline if priority boost is turned on. Therefore, it should only be used under tightly

controlled conditions.

Do not use fiber mode scheduling for routine operation. This can decrease performance

by inhibiting the regular benefits of context switching, and because some components of

SQL Server cannot function correctly in fiber mode. For more information, see

.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

）

Important

---
title: "Lesson 2: Connecting from Another Computer"
topic: "configuration"
description: |
  08/26/2025

  Applies to:

  SQL Server

  For enhanced security, the Database Engine of SQL Server Developer, Express, and Evaluation

  editions can't be accessed from another computer when initially instal
tags:
  - "configuration"
  - "lesson-2-connecting-from-another-computer"
pubDate: 2025-12-01
---

08/26/2025

Applies to:

SQL Server

For enhanced security, the Database Engine of SQL Server Developer, Express, and Evaluation

editions can't be accessed from another computer when initially installed. This lesson shows

how to enable the protocols, configure the ports, and configure Windows Firewall for

connecting to the Database Engine from other computers.

This lesson contains the following tasks:

Enabling protocols

Configuring a fixed port

Opening ports in the firewall

Connecting to the Database Engine from another computer

Connecting by using the SQL Server Browser service

For enhanced security, SQL Server Express, Developer, and Evaluation editions install with only

limited network connectivity. Connections to the Database Engine can be made from tools that

are running on the same computer but not from other computers. If you're planning to do

your development work on the same computer as the Database Engine, you don't need to

enable additional protocols. Management Studio connects to the Database Engine by using the

shared memory protocol. This protocol is already enabled.

If you plan to connect to the Database Engine from another computer, you must enable a

protocol, such as TCP/IP.

1. On the

menu, point to

, point to

, point to

, and then select

SQL Server Configuration Manager

.

７

Note

Check to see whether you have both 32-bit and 64-bit options available.

---
title: "Troubleshoot configuration"
topic: "high-availability"
description: |
  Applies to:

  SQL Server

  This article provides information to help you troubleshoot typical problems with configuring

  server instances for Always On availability groups. Typical configuration problem
tags:
  - "high-availability"
  - "troubleshoot-configuration"
pubDate: 2025-12-01
---

SQL Server

This article provides information to help you troubleshoot typical problems with configuring

server instances for Always On availability groups. Typical configuration problems include

Always On availability groups is disabled, accounts are incorrectly configured, the database

mirroring endpoint doesn't exist, the endpoint is inaccessible (SQL Server Error 1418), network

access doesn't exist, and a join database command fails (SQL Server Error 35250).

Description

Always On Availability

Groups Isn't Enabled

If an instance of SQL Server isn't enabled for Always On availability groups, the

instance doesn't support availability group creation and can't host any

availability replicas.

Accounts

Discusses requirements for correctly configuring the accounts under which

is running.

Endpoints

Discusses how to diagnose issues with the database mirroring endpoint of a

server instance.

Network access

Documents the requirement that each server instance that's hosting an

availability replica must be able to access the port of each of the other server

instances over TCP.

Listener

Documents how to establish the IP address and port of the listener and make

sure it's running and listening for incoming connections

Endpoint Access (SQL

Server Error 1418)

Contains information about this SQL Server error message.

Join Database Fails (SQL

Server Error 35250)

Discusses the possible causes and resolution of a failure to join secondary

databases to an availability group because the connection to the primary

７

Note

Ensure that you're meeting the Always On availability groups prerequisites. For more

information, see

Prerequisites, Restrictions, and Recommendations for Always On.

ﾉ

Expand table

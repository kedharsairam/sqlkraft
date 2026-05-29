---
title: "Troubleshooting & monitoring guide"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  This guide helps you get started on monitoring availability groups and troubleshooting some

  of the common issues in availability groups. It provides original content, and a la
tags:
  - "high-availability"
  - "troubleshooting-monitoring-guide"
pubDate: 2025-12-01
---

Article

•

03/03/2023

This guide helps you get started on monitoring availability groups and troubleshooting some

of the common issues in availability groups. It provides original content, and a landing page of

useful information that is published elsewhere. While this guide can't fully discuss all the issues

that can occur in the large area of availability groups, it can point you in the right direction in

your root-cause analysis and resolution of issues.

Because availability groups are an integrated technology, many problems you encounter may

be symptoms of other issues in your database system. Some issues are caused by settings

within an availability group, such as an availability database being suspended. Other issues can

include problems with other aspects of SQL Server, such as SQL Server settings, database file

deployments, and systemic performance issues unrelated to availability. Still other problems

can exist outside of SQL Server, such as network I/O, TCP/IP, Active Directory, and Windows

Server Failover Clustering (WSFC) issues. Often, problems that surface in an availability group,

replica, or database require you to troubleshoot multiple technologies to identify the root

cause.

The following table contains links to the common troubleshooting scenarios for availability

groups. They are categorized by their scenario types, such as configuration, client connectivity,

failover, and performance.

Description

Troubleshoot Always On

Availability Groups

configuration (SQL Server)

Configuration

Provides information to help you troubleshoot typical

problems with configuring server instances for

availability groups. Typical configuration problems

include:

- availability groups are disabled

- accounts are incorrectly configured

- the database mirroring endpoint doesn't exist

- the endpoint is inaccessible (SQL Server Error 1418)

- network access doesn't exist

ﾉ

Expand table

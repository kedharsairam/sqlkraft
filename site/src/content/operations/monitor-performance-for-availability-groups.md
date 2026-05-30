---
title: "Monitor performance for availability groups"
topic: "high-availability"
description: |
  Article

  •

  03/27/2025

  Applies to:

  SQL Server

  The performance aspect of Always On Availability Groups is crucial to maintaining the service-

  level agreement (SLA) for your mission-critical databas
tags:
  - "high-availability"
  - "monitor-performance-for-availability-groups"
pubDate: 2025-12-01
---

Article

•

03/27/2025

Applies to:

SQL Server

The performance aspect of Always On Availability Groups is crucial to maintaining the service-

level agreement (SLA) for your mission-critical databases. Understanding how availability

groups ship logs to secondary replicas can help you estimate the recovery time objective (RTO)

and recovery point objective (RPO) of your availability implementation and identify bottlenecks

in poorly performing availability groups or replicas. This article describes the synchronization

process, shows you how to calculate some of the key metrics, and gives you the links to some

of the common performance troubleshooting scenarios.

To estimate the time to full synchronization and to identify the bottleneck, you need to

understand the synchronization process. Performance bottleneck can be anywhere in the

process, and locating the bottleneck can help you dig deeper into the underlying issues. The

following figure and table illustrate the data synchronization process:

description

1

Log

generation

Log data is flushed to disk. This log must

be replicated to the secondary replicas.

The log records enter the send queue.

SQL Server:Database > Log bytes

flushed/sec

ﾉ

Expand table

---
title: "Configure (HA add-on)"
topic: "linux-operations"
description: |
  Applies to:
  
  SQL Server
  
  on Linux
  
  This guide provides instructions to create a two-node shared disk cluster for SQL Server on
  
  SUSE Linux Enterprise Server (SLES). The clustering layer is based on SU
tags:
  - "linux-operations"
  - "configure-ha-add-on-2"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

This guide provides instructions to create a two-node shared disk cluster for SQL Server on

SUSE Linux Enterprise Server (SLES). The clustering layer is based on SUSE

High Availability

Extension (HAE)

built on top of

Pacemaker

.

For more information on cluster configuration, resource agent options, management, best

practices, and recommendations, see

SUSE Linux Enterprise High Availability Extension 12

SP5

.

To complete the following end-to-end scenario, you need two machines to deploy the two

nodes cluster and another server to configure the NFS share. The following steps outline how

to configure these servers.

The first step is to configure the operating system on the cluster nodes. For this walkthrough,

use SLES with a valid subscription for the HA add-on.

1. Install and set up SQL Server on both nodes. For detailed instructions, see

Installation

guidance for SQL Server on Linux

.

2. Designate one node as primary and the other as secondary, for purposes of

configuration. Use these terms for the following this guide.

７

Note

Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES) isn't supported.
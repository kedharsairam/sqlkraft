---
title: "Run and connect - Cloud"
topic: "linux-operations"
description: "Quickstart: Run SQL Server in the cloud on Linux In this quickstart, you install SQL Server on Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), or Ubun"
tags: ["linux-operations","run-and-connect-cloud"]
pubDate: 2025-12-01
---

Quickstart: Run SQL Server in the cloud

on Linux

In this quickstart, you install SQL Server on Red Hat Enterprise Linux (RHEL), SUSE Linux

Enterprise Server (SLES), or Ubuntu in the cloud of your choice. To run SQL Server on Linux in

Azure, see

Provision a Linux virtual machine running SQL Server in the Azure portal.

If you choose to run a paid edition of SQL Server, you must bring your own license (BYOL).

1. Create a Linux AMI with at least 2 GB of memory from the marketplace:

RHEL 9

SLES v15

Ubuntu 22.04

2. Connect to the AMI by using.

3. Follow the quickstart for the Linux distribution you chose:

Red Hat Enterprise Linux

SUSE Linux Enterprise Server

Ubuntu

Windows Subsystem for Linux (WSL 2)

4. Configure for remote connections:

a. Open the

Amazon EC2 console.

b. In the navigation pane, choose.

c. Choose.

d. Add an inbound rule to allow traffic on the port on which SQL Server listens (default

TCP port 1433).

７

Note

Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES) isn't supported.

---
title: "Configure on RHEL, SLES, and Ubuntu"
topic: "linux-operations"
description: "on Linux This article describes how to create a three-node cluster on Linux using Pacemaker, and add a previously created availability group as a resource in the cluster. Fo"
tags: ["linux-operations","configure-on-rhel-sles-and-ubuntu"]
pubDate: 2025-12-01
---

on Linux

This article describes how to create a three-node cluster on Linux using Pacemaker, and add a

previously created availability group as a resource in the cluster. For high availability, an

availability group on Linux requires three nodes - see

High availability and data protection for

availability group configurations.

isn't as tightly integrated with Pacemaker on Linux as it is with Windows Server

failover clustering (WSFC). A SQL Server instance isn't aware of the cluster, and all orchestration

is from the outside in. Pacemaker provides cluster resource orchestration. Also, the virtual

network name is specific to Windows Server failover clustering; there's no equivalent in

Pacemaker. Availability group dynamic management views (DMVs) that query cluster

information return empty rows on Pacemaker clusters. To create a listener for transparent

reconnection after failover, manually register the listener name in DNS with the IP used to

create the virtual IP resource.

You can still

create a listener

for transparent reconnection after failover, but you have to

manually register the listener name in the DNS server with the IP used to create the virtual IP

resource (as explained in the following sections).

The following sections walk through the steps to set up a Pacemaker cluster and add an

availability group as resource in the cluster for high availability, for each supported Linux

distribution.

The clustering layer is based on Red Hat Enterprise Linux (RHEL)

HA add-on

built on top

of

Pacemaker.

７

Note

This article contains references to the term slave, a term that Microsoft no longer uses.

When the term is removed from the software, we remove it from this article.

Red Hat Enterprise Linux

７

Note

Access to Red Hat full documentation requires a valid subscription.

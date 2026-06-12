---
title: "Administration & maintenance"
topic: "high-availability"
description: "Maintenance tasks like adding or removing nodes from an existing Always On Failover Cluster Instance (FCI) are accomplished using the SQL Server Setup"
tags: ["high-availability","administration-maintenance"]
pubDate: 2025-12-01
---

Maintenance tasks like adding or removing nodes from an existing Always On Failover Cluster

Instance (FCI) are accomplished using the SQL Server Setup program. Other administration

tasks like changing the IP address resource, recovering from certain FCI scenarios are

accomplished using the Failover Cluster Manager snap-in, which is the management snap-in

for the Windows Server Failover Clustering (WSFC) service.

After you have installed an FCI, you can change or repair it using the SQL Server Setup

program. For example, you can add additional nodes to an FCI, run an FCI as a stand-alone

instance, or remove a node from a FCI configuration.

Setup gives you the option of maintaining an existing FCI. If you choose this option,

you can add other nodes to your FCI by running SQL Server Setup on the computer that you

want to add to the FCI. For more information, see

Create a New SQL Server Failover Cluster

(Setup)

and

Add or Remove Nodes in a SQL Server Failover Cluster (Setup).

You can remove a node from an FCI by running SQL Server Setup on the computer that you

want to remove from the FCI. Each node in an FCI is considered a peer without dependencies

on other nodes on the FCI, and you can remove any node. A damaged node does not have to

be available to be removed, and the removal process does not uninstall the SQL Server binaries

from the unavailable node. A removed node can be added back to a FCI at any time. For more

information, see

Add or Remove Nodes in a SQL Server Failover Cluster (Setup).

You should not change passwords for any of the SQL Server service accounts when an FCI node

is down or offline. If you must do this, you must reset the password again by using SQL Server

Configuration Manager when all nodes are back online.

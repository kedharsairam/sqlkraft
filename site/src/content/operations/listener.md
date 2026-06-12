---
title: "Listener"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  An availability group listener is a virtual network name (VNN) that clients can connect to in

  order to access a database in a primary or secondary rep
tags:
  - "high-availability"
  - "listener"
pubDate: 2025-12-01
---

Article

•

03/03/2023

SQL Server

An availability group listener is a virtual network name (VNN) that clients can connect to in

order to access a database in a primary or secondary replica of an Always On availability group.

A listener allows a client to connect to a replica without having to know the physical instance

name of the SQL Server. Since the listener routes traffic, the client connection string doesn't

need to be modified after a failover occurs.

An availability group listener consists of a Domain Name System (DNS) listener name, listener

port designation, and one or more IP addresses. Only the TCP protocol is supported by

availability group listener. The DNS name of the listener must be unique in the domain and in

NetBIOS. When you create a listener, it becomes a resource in a cluster with an associated

virtual network name (VNN), virtual IP (VIP), and availability group dependency. A client uses

DNS to resolve the VNN into multiple IP addresses and then tries to connect to each address,

until a connection request succeeds or until the connection requests time out.

If read-only routing is configured for one or more

readable secondary replicas

, read-intent

client connections to the listener are automatically redirected to a readable secondary replica.

This article provides an overview of an availability group listener. You can also

configure the

listener

, and then learn how to

connect to the listener.

An availability group listener uses the following:

This is also known as a Virtual Network Name (VNN). Active Directory naming rules for DNS

host names apply. For more information, see the

Naming conventions in Active Directory for

computers, domains, sites, and OUs

KB article.

VIPs are configured for one or more subnets to which the availability group can fail over.

For a given availability group listener, the IP address can use either Dynamic Host

Configuration Protocol (DHCP), or one or more static IP address. Using DHCP can cause

connectivity delays during failover, and so it is not recommended for use in production

environments. Availability groups that extend across multiple subnets, or use hybrid network

configurations, must use a static IP address.

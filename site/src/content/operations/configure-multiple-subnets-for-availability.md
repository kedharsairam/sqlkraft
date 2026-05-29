---
title: "Configure multiple subnets for availability"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  When an Always On availability group (AG) or failover cluster instance (FCI) spans more than

  one site, each site usually has its own networking, which often means t
tags:
  - "linux-operations"
  - "configure-multiple-subnets-for-availability"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

When an Always On availability group (AG) or failover cluster instance (FCI) spans more than

one site, each site usually has its own networking, which often means that each site has its own

IP addressing.

For example, the Site A addresses start with

, and the Site B addresses start with

, where

is the part of the IP address that is unique to the server. Without

some sort of routing in place at the networking layer, these servers aren't able to communicate

with each other.

There are two ways to handle this scenario:

set up a network that bridges the two different subnets (known as a VLAN)

configure routing between the subnets

: For a VLAN-based solution, each server participating in an AG or FCI needs two

network cards (NICs) for proper availability (a dual port NIC would be a single point of failure

on a physical server), so that it can be assigned IP addresses on its native subnet as well as one

on the VLAN. This requirement is in addition to any other network needs, such as iSCSI, which

also needs its own network.

The IP address creation for the AG or FCI is done on the VLAN. In the following example, the

VLAN has a subnet of

, so the IP address created for the AG or FCI is

. Nothing additional needs to be configured, since there's a single IP address

assigned to the AG or FCI.

```cmd
192.168.1.<x>
192.168.2.<x>
<x>
192.168.3.<x>
192.168.3.104
```

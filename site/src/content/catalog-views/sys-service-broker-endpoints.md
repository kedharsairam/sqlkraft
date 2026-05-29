---
name: "sys.service_broker_endpoints"
title: "sys.service_broker_endpoints"
category: "service-broker"
description: "When a route specifies next_hop_address , the network address is determined based on the network address in the name of the service. A route that specifies can specify a service name or broker instance. next_hop_address is the principal server for a database mirror, you must also specify the MIRROR_ADDRESS for the mirror server. Otherwise, this route does not automatically failover to the mirror s"
tags: ["service-broker", "catalog-view"]
pubDate: 2026-05-29
syntax: "is_message_forwarding_enabled"
---

## Description

When a route specifies next_hop_address , the network address is determined based on the network address in the name of the service. A route that specifies can specify a service name or broker instance. next_hop_address is the principal server for a database mirror, you must also specify the MIRROR_ADDRESS for the mirror server. Otherwise, this route does not automatically failover to the mirror server. next_hop_mirror_address Specifies the network address for the mirror server of a mirrored pair whose principal server is next_hop_address next_hop_mirror_address specifies a TCP/IP address in the following format: must match the port number for the Service Broker endpoint of an instance of SQL Server at the specified computer. This can be obtained by running the following query in the selected database: When the service is hosted in a mirrored database, you must also specify the

## Syntax

```sql
is_message_forwarding_enabled
```

## Remarks

When a route specifies

next_hop_address

, the network address is

determined based on the network address in the name of the service. A route that specifies

can specify a service name or broker instance.

next_hop_address

is the principal server for a database mirror, you must also specify

the MIRROR_ADDRESS for the mirror server. Otherwise, this route does not automatically

failover to the mirror server.

MIRROR_ADDRESS

next_hop_mirror_address

Specifies the network address for the mirror server of a mirrored pair whose principal server is

next_hop_address

next_hop_mirror_address

specifies a TCP/IP address in the

following format:

netbios_name

port_number

The specified

port_number

must match the port number for the Service Broker endpoint of an

instance of SQL Server at the specified computer. This can be obtained by running the

following query in the selected database:

When the MIRROR_ADDRESS is specified, the route must specify the SERVICE_NAME clause

and the BROKER_INSTANCE clause. A route that specifies

next_hop_address

might not specify a mirror address.

This option is not available in a contained database.

This option is not available in a contained database.

When the service is hosted in a mirrored database, you must also specify the

MIRROR_ADDRESS for the other instance that hosts a mirrored database. Otherwise, this route

does not fail over to the mirror.

When a route specifies

next_hop_address

, the message is delivered to a service

within the current instance of SQL Server.

When a route specifies

next_hop_address

, the network address is

determined based on the network address in the name of the service. A route that specifies

might not specify a service name or broker instance.

MIRROR_ADDRESS

next_hop_mirror_address

Specifies the network address for a mirrored database with one mirrored database hosted at

next_hop_address

next_hop_mirror_address

specifies a TCP/IP address in the following

netbios_name

port_number

The specified

port_number

must match the port number for the Service Broker endpoint of an

instance of SQL Server at the specified computer. This can be obtained by running the

following query in the selected database:

When the MIRROR_ADDRESS is specified, the route must specify the SERVICE_NAME clause

and the BROKER_INSTANCE clause. A route that specifies

next_hop_address

might not specify a mirror address.

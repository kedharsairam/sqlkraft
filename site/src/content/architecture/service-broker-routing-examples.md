---
title: "Service Broker Routing Examples"
topic: "service-broker"
description: "09/11/2025 This section presents examples of the Service Broker routing process."
tags: ["service-broker","service-broker-routing-examples"]
pubDate: 2025-12-01
---

This section presents examples of the Service Broker routing process. Each example contains sample routing

tables for

and

, and describes how Service Broker uses those routing tables to

choose a route for the message.

The routing tables presented in this topic are simplified versions of the

catalog view. The route ID

and the owner aren't important for the routing process, and all routes are considered to have an indefinite

lifetime.

A value of

in the

column matches any service name. A value of

in the

column matches any Service Broker identifier.

The examples for outgoing messages don't use the routing table in

, and the examples for incoming

messages and message forwarding don't use the routing table for.

This example describes the default configuration for Service Broker routing. By default, all databases except

contain the

route. Therefore, the routing tables for

and

contain the following information.

Column

AdventureWorks2008R2

msdb

In this case, all dialogs created in the

database are delivered to a service in the current

instance. In addition, all dialogs arriving from outside the instance are delivered to a service in the current

instance.

７

Note

The code samples in this article were tested using the

sample database, which you

can download from the

home page.

ﾉ

Expand table

```sql
AdventureWorks2008R2 msdb sys.routes
NULL remote_service_name
NULL broker_instance msdb
AdventureWorks2008R2 master
AutoCreatedLocal
AdventureWorks2008R2 msdb name
AutoCreatedLocal
AutoCreatedLocal remote_service_name
NULL
NULL broker_instance
NULL
NULL address
LOCAL
LOCAL mirror_address
NULL
NULL
AdventureWorks2008R2
AdventureWorks2022
```

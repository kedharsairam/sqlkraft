---
title: "Managing Routing"
topic: "service-broker"
description: "09/04/2025 Service Broker uses routes to determine where to deliver messages. This section describes considerations for managing routing."
tags: ["service-broker","managing-routing"]
pubDate: 2025-12-01
---

Service Broker uses routes to determine where to deliver messages. This section describes

considerations for managing routing.

By default, each user database, including

, contains the route. This

route matches any service name and broker instance and specifies that the message should be

delivered within the current instance.

has lower priority than routes that

explicitly specify the service name or broker instance.

Because

exists in

by default, Service Broker attempts to deliver all

messages from outside of the instance within the current instance. In many cases, the database

administrator restricts access to services from outside of the instance by dropping

in. The database administrator then creates a route for each service

that communicates with a remote instance.

In most cases, a route doesn't need to expire. The route remains active while the route object

exists. If the destination address for the route changes, an administrator either alters the route

to update the address or removes the route.

An application that uses dynamic routing, however, might use route expiration to ensure that

the routing information remains up to date. Service Broker doesn't remove expired routes from

the database. An application that uses route expiration should also create a SQL Server Agent

job to periodically remove route objects that have expired.

Routes

Service Broker Routing

```sql
msdb msdb msdb
```

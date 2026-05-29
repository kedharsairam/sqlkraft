---
title: "Mapping Remote Principals to Local Principals"
topic: "service-broker"
description: |
  09/11/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Service Broker dialog security uses certificates to map remote operations to a local security
  
  principal. This topic describes some of 
tags:
  - "service-broker"
  - "mapping-remote-principals-to-local-principals"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker dialog security uses certificates to map remote operations to a local security

principal. This topic describes some of the considerations involved in choosing a local principal

to map to a remote user.

Access to SQL Server resources occurs within the security context of a database principal.

Service Broker dialog security uses remote authorization to determine the local security context

(that is, the local database principal) within which messages are sent for a specific dialog. The

local security principal is determined by the certificate used for the conversation. For more

information, see

Certificates for dialog security

.

The local principal need only have

permission on the service or services that the principal

sends messages to. There's no need for the principal to have any other permissions in the

database. In particular,

permission isn't required. Therefore, remote authorization

generally uses a database principal specifically created for remote authorization. That principal

has no other permissions, and shouldn't be used for any other purpose. For a discussion of

security principals in SQL Server, see

Principals (Database Engine)

.

In general, you use one principal for each service. This helps to limit access to services. In some

cases, if your application uses a closely related set of services, you might decide to use the

same principal for all of the services. For example, if you design your application so that one

service accepts expense report submissions while another service provides status information

on expense reports, you might decide to secure both services with the same principal. In this

case, access to one service implies access to the other service, so there's no need to separate

the principals.

Dialog security can use either a database user or an application role as the local principal. Each

principal type has different characteristics. Select the type of principal that best suits the needs

of your application. In most cases, a database user without a login provides the most flexible

way to authorize remote connections while minimizing the privileges required.

```sql
SEND
CONNECT
```
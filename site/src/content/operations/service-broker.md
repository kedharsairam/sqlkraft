---
title: "Service Broker"
topic: "high-availability"
description: |
  Article

  •

  10/08/2024

  Applies to:

  SQL Server

  This topic contains information about configuring Service Broker to work with Always On

  availability groups in SQL Server.

  1.

  For more information,
tags:
  - "high-availability"
  - "service-broker"
pubDate: 2025-12-01
---

Article

•

10/08/2024

Applies to:

SQL Server

This topic contains information about configuring Service Broker to work with Always On

availability groups in SQL Server.

1.

For more information, see

Create or Configure an Availability Group Listener (SQL Server)

.

2.

On every instance of SQL Server that hosts an availability replica for the availability group,

configure the Service Broker endpoint, as follows:

Set LISTENER_IP to 'ALL'. This setting enables connections on any valid IP address

that is bound to the availability group listener.

Set the Service Broker PORT to the same port number on all the host server

instances.

The following example creates a Windows authenticated Service Broker endpoint that

uses the default Service Broker port (4022) and listens to all valid IP addresses.



Tip

To view the port number of the Service Broker endpoint on a given server

instance, query the

column of the

catalog view, where

= 'SERVICE_BROKER'.

```cmd
CREATE ENDPOINT [SSBEndpoint]
STATE = STARTED
AS TCP  (LISTENER_PORT = 4022, LISTENER_IP = ALL )
FOR SERVICE_BROKER (AUTHENTICATION = WINDOWS)
```

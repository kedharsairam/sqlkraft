---
title: "Backing Up and Restoring Service Broker Applications"
topic: "service-broker"
description: |
  09/11/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Backup and restore procedures for a Service Broker service are integrated with the database in

  which the service runs. If the service
tags:
  - "service-broker"
  - "backing-up-and-restoring-service-broker-applications"
pubDate: 2025-12-01
---

09/11/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Backup and restore procedures for a Service Broker service are integrated with the database in

which the service runs. If the service contains components outside the database such as an

external application, you must back up and restore those components separately.

The

database contains routes for incoming messages. Therefore, these routes aren't

backed up with the database that contains the service. Service Broker endpoints and

configuration for transport security are stored in the

database, so these objects also

aren't backed up with the database that contains the service.

Service Broker routing relies on a unique identifier in each database to correctly deliver

messages. When restoring a backup that is intended to replace the original database, ensure

that this identifier isn't changed. When restoring a copy of a database to a different location,

take care to change this identifier. For more information on Service Broker database identities,

see

Manage Service Broker identities

.

Migration (Service Broker)

Back up and restore of SQL Server databases

```sql
msdb
master
```

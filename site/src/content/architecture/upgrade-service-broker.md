---
title: "Upgrade (Service Broker)"
topic: "service-broker"
description: |
  09/16/2025
  
    Service Broker operations don't change when a database or an instance of the Database Engine
  
    are upgraded. The Service Broker features available in SQL Server across supported versions.
tags: ["service-broker","upgrade-service-broker"]
pubDate: "2025-12-01"
---

Service Broker operations don't change when a database or an instance of the Database Engine

are upgraded. The Service Broker features available in SQL Server across supported versions.

Databases are upgraded when the following are true:

They're attached to an instance of SQL Server Database Engine after they're detached

from an instance of a previous version of the database engine.

The instance of the database engine they're in is upgraded from a previous version.

When a SQL Server database is upgraded to a newer version, conversations continue to

operate as they did in the previous version.

ALTER DATABASE SET options (Transact-SQL)

CREATE BROKER PRIORITY (Transact-SQL)

Conversation priorities

installation guide

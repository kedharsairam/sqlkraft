---
title: "Configure"
topic: "change-data-capture"
description: |
  Applies to:

  SQL Server 2025 (17.x)

  Azure SQL Database

  Azure SQL Managed

  Instance

  This article describes how to configure the

  change event streaming (CES)

  feature introduced in

  SQL Server 2025
tags:
  - "change-data-capture"
  - "configure"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2025 (17.x)

Azure SQL Database

Azure SQL Managed

Instance

This article describes how to configure the

change event streaming (CES)

feature introduced in

SQL Server 2025 (17.x), Azure SQL Database, and Azure SQL Managed Instance.

To configure and use change event streaming, follow these steps:

1. Use an existing or create a new

Azure Event Hubs

namespace and Event Hubs instance. The

Event Hubs instance receives events.

2. Enable change event streaming for a user database.

3. Create an event stream group. With this group, configure the destination, credentials,

message size limits, and partitioning schema.

4. Add one or more tables to the event stream group.

Each step is described in detail in the following sections of this article.

To configure change event streaming, you need the following resources, permissions, and

configuration:

Azure Event Hubs namespace

Azure Event Hubs instance

７

Note

Change event streaming is currently in

for:

SQL Server 2025 (

).

Azure SQL Database (preview feature database scoped configuration not required).

Azure SQL Managed Instance (with the SQL Server 2025 or Always-up-to-date

, preview feature database scoped configuration not required). During preview,

this feature is subject to change. For current supportability, see

.

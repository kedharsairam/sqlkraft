---
title: "JSON message format"
topic: "change-data-capture"
description: |
  Applies to:

  SQL Server 2025 (17.x)

  Azure SQL Database

  Azure SQL Managed

  Instance

  This article describes the JSON format of a CloudEvents message that is streamed from SQL

  Server to Azure Event H
tags:
  - "change-data-capture"
  - "json-message-format"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2025 (17.x)

Azure SQL Database

Azure SQL Managed

Instance

This article describes the JSON format of a CloudEvents message that is streamed from SQL

Server to Azure Event Hubs when using the

change event streaming (CES)

feature introduced in

SQL Server 2025 (17.x), Azure SQL Database, and Azure SQL Managed Instance

Events emitted by change event streaming follow the

CloudEvents

specification, making them

easy to integrate with event-driven systems. All CES CloudEvents contain 11 attributes (fields).

CES can be configured to serialize CloudEvents as JSON (native), or as Avro binary. The following

sections of this article describe the message format in detail, including CES CloudEvent attributes,

and serialization.

When applicable, the descriptions in this section are taken from

CloudEvent specification

,

which includes more details.

:

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

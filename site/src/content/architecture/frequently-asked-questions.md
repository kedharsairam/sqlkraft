---
title: "Frequently asked questions"
topic: "change-data-capture"
description: |
  Applies to:
  
  SQL Server 2025 (17.x)
  
  Azure SQL Database
  
  Azure SQL Managed
  
  Instance
  
  The following are answers to questions about the Change Event Streaming (CES) feature for SQL
  
  Server 2025 (17.x),
tags:
  - "change-data-capture"
  - "frequently-asked-questions"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2025 (17.x)

Azure SQL Database

Azure SQL Managed

Instance

The following are answers to questions about the Change Event Streaming (CES) feature for SQL

Server 2025 (17.x), Azure SQL Database, and Azure SQL Managed Instance.

Yes. CES is supported in Azure SQL Database starting in November 2025.

Yes. CES relies on reading the transaction log, so the SQL Server database must be configured

with the full recovery model.

For CES, Azure Event Hubs usage is billed at standard rates. Ingress and egress charges also

apply.

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
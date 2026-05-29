---
title: "Troubleshoot extension"
topic: "azure-synapse"
description: |
  Applies to:

  SQL Server

  This article describes ways to identify unhealthy extensions that aren't installed correctly,

  running properly, or not connected to Azure.

  You can use the

  built-in extensio
tags:
  - "azure-synapse"
  - "troubleshoot-extension"
pubDate: 2025-12-01
---

Applies to:

SQL Server

This article describes ways to identify unhealthy extensions that aren't installed correctly,

running properly, or not connected to Azure.

You can use the

built-in extension health dashboard

in the Azure portal to show the health

for all deployed Azure extensions for SQL Server.

Use Azure Resource Graph to identify the state the Azure extension for SQL Server on your

Azure Arc-enabled servers.

This query returns instances of SQL Server on servers with extensions installed, but not healthy.



Tip

Create your own custom dashboard with this file from the sql-server-samples GitHub

repository:

.



Tip

If you're not already familiar, learn about Azure Resource Graph:

Quickstart: Run Resource Graph query using Azure portal

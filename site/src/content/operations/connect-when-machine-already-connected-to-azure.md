---
title: "Connect when machine already connected to Azure"
topic: "azure-synapse"
description: |
  Applies to:

  SQL Server

  This article explains how to connect your SQL Server instance to Azure Arc on an Arc-enabled

  server. For example, you need to use this method to connect a SQL Server instance
tags:
  - "azure-synapse"
  - "connect-when-machine-already-connected-to-azure"
pubDate: 2025-12-01
---

Applies to:

SQL Server

This article explains how to connect your SQL Server instance to Azure Arc on an Arc-enabled

server. For example, you need to use this method to connect a SQL Server instance to Azure

Arc at this time in US Government Virginia region, because automatic connection isn't currently

available in that region. For this case, follow the steps under

Connect

.

If the physical or virtual server isn't connected to Azure yet, follow the steps in

Connect your

SQL Server to Azure Arc

.

Verify that

is registered in each subscription. Review instructions at

Register resource providers

.

Review all of the prerequisites at

Prerequisites - SQL Server enabled by Azure Arc

.

If the machine with SQL Server is already connected to Azure Arc, to connect the SQL Server

instances, install

Azure extension for SQL Server

. The extension is in the extension tab of "Server

- Azure Arc" resource as

.

）

Important

Azure Arc automatically installs the Azure extension for SQL Server when a server

connected to Azure Arc has SQL Server installed. All the SQL Server instance resources are

automatically created in Azure, providing a centralized management platform for all your

SQL Server instances.

To automatically connect your SQL Server instances, see

.

Use the method in this article, if your server is already connected to Azure, but Azure

extension for SQL Server is not deployed automatically.

An

tag is created on the Arc machine

resource if the extension is deployed using this method.

）

Important

```cmd
Microsoft.AzureArcData
ArcSQLServerExtensionDeployment = Disabled
```

---
title: "Connect when machine not connected to Azure"
topic: "azure-synapse"
description: |
  Applies to:
  
  SQL Server
  
  This article explains how to connect your SQL Server instance to Azure Arc. Before you proceed,
  
  complete the
  
  Prerequisites - SQL Server enabled by Azure Arc
  
  .
  
  If the serve
tags:
  - "azure-synapse"
  - "connect-when-machine-not-connected-to-azure"
pubDate: 2025-12-01
---

Applies to:

SQL Server

This article explains how to connect your SQL Server instance to Azure Arc. Before you proceed,

complete the

Prerequisites - SQL Server enabled by Azure Arc

.

If the server that runs your SQL Server instance isn't yet connected to Azure, you can initiate

the connection from the target machine using the onboarding script. This script connects the

server to Azure and installs the Azure extension for SQL Server.

1. Go to

Azure Arc

in the Azure portal.

2. Under

, select

SQL Server instances

and then select

to open the

page.

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

７

Note

If your server is already connected to Azure, proceed to

.

```cmd
ArcSQLServerExtensionDeployment = Disabled
```
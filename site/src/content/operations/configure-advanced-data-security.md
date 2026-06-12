---
title: "Configure advanced data Security"
topic: "azure-synapse"
description: "You can configure your instance of SQL Server enabled by Azure Arc with Microsoft Defender for Cloud by following these steps. Your Windows-based SQL"
tags: ["azure-synapse","configure-advanced-data-security"]
pubDate: "2025-12-01"
---

You can configure your instance of SQL Server enabled by Azure Arc with Microsoft Defender

for Cloud by following these steps.

Your Windows-based SQL Server instance is connected to Azure. Follow the instructions

to

Connect your SQL Server to Azure Arc.

Your user account is assigned one of the

Security Center Roles (RBAC)

1. Search for

resource type and add a new one through the

creation pane.

2. Go to

and copy Workspace ID

and Primary key for later use.

The next step is needed only if you haven't yet configured MMA on the remote machine.

７

Note

Microsoft Defender for Cloud is only supported for SQL Server instances on

Windows machines. This will not work for SQL Server on Linux machines.

７

Note

You can use a Log Analytics workspace in any region so if you already have one, you

can use it. But we recommend creating it in the same region where your SQL Server

enabled by Azure Arc resource is created.

---
title: "Manage auto deploy"
topic: "azure-synapse"
description: |
  Applies to:

  SQL Server

  SQL Server instances are automatically connected to Azure Arc when they are installed on an

  Azure Arc-enabled Server and the Arc server resource is in a

  supported region

  .
tags:
  - "azure-synapse"
  - "manage-auto-deploy"
pubDate: 2025-12-01
---

SQL Server

instances are automatically connected to Azure Arc when they are installed on an

Azure Arc-enabled Server and the Arc server resource is in a

supported region. All the SQL Server

instance resources are automatically created in Azure, providing a centralized management

platform for all your SQL Server instances. For more information, visit

enabled by

Azure Arc.

This article details how the streamlined process of connecting SQL Server to Azure works.

1. Complete the

Prerequisites - SQL Server enabled by Azure Arc.

2. For Always On availability groups, complete the steps on all nodes.

Optionally, specify the license type for each instance of SQL Server.

To specify the desired license type, provide the license type value tag. The automatic connecting

workflow requires that tag. For more information, visit

Tag resources, resource groups, and

subscriptions for a logical organization.

The automatic connection workflow checks for the tag at the subscription level first, then

resource group level, then resource level.

７

Note

Currently, least privileged configuration is not applied by default.

Existing servers with extension version

or greater will eventually have the least

privileged configuration applied. This extension was released in November, 2024. To prevent

the automatic application of least privilege, block extension upgrades after.

```cmd
1.1.2859.223
1.1.2859.223
```

---
title: "Move resources"
topic: "azure-synapse"
description: |
  09/30/2025

  This article describes how you can move resources to a new resource group or subscription

  with SQL Server enabled by Azure Arc. The capability applies to both:

  SQL Server instances

  Data
tags:
  - "azure-synapse"
  - "move-resources"
pubDate: 2025-12-01
---

09/30/2025

This article describes how you can move resources to a new resource group or subscription

with SQL Server enabled by Azure Arc. The capability applies to both:

SQL Server instances

Databases

Before you begin, review

Known limitations

.

To complete this task, make sure that:

The

Machine - Azure Arc

resource and all SQL Server instances are in the same resource

group.

The new subscription or resource group needs to meet all

.

In addition:

If Microsoft Purview is enabled, you must disable it in the compliance portal before the

move.

If best practices assessment is enabled, you must disable it before the move.

SQL Server license and SQL Server extended security update license aren't moved

automatically.

After the move:

1. Reenable any features that you disabled.

2. Configure SQL Server license in the new location.

3. Configure ESU in the new location.

4. In the Azure portal, locate the resource group.

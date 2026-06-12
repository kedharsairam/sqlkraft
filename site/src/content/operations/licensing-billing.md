---
title: "Licensing & billing"
topic: "azure-synapse"
description: |
  This article explains how to manage licensing and billing of SQL Server enabled by Azure Arc.

  SQL Server enabled by Azure Arc directly supports only the core-based licensing methods. For

  information
tags:
  - "azure-synapse"
  - "licensing-billing"
pubDate: 2025-12-01
---

This article explains how to manage licensing and billing of SQL Server enabled by Azure Arc.

enabled by Azure Arc directly supports only the core-based licensing methods. For

information about how you can manage SQL Server instances with a Server+CAL license, see

Manage SQL Server instances with a Server+CAL license.

The full range of the licensing options is described in the

licensing guide (download

link).

You can use one of the following three licensing options. The links in the list take you to

sections in this article that provide more details.

The diagrams in the list use normalized cores (NCs) to illustrate the cost implications of the

licensing options. One core license for the Standard edition is equivalent to one NC. One core

license for the Enterprise edition is equivalent to four NCs. For more information, see

How

licenses apply to Azure resources.

License by virtual cores

Use an Enterprise or Standard license for the vCPUs (v-cores) of the virtual machine (VM)

that runs one or multiple instances of SQL Server. Each virtual machine is billed

individually for the v-cores allocated to it.

The following diagram illustrates this licensing method and the cost implications.

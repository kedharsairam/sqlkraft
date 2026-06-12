---
title: "Data collection & reporting"
topic: "azure-synapse"
description: "This article describes the data that SQL Server enabled by Azure Arc transmits to Microsoft. Specifically: SQL Server enabled by Azure Arc collects u"
tags: ["azure-synapse","data-collection-reporting"]
pubDate: "2025-12-01"
---

This article describes the data that SQL Server enabled by Azure Arc transmits to Microsoft.

Specifically:

enabled by Azure Arc collects usage data as described in this article and at

Monitor Azure Arc-enabled SQL Server.

Azure Connected Machine agent transmits this data to

as outlined in

Connected Machine agent network requirements - URLs.

enabled by Azure Arc does not collect any personally identifiable information (PII)

or end-user identifiable information or store any customer data.

enabled by Azure Arc uses the following products:

Azure Arc-enabled servers

The following data is collected for SQL Server enabled by Azure Arc instances:

Description

SQL Server edition

Resource ID of the hosting Azure Arc for Servers resource

Time when the resource was created

The number of logical processors used by the SQL Server instance

Cloud connectivity status

SQL Server update level

SQL Server collation

enabled by Azure Arc instance

ﾉ

Expand table

```cmd
*.<region>.arcdataservices.com
Edition string
ContainerResourceId string
CreateTime string
VCore string
```

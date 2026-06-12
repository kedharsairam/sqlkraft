---
title: "Register Purview"
topic: "azure-synapse"
description: "This article shows how to register an Azure Arc-enabled SQL Server instance. It also shows how to authenticate and interact with Azure Arc-enabled SQL Server in Microsoft Pur"
tags: ["azure-synapse","register-purview"]
pubDate: 2025-12-01
---

This article shows how to register an Azure Arc-enabled SQL Server instance. It also

shows how to authenticate and interact with Azure Arc-enabled SQL Server in Microsoft

Purview. For more information about Microsoft Purview, read the

introductory article.

Yes

Yes

(preview)

Yes

(preview)

Yes

(preview)

The supported SQL Server versions are 2012 and later. SQL Server Express LocalDB isn't

supported.

When you're scanning Azure Arc-enabled SQL Server, Microsoft Purview supports

extracting the following technical metadata:

Instances

Databases

Schemas

Tables, including the columns

Views, including the columns

When you're setting up a scan, you can choose to specify the database name to scan

one database. You can further scope the scan by selecting tables and views as needed.

The whole Azure Arc-enabled SQL Server instance will be scanned if you don't provide a

database name.

ﾉ

Expand table

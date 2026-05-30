---
title: "Managed identity overview"
topic: "azure-synapse"
description: |
  Applies to:

  SQL Server 2025 (17.x)

  SQL Server 2025 (17.x) includes managed identity support for SQL Server on Windows. Use a

  managed identity to interact with resources in Azure by using Microsoft
tags:
  - "azure-synapse"
  - "managed-identity-overview"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2025 (17.x)

SQL Server 2025 (17.x) includes managed identity support for SQL Server on Windows. Use a

managed identity to interact with resources in Azure by using Microsoft Entra authentication.

SQL Server 2025 (17.x) introduces support for

Microsoft Entra managed identities

. Use

managed identities to authenticate to Azure services without needing to manage credentials.

Managed identities are automatically managed by Azure and can be used to authenticate to

any service that supports Microsoft Entra authentication. With SQL Server 2025 (17.x), you can

use managed identities both to authenticate inbound connections, and also to authenticate

outbound connections to Azure services.

When you connect your SQL Server instance to Azure Arc, a system-assigned managed identity

is automatically created for the SQL Server hostname. After the managed identity is created,

you must associate the identity with the SQL Server instance and the Microsoft Entra tenant ID

by updating the registry.

For step-by-step setup instructions, see

Set up managed identity for SQL Server enabled by

Azure Arc

.

When using managed identity with SQL Server enabled by Azure Arc, consider the following:

The managed identity is assigned at the Azure Arc server level.

Only system-assigned managed identities are supported.

SQL Server uses this Azure Arc server level managed identity as the

.

SQL Server can use this primary managed identity in either

and/or

connections.

are logins and users connecting to SQL Server. Inbound

connections can also be achieved by using

App registration

, starting in SQL Server

2022 (16.x).

are SQL Server connections to Azure resources, like backup to

URL, or connecting to Azure Key Vault.

App Registration

enable a SQL Server to make outbound connections. Outbound

connections need a primary managed identity assigned to the SQL Server.

```cmd
inbound outbound
Inbound connections
Outbound connections
```

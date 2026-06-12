---
title: "Managed identity for Extensible Key Management"
topic: "azure-synapse"
description: "2025 (17.x) This article shows you how to use managed identities for Extensible Key Management (EKM) with Azure Key Vault (AKV) on SQL Server enabled by Azure Arc . Starti"
tags: ["azure-synapse","managed-identity-for-extensible-key-management"]
pubDate: 2025-12-01
---

2025 (17.x)

This article shows you how to use managed identities for Extensible Key Management (EKM)

with Azure Key Vault (AKV) on

enabled by Azure Arc.

Starting with SQL Server 2025 (17.x), managed identities are supported for EKM with AKV and

Managed Hardware Security Modules (HSM) on SQL Server enabled by Azure Arc. Managed

identities are the recommended authentication method to allow different Azure services to

authenticate the SQL Server enabled by Azure Arc resource without using passwords or secrets.

For more information on managed identities, see

Managed identity types.

Connect the instance of SQL Server to Azure Arc. For more information, see

Automatically

connect your SQL Server to Azure Arc.

Enable managed identity for SQL Server 2025.

An Azure Key Vault and key created in the key vault. For more information, see

Create a

key vault.

The managed identity for the SQL Server enabled by Azure Arc needs to have the

role assigned to the key vault if you're using

Azure

role-based access control

or the

Unwrap Key

and

Wrap Key

permissions if you're using

vault access policy.

Download and install the preview version of the SQL Server Connector.

Before you can create a credential using a managed identity, you need to add a registry key to

enable the EKM provider to use managed identities. This step needs to be performed by the

computer administrator. For detailed steps, see

Step 4: Add registry key to support EKM

provider.

1. Open SQL Server Management Studio.

```cmd
Key
Vault Crypto Service Encryption User
```

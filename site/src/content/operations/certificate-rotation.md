---
title: "Certificate rotation"
topic: "azure-synapse"
description: |
  08/28/2025

  Applies to:

  SQL Server

  On SQL Server enabled by Azure Arc, Azure extension for SQL Server can automatically rotate

  certificates for Microsoft Entra ID for service managed certificates a
tags:
  - "azure-synapse"
  - "certificate-rotation"
pubDate: 2025-12-01
---

08/28/2025

Applies to:

SQL Server

On SQL Server enabled by Azure Arc, Azure extension for SQL Server can automatically rotate

certificates for Microsoft Entra ID for service managed certificates and service managed app

registration. For customer managed certificates and customer managed app registration, you

can follow the steps to rotate the certificate used for Microsoft Entra ID.

This article explains how automatic certificate rotation and customer managed certificate

rotation works and identifies the process specifics for Windows and Linux operating systems.

You can enable either:

Service managed certificate rotation

or

Customer managed certificate rotation

Azure Key Vault automatically rotates the certificate for you. Key vault rotates certificates by

default, after the certificate lifetime is at 80%. You can configure this setting. For instructions,

review

Configure certificate auto-rotation in Key Vault

. If the certificate has expired, then the

automatic rotation fails.

The functionality described in this article applies to an instance of SQL Server enabled by Azure

Arc configured for authentication with Microsoft Entra ID. For instructions to configure such an

instance, see:

Microsoft Entra authentication for SQL Server

With service managed certificate rotation, the Azure Extension for SQL Server rotates the

certificates.

７

Note

was previously known as Azure Active Directory (Azure AD).

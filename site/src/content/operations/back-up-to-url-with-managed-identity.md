---
title: "Back up to URL with managed identity"
topic: "azure-synapse"
description: |
  SQL Server enabled by Azure Arc

  Applies to:

  SQL Server 2025 (17.x)

  This article describes how to use a managed identity to back up and restore databases with

  Azure Blob storage using

  SQL Server e
tags:
  - "azure-synapse"
  - "back-up-to-url-with-managed-identity"
pubDate: 2025-12-01
---

enabled by Azure Arc

2025 (17.x)

This article describes how to use a managed identity to back up and restore databases with

Azure Blob storage using

enabled by Azure Arc.

For SQL Server on Azure VMs, review

Backup and restore to URL using managed identities.

To back up and restore databases with Azure Blob storage using managed identities, you need

the following:

2025 enabled by Azure Arc

that's been assigned a

primary managed identity.

An

Azure Blob storage account.

Valid network access to the Azure Blob storage and Windows Firewall permissions on the

host to allow the outbound connection, and valid storage account service endpoints.

The primary managed identity for the SQL Server instance needs to have the

role assigned to the storage account.

The primary managed identity for the SQL Server instance needs to have the

role assigned to the storage account. This role allows the managed identity

to write to and read from the storage account.

Use the Azure portal to check the permissions assigned to the managed identity by following

these steps:

1. Go to your

Storage account

in the Azure portal.

2. Select

to open the

pane.

3. On the

pane, select

to view the list of users and

groups that have been assigned roles for the storage account.

4. Filter by the

role and verify that you see the managed

identity for your SQL Server instance listed:

```cmd
Storage
Blob Data Contributor
Storage Blob
Data Contributor
Storage Blob Data Contributor
```

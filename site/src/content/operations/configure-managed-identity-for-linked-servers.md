---
title: "Configure managed identity for linked servers"
topic: "azure-synapse"
description: ": SQL Server 2025 (17.x) SQL Server 2025 introduces managed identity support for linked servers, enabling secure, credential-free authentication between SQL Server instances."
tags: ["azure-synapse","configure-managed-identity-for-linked-servers"]
pubDate: "2025-12-01"
---

:

2025 (17.x)

2025 introduces managed identity support for linked servers, enabling secure,

credential-free authentication between SQL Server instances. This capability is available for

both SQL Server on Azure Virtual Machines and SQL Server enabled by Azure Arc. With

managed identity authentication, you can establish linked server connections without

managing passwords or storing credentials, improving your security posture and simplifying

credential management.

This article shows you how to set up linked server connections using managed identity

authentication. You'll configure the source server to initiate connections and the destination

server to accept managed identity-based authentication.

Before you begin, ensure you have the following:

2025 running on either:

Azure Virtual Machine with SQL Server IaaS Agent extension installed, or

On-premises or virtual machine with Azure Arc enabled

Microsoft Entra authentication configured on both source and destination servers

Network connectivity between source and destination servers with appropriate firewall

rules

Appropriate permissions to create logins and configure linked servers on both instances

For Azure Virtual Machines: Both

SqlIaasExtension

and

AADLogin

extensions enabled

For Azure Arc-enabled instances: Azure Arc agent installed and configured

When using SQL Server on Azure Virtual Machines:

Verify that

SqlIaasExtension

and

AADLogin

extensions are installed. These extensions are

included by default when deploying from the Azure Marketplace SQL Server template.

Configure Microsoft Entra authentication following the guidance in

Enable Microsoft

Entra authentication for SQL Server on Azure VMs.

Ensure both virtual machines allow inbound and outbound network traffic for SQL Server

communication.

Configure firewall rules on each virtual machine to permit SQL Server traffic.

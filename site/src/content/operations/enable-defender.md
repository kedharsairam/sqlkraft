---
title: "Enable Defender"
topic: "azure-synapse"
description: |
  09/21/2025
  
    The Defender for SQL Servers on Machines plan is one of the Defender for Databases plans in
  
    Microsoft Defender for Cloud. Use Defender for SQL Servers on Machines to protect SQL
  
    virtual
tags: ["azure-synapse","enable-defender"]
pubDate: "2025-12-01"
---

The Defender for SQL Servers on Machines plan is one of the Defender for Databases plans in

Microsoft Defender for Cloud. Use Defender for SQL Servers on Machines to protect SQL

virtual machines (VM) and Azure Arc SQL Server instances.

: To deploy the plan on a subscription, including Azure Policy,

you need

permissions.

instance permissions

: SQL Server service accounts must be a member of the

fixed server role on each SQL Server instance, which is the default setting. Learn

more about the

service account requirement.

:

SQL virtual machines

, and

Azure Arc SQL Server instances

are supported.

On-premises machines must be

onboarded to Arc and registered as Azure Arc SQL

Server instances.

: Allow outbound HTTPS traffic on Transmission Control Protocol (TCP) port

443 using Transport Layer Security (TLS) to

URL. Learn more

about

URL requirements.

: Ensure these extensions aren't blocked in your environment. Learn more

about

restricting extensions installation on Windows VMs.

）

Important

This article applies to commercial clouds. If you're using Government clouds, see the

article.

）

Important

The Defender for SQL Servers on Machines plan is undergoing a transition to the new

agent architecture. For more information, see.

```cmd
*.<region>.arcdataservices.com
```

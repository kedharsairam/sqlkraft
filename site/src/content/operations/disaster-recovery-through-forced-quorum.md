---
title: "Disaster Recovery through Forced Quorum"
topic: "high-availability"
description: ""
tags: ["high-availability","disaster-recovery-through-forced-quorum"]
pubDate: "2025-12-01"
---

Quorum failure is usually caused by a systemic disaster, or a persistent communications failure,

or a misconfiguration involving several nodes in the WSFC cluster. Manual intervention is

required to recovery from a quorum failure.

,

Security

WSFC Disaster

Recovery through the Forced Quorum Procedure

The Forced Quorum Procedure assumes that a healthy quorum existed before the quorum

failure.

The user must be a domain account that is member of the local Administrators group on each

node of the WSFC cluster.

２

Warning

The user should be well-informed on the concepts and interactions of Windows Server

Failover Clustering, WSFC Quorum Models, SQL Server, and the environment's specific

deployment configuration.

For more information, see:

,

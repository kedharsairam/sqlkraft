---
title: "Replication components fail after an upgrade"
topic: "io-fundamentals"
description: "2025 (17.x)"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

2025 (17.x)

This article describes the breaking changes to features in the SQL Server Database Engine

introduced with SQL Server 2025 (17.x). These changes can break applications, scripts, or

functionalities that are based on earlier versions of SQL Server.

2025 (17.x) includes changes to

encryption

that introduce a breaking change to

linked servers. These changes can break applications, scripts, or functionalities that are based

on earlier versions of SQL Server.

When you upgrade from previous versions of SQL Server to SQL Server 2025 (17.x) with

Microsoft OLE DB Driver 19, existing linked server configurations might fail. Different default

values for the encryption parameter might cause this failure unless a valid certificate is

provided.

In SQL Server 2025 (17.x):

Linked servers to instances of SQL Server 2025 must use the Encrypt parameter in the

connection string

When you migrate from previous editions of SQL Server to SQL Server 2025 with

Microsoft OLE DB Driver 19, existing linked server configurations can fail

For information about how to connect securely to SQL Server 2025 (17.x) instances, see

TDS

8.0.

2025 (17.x) includes changes to

encryption

that introduce a breaking change to

Transactional

,

Snapshot

,

Peer-to-peer

, and

Merge

replication.

Replication components might fail after an upgrade to SQL Server 2025 (17.x) from all previous

versions of SQL Server, if your SQL Server instance:

Is configured as a replication publisher.

Has a remote distributor in the replication topology.

Isn't configured with a trusted certificate.

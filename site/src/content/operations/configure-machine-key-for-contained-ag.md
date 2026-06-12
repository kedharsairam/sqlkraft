---
title: "Configure machine key for contained AG"
topic: "linux-operations"
description: |
  07/03/2025

  Applies to:

  SQL Server

  - Linux

  This article provides an example of how to prepare a machine key for SQL Server running on

  Linux in a contained availability group (AG).

  A

  contained AG
tags:
  - "linux-operations"
  - "configure-machine-key-for-contained-ag"
pubDate: 2025-12-01
---

07/03/2025

SQL Server

- Linux

This article provides an example of how to prepare a machine key for SQL Server running on

Linux in a contained availability group (AG).

A

contained AG

is an availability group that supports:

Managing metadata objects (users, logins, permissions, SQL Server Agent jobs, and so on)

at the AG level in addition to the instance level.

Specialized contained system databases within the AG.

The examples in this article target SQL Server in Linux containers, but you can use the same

steps for SQL Server on Linux, running on physical machines, virtual machines, and in a

Kubernetes-based deployment.

In SQL Server on Linux, the machine key plays a vital role in securing communication and data.

The following table describes its primary functions.

Description

The machine key is used to encrypt and decrypt data exchanged between

nodes in an AG

Ｕ

Caution

These instructions should only be used for

contained availability groups. When you

configure a contained AG with a common machine key across all replicas, first ensure

there's no existing encryption hierarchy (for example, transparent data encryption,

column-level encryption, or any other security-related feature that requires key

management). Changing the machine key could break the encryption and cause data loss.

After configuration, avoid creating or modifying the encryption hierarchy for security

reasons.

ﾉ

Expand table

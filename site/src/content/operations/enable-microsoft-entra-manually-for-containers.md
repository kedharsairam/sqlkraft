---
title: "Enable Microsoft Entra manually for containers"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This tutorial walks you through manually enabling Microsoft Entra ID authentication for SQL

  Server running in containers. Because Azure Arc doesn't currently suppor
tags:
  - "linux-operations"
  - "enable-microsoft-entra-manually-for-containers"
pubDate: 2025-12-01
---

SQL Server

on Linux

This tutorial walks you through manually enabling Microsoft Entra ID authentication for SQL

Server running in containers. Because Azure Arc doesn't currently support

container workloads

for this scenario, you can configure Microsoft Entra ID authentication directly, for standalone

containers and Kubernetes deployments.

For all other deployment scenarios, you should configure Microsoft Entra ID authentication

through Azure Arc.

Microsoft Entra ID is configured for your tenant.

can reach Microsoft Entra ID endpoints.

A Microsoft Entra application is registered.

Follow the directions in

Tutorial: Set up Microsoft Entra authentication for SQL Server with

app registration

, and upload the certificate to the created registered application, that you

create in the first step of the tutorial.

A supported SQL Server Linux container image.

Access to Docker or a Kubernetes cluster with.

Deployment models require:

1. A certificate associated with the Microsoft Entra application

2. SQL Server configured with:

Certificate path

Microsoft Entra application (client) ID

Microsoft Entra tenant ID

```cmd
kubectl
```

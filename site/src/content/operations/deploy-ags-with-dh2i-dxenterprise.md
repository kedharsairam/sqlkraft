---
title: "Deploy AGs with DH2i DxEnterprise"
topic: "linux-operations"
description: "- Linux This tutorial explains how to configure SQL Server Always On availability groups (AGs) for SQL Server Linux based containers deployed to an A"
tags: ["linux-operations","deploy-ags-with-dh2i-dxenterprise"]
pubDate: "2025-12-01"
---

- Linux

This tutorial explains how to configure SQL Server Always On availability groups (AGs) for SQL

Server Linux based containers deployed to an Azure Kubernetes Service (AKS) Kubernetes

cluster, using DH2i DxEnterprise. You can choose between a

sidecar configuration

(preferred),

or build your own custom container image.

Using the steps mentioned in this article, learn how to deploy a StatefulSet and use the

DH2i DxEnterprise solution to create and configure an AG. This tutorial consists of the

following steps.

This tutorial shows an example of an AG with three replicas. You need:

An Azure Kubernetes Service (AKS) or Kubernetes cluster.

A valid DxEnterprise license with AG features and tunnels enabled. For more

information, see the

developer edition

for nonproduction usage, or

DxEnterprise

software

for production workloads.

７

Note

Microsoft supports data movement, AG, and SQL Server components. DH2i is responsible

for support of the DxEnterprise product, which includes cluster and quorum management.

Sidecar configuration

Create a headless service configuration

＂

Create a StatefulSet configuration with SQL Server and DxEnterprise in the same pod

as a sidecar container

＂

Create and configure a SQL Server AG, adding the secondary replicas

＂

Create a database in the AG, and test failover

＂

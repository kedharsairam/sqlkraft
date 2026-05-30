---
title: "Configure a Kubernetes cluster"
topic: "linux-operations"
description: |
  Quickstart: Deploy a SQL Server container

  Applies to:

  SQL Server

  on Linux

  This quickstart demonstrates how to configure a highly available SQL Server instance in a

  container with persistent stora
tags:
  - "linux-operations"
  - "configure-a-kubernetes-cluster"
pubDate: 2025-12-01
---

Quickstart: Deploy a SQL Server container

Applies to:

SQL Server

on Linux

This quickstart demonstrates how to configure a highly available SQL Server instance in a

container with persistent storage, on Azure Kubernetes Service (AKS) or Red Hat OpenShift. If the

SQL Server instance fails, the orchestrator automatically re-creates it in a new pod. The cluster

service also provides resiliency against a node failure.

This quickstart uses the following command line tools to manage the cluster.

Azure Kubernetes Service (AKS)

kubectl

(Kubernetes CLI)

Azure Red Hat OpenShift

oc

(OpenShift CLI)

An Azure account with an active subscription.

Create an account for free

.

A Kubernetes cluster. For more information on creating and connecting to a

Kubernetes cluster in AKS with

, see

Deploy an Azure Kubernetes Service (AKS)

cluster

.

Azure CLI. See

How to install the Azure CLI

to install the latest version.

ﾉ

Expand table

Kubernetes

７

Note

To protect against node failure, a Kubernetes cluster requires more than one node.

```cmd
kubectl
```

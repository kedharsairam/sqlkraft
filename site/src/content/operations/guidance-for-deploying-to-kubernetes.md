---
title: "Guidance for deploying to Kubernetes"
topic: "linux-operations"
description: "on Linux This article contains best practices and guidance for running SQL Server containers on Kubernetes with StatefulSets. We recommend deploying one SQL Server container"
tags: ["linux-operations","guidance-for-deploying-to-kubernetes"]
pubDate: 2025-12-01
---

on Linux

This article contains best practices and guidance for running SQL Server containers on

Kubernetes with StatefulSets. We recommend deploying one SQL Server container (instance) per

pod in Kubernetes. Thus, you have one SQL Server instance deployed per pod in the Kubernetes

cluster.

Similarly, the deployment script recommendation is to deploy one SQL Server instance by setting

the

value to. If you enter a number greater than

as the

value, you get

that many SQL Server instances with correlated names. For example, in the below script, if you

assigned the number

as the value for

, you would deploy two SQL Server pods, with

the names

and

respectively.

Another reason we recommend one SQL Server per deployment script is to allow changes to

configuration values, edition, trace flags, and other settings to be made independently for each

instance deployed.

In the following example, the StatefulSet workload name should match the

value, which in this case is. For more information, see

StatefulSets.

）

Important

The

environment variable is deprecated. Use

instead.

```cmd
replicas
1
1 replicas
2
```

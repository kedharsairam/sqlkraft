---
title: "Deploy AGs with DH2i DxOperator"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This tutorial explains how to configure SQL Server Always On availability groups (AGs) for SQL

  Server Linux based containers deployed to an Azure Kubernetes Service
tags:
  - "linux-operations"
  - "deploy-ags-with-dh2i-dxoperator"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

This tutorial explains how to configure SQL Server Always On availability groups (AGs) for SQL

Server Linux based containers deployed to an Azure Kubernetes Service (AKS) cluster, using

DH2i DxOperator. These procedures are also applicable to Azure Red Hat OpenShift clusters;

the primary distinction is the deployment of an

Azure Red Hat OpenShift cluster

, followed by

substituting

commands with

in the following steps.

Microsoft supports data movement, AG, and SQL Server components. DH2i is responsible

for support of the DxEnterprise product, which includes cluster and quorum management.

DxOperator is a software extension to Kubernetes that uses custom resource definitions

to automate the deployment of DxEnterprise clusters. DxEnterprise then provides all of

the instrumentation to create, configure, manage and provide automatic failover for SQL

Server AG workloads in Kubernetes. You can register for a

free DxEnterprise software

license

. For more information, see the

DxOperator Quick Start Guide

.

Using the steps mentioned in this article, learn how to deploy a StatefulSet and use the DH2i

DxOperator to create and configure an AG with three replicas, hosted on AKS.

This tutorial consists of the following steps:

An Azure Kubernetes Service (AKS) or Kubernetes cluster.

A valid DxEnterprise license with AG features and tunnels enabled. For more information,

see the

developer edition

for nonproduction usage, or

DxEnterprise software

for

production workloads.

Create a

object on AKS cluster with mssql-conf settings

＂

Install DxOperator

＂

Create a secret objects

＂

Deploy 3 replica SQL AG using YAML file

＂

Connect to SQL Server

＂

```cmd
kubectl oc configmap
```

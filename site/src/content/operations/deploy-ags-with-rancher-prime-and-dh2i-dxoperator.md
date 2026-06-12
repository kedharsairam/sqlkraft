---
title: "Deploy AGs with Rancher Prime and DH2i DxOperator"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This tutorial provides instructions on setting up SQL Server configured with Always On

  availability groups (AGs) in an Azure Kubernetes Service (AKS) cluster. It ut
tags:
  - "linux-operations"
  - "deploy-ags-with-rancher-prime-and-dh2i-dxoperator"
pubDate: 2025-12-01
---

SQL Server

on Linux

This tutorial provides instructions on setting up SQL Server configured with Always On

availability groups (AGs) in an Azure Kubernetes Service (AKS) cluster. It utilizes the DH2i

DxOperator and Rancher Prime from SUSE for deployment.

Microsoft supports data movement, AG, and SQL Server components. DH2i is responsible for

support of the DxEnterprise product, which includes cluster and quorum management.

This tutorial consists of the following steps:

An

Azure Kubernetes Service

(AKS) or Kubernetes cluster.

７

Note

Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES) isn't supported.

７

Note

DxOperator is a software extension to Kubernetes that uses custom resource definitions to

automate the deployment of DxEnterprise clusters. DxEnterprise then provides all of the

instrumentation to create, configure, manage, and provide automatic failover for SQL

Server AG workloads in Kubernetes. You can register for a. For more information, see the. For support

issues, contact SUSE directly.

Configure Rancher Prime on AKS

＂

Install DxOperator

＂

Deploy SQL Server containers and configure the always on availability groups using the

DH2i DxOperator

＂

Connect and manage SQL Server containers using SQL Server Management Studio (SSMS).

＂

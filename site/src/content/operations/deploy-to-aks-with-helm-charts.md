---
title: "Deploy to AKS with Helm charts"
topic: "linux-operations"
description: ""
tags: ["linux-operations","deploy-to-aks-with-helm-charts"]
pubDate: "2025-12-01"
---

Quickstart: Deploy a SQL Server Linux

on Linux

This quickstart takes you through the steps to deploy SQL Server on Linux containers to

Azure

Kubernetes Service

(AKS) with

Helm charts

, from a Windows client machine.

AKS is a managed Kubernetes service for deploying and managing container clusters.

Helm

is an open-source packaging tool that helps you install and manage the lifecycle of Kubernetes

applications.

An Azure subscription. If you don't have an Azure subscription, you can create a

free

account.

Create an AKS cluster.

Download and review the sample

Helm chart

for this quickstart. The sample chart

contains many configuration options for customizing your SQL Server deployment.

On your Windows client machine, you need the following tools.

Azure CLI

for Windows.

Helm

for Windows.

If you prefer to use a different client operating system, you need to select the appropriate

packages for that platform.

You use

to interact with the Kubernetes cluster. For more information, see

az aks

install-cli.

To install

, run the following command from your Windows command prompt:

Windows Command Prompt

```cmd
az aks install-cli
```

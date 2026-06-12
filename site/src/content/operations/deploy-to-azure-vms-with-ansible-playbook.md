---
title: "Deploy to Azure VMs with Ansible playbook"
topic: "linux-operations"
description: |
  Quickstart: Deploy SQL Server on Linux

  Applies to:

  SQL Server

  on Linux

  This quickstart takes you through the steps to automate a SQL Server on Linux deployment on

  Azure Virtual Machines, using an
tags:
  - "linux-operations"
  - "deploy-to-azure-vms-with-ansible-playbook"
pubDate: 2025-12-01
---

Quickstart: Deploy SQL Server on Linux

SQL Server

on Linux

This quickstart takes you through the steps to automate a SQL Server on Linux deployment on

Azure Virtual Machines, using an

Ansible

playbook.

Ansible

is an open-source product that automates cloud provisioning, configuration

management, and application deployments.

Ansible playbooks

allow you to direct Ansible to configure your environment. Playbooks are

coded using YAML so as to be human-readable.

An Azure subscription. If you don't have an Azure subscription, you can create a

free

account.

Create a new

resource group

using Azure CLI, which contains three Azure Virtual

Machines:

Create an Azure VM

, running Red Hat Enterprise Linux (RHEL) 8.5 or higher. This virtual

machine (VM) becomes the

controller node.

Create an Azure VM

, running RHEL, to serve as the first

managed node.

Create an Azure VM

, running Ubuntu Server, to serve as the second

managed node.

The first VM, where you configure Ansible Core, is the controller node. On this node, you install

the SQL Server

system role.

The remaining VMs are the target machines, also known as

managed nodes

, for deploying and

configuring SQL Server using the system role.

Starting with RHEL 8.x on Azure VMs, the

package can be installed from the

preconfigured AppStream repository. You can install Ansible Core on the controller node using

the following command:

```cmd
ansible-core
```

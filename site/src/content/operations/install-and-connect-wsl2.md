---
title: "Install and connect (WSL2)"
topic: "linux-operations"
description: ""
tags: ["linux-operations","install-and-connect-wsl2"]
pubDate: 2025-12-01
---

Quickstart: Install SQL Server and create a

on Linux

Use the Windows Subsystem for Linux (WSL) to run a Linux environment directly on your

Windows machine, without the need for a virtual machine or dual booting. WSL provides a

seamless and productive experience for developers who want to use both Windows and Linux

simultaneously. For more information, see

What is the Windows Subsystem for Linux?

on WSL 2 is intended for development purposes only, and is

supported for

production workloads. Run SQL Server in WSL environments on one of the

supported platforms

,

for the version of SQL Server you intend to run.

For any support related issues, you can

obtain support from Microsoft.

There are two ways to get started with SQL Server on WSL 2:

Install SQL Server as a

service, which you can then manage with

commands. Make sure that you enable

on WSL. For more information, see

How to

enable systemd.

Deploy SQL Server containers in WSL. For this option, you need to install a Linux container

engine in WSL, such as Docker or Podman, and then deploy SQL Server containers.

Install WSL 2. Ensure you're running Windows 10 version 2004 or a later version (Build 19041 and

higher), or Windows 11. To install WSL, open a PowerShell or Windows command prompt in

administrator mode, and follow the instructions in the next section.

on WSL is for development use only

```cmd
systemd systemctl systemd
```

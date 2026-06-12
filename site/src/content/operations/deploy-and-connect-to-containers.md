---
title: "Deploy and connect to containers"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This article explains how to deploy and connect to SQL Server Linux containers.

  For other deployment scenarios, see:

  Windows

  Linux

  Container cluster on Azure

  Th
tags:
  - "linux-operations"
  - "deploy-and-connect-to-containers"
pubDate: 2025-12-01
---

SQL Server

on Linux

This article explains how to deploy and connect to SQL Server Linux containers.

For other deployment scenarios, see:

Windows

Linux

Container cluster on Azure

This article specifically focuses on using the

image. SQL Server deployments

in Windows containers aren't covered by support. For development and testing, you can create

your own custom container images to work with SQL Server in Windows containers. Sample files

are available on

GitHub. Sample files are for reference only.

This 6-minute video provides an introduction into running SQL Server on containers:

７

Note

container images are supported only on Linux hosts running on. Emulation or translation environments (for example, Rosetta 2, Prism, or

QEMU) aren't tested or supported. If you want to create a feature request, or report an

emulator-related issue, visit the.

）

Important

Before choosing to run a SQL Server container for production use cases, review the

to ensure that you're running on a supported

configuration.

https://channel9.msdn.com/Shows/Data-Exposed/SQL-Server-2019-in-Containers/player?

WT.mc_id=dataexposed-c9-niner&nocookie=true&locale=en-

us&embedUrl=%2Fsql%2Flinux%2Fsql-server-linux-docker-container-deployment

```cmd
mssql-server-linux
```

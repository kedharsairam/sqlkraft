---
title: "Container security"
topic: "linux-operations"
description: "on Linux SQL Server 2017 (14.x) containers start up as the root user by default, which can cause some security concerns. This article talks about security options that you h"
tags: ["linux-operations","container-security"]
pubDate: 2025-12-01
---

on Linux

2017 (14.x) containers start up as the root user by default, which can cause some

security concerns. This article talks about security options that you have when running SQL Server

Linux containers, and how to build a SQL Server container as a non-root user.

The examples in this article assume that you're using Docker, but you can apply the same

principles to other container orchestration tools including Kubernetes.

Follow these steps to build a SQL Server 2017 (14.x) container that starts up as the

(non-

root) user.

1. Download the

sample Dockerfile for non-root SQL Server containers

and save it as.

2. Run the following command in the context of the dockerfile directory to build the non-root

container:

3. Start the container.

７

Note

Containers for SQL Server 2019 (15.x) and later versions automatically start up as non-root,

while SQL Server 2017 (14.x) containers start as root by default. For more information on

running SQL Server containers as non-root, see.

）

Important

The

environment variable is deprecated. Use

instead.

```cmd
mssql dockerfile cd
<path to dockerfile>
docker build -t 2017-latest-non-root.
SA_PASSWORD
MSSQL_SA_PASSWORD
```

---
title: "Troubleshoot containers"
topic: "linux-operations"
description: "on Linux This article talks about common errors seen when deploying and using SQL Server Docker containers, and provide troubleshooting techniques to help resolve the issue."
tags: ["linux-operations","troubleshoot-containers"]
pubDate: "2025-12-01"
---

on Linux

This article talks about common errors seen when deploying and using SQL Server Docker

containers, and provide troubleshooting techniques to help resolve the issue.

If you get errors for any

commands, make sure that the docker service is running, and

try to run with elevated permissions.

For example, on Linux, you might get the following error when running

commands:

Output

If you get this error on Linux, try running the same commands prefaced with. If that fails,

verify the docker service is running, and start it if necessary.

Bash

On Windows, verify that you're launching PowerShell or your command-prompt as an

Administrator.

If the SQL Server container fails to run, try the following tests:

If you get an error such as

, you're

attempting to map the container port 1433 to a port that is already in use. This can

happen if you're running SQL Server locally on the host machine. It can also happen if you

start two SQL Server containers and try to map them both to the same host port. If this

）

Important

The

environment variable is deprecated. Use

instead.

container startup errors

```cmd
docker docker sudo failed to create endpoint CONTAINER_NAME on network bridge.
Error starting proxy: listen tcp 0.0.0.0:1433 bind: address already in use.
Cannot connect to the Docker daemon. Is the docker daemon running on this host?
sudo systemctl status docker sudo systemctl start docker
```

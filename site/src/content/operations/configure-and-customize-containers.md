---
title: "Configure and customize containers"
topic: "linux-operations"
description: "on Linux This article explains how you can configure and customize SQL Server Linux containers using Docker."
tags: ["linux-operations","configure-and-customize-containers"]
pubDate: 2025-12-01
---

on Linux

This article explains how you can configure and customize SQL Server Linux containers using

Docker. You can persist your data, move files from and to containers, and change default settings.

You can create your own

Dockerfile

to build a customized SQL Server container. For more

information, see

a demo that combines SQL Server and a Node application. If you do create

your own Dockerfile, be aware of the foreground process, because this process controls the life of

the container. If it exits, the container shuts down. For example, if you want to run a script and

start SQL Server, make sure that the SQL Server process is the right-most command. All other

commands are run in the background. The following command illustrates this inside a Dockerfile:

If you reversed the commands in the previous example, the container would shut down when the

do-my-sql-commands.sh script completes.

Your SQL Server configuration changes and database files are persisted in the container even if

you restart the container with

and. However, if you remove the

container with

, everything in the container is deleted, including SQL Server and your



Tip

You can use

(Go) to create a new instance of SQL Server in a container for

development purposes. For more information, see.

```cmd
docker stop docker start docker rm sqlcmd
/usr/src/app/
do
-my-sql-commands.sh & /opt/mssql/bin/sqlservr
```

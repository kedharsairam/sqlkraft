---
title: "Install SQL Server Java Language Extension"
topic: "linux-operations"
description: "07/11/2025 SQL Server 2019 (15.x) - Linux and later versions Learn how to install the Java Language Extension component for SQL Server on Linux. The Java Language Extension is part o"
tags: ["linux-operations","install-sql-server-java-language-extension"]
pubDate: "2025-12-01"
---

2019 (15.x) - Linux and later versions

Learn how to install the

Java Language Extension

component for SQL Server on Linux. The Java

Language Extension is part of

Language Extensions

and an add-on to the Database

Engine.

Although you can

install the Database Engine and Language Extensions concurrently

, it's a best

practice to install and configure the SQL Server Database Engine first so that you can resolve

any issues before adding more components.

The Linux version must be

supported by SQL Server

, but doesn't include the Docker

Engine. Supported versions include:

Red Hat Enterprise Linux

(RHEL)

SUSE Linux Enterprise Server

(SLES)

Ubuntu

You should have a tool for running Transact-SQL (T-SQL) commands. A query editor is

necessary for post-install configuration and validation. We recommend the

MSSQL

extension for Visual Studio Code

, which is a free download that runs on Linux.

Language Extensions is also supported on Linux containers. We don't provide prebuilt

containers with Language Extensions, but you can create one from the SQL Server

containers using

an example template available on GitHub.

Language Extensions and

Machine Learning Services

are installed by default on SQL

Server Big Data Clusters. If you use Big Data Clusters, you don't need to follow the steps

in this article. For more information, see

Run Python and R scripts with Machine Learning

Services on SQL Server 2019 Big Data Clusters.

On an internet-connected device, packages are downloaded and installed independently of the

Database Engine using the package installer for each operating system. The following table

describes all available packages.

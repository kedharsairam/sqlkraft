---
title: "Install client tools"
topic: "high-availability"
description: "Client tools such as SQL Server Management Studio are shared features common across all instances on the same machine. They are backward compatible, w"
tags: ["high-availability","install-client-tools"]
pubDate: "2025-12-01"
---

Client tools such as SQL Server Management Studio are shared features common across all

instances on the same machine. They are backward compatible, with supported SQL Server

versions that can be installed side by side. Only one version of the client tool exists on a node

at a time.

If the SQL Server client tools are installed during setup on first node of the SQL Server cluster,

they are automatically added to any nodes that may be added later to the instance of SQL

Server using Add Node.

If you do not install the SQL Server client tools during the initial installation of the SQL Server

cluster, you can install it later as described in the procedures below.

1. Insert the SQL Server installation media. From the root installation folder, double-click

Setup.exe. To install from the network share, locate the root folder on the share, and then

double-click Setup.exe.

2. On the

page, click. Do not click.

3. The system configuration checker verifies the system state of your computer before Setup

will continue.

4. On the

page, click.

）

Important

Books Online is not automatically added to the additional nodes added to the

cluster using Add Node. SQL Server Books Online can be installed manually on

the nodes that you wish to have a local copy of SQL Server Books Online.

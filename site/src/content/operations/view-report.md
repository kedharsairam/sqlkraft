---
title: "View report"
topic: "high-availability"
description: "This topic explains how to view the Transaction Log Shipping Status report in SQL Server Management Studio. You can run a status report at a monitor s"
tags: ["high-availability","view-report"]
pubDate: 2025-12-01
---

This topic explains how to view the Transaction Log Shipping Status report in SQL Server

Management Studio. You can run a status report at a monitor server, primary server, or

secondary server. To see the most complete information about your log shipping configuration,

view the report at the monitor server instance.

The report displays the status of any log shipping activity whose status is available from the

server instance to which you are connected. If that server instance is involved in multiple

configurations in different roles (such as serving as a monitor for one database and a

secondary for another database), the displayed results contain the information of every

configuration from the perspective of each role. If the stored procedure can connect to the

monitor server instance for a given log shipping configuration, the report displays additional

status for that configuration.

For each role performed by the current server instance, you can view the following information:

Monitor

The name and status of every primary server and secondary server that uses this server

instance as its monitor server.

Primary

For each primary database, the status and name of the current server instance (as the

primary server), along with the primary database name. The report displays the status of the

backup job (which is stored locally on the primary server).

The report also contains a row for each of the corresponding secondary servers. If the

configuration uses a monitor server and the stored procedure can connect to the monitor,

these rows display the copy status and restore status for the most recent log backup.

Secondary

For each secondary database, the status and name of the current server instance (as the

secondary server), along with the secondary database name.

The report displays the status of the copy and restore jobs at the secondary server.

The report also contains a row for the corresponding primary server. If the configuration

uses a monitor server and the stored procedure can connect to the monitor, this row

displays the status of the most recent log backup.

ﾉ

Expand table

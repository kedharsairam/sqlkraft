---
title: "Status Page"
topic: "high-availability"
description: ""
tags: ["high-availability","status-page"]
pubDate: "2025-12-01"
---

This read-only page displays the most recent mirroring status for the principal and mirror

server instances of the database currently selected in the navigation tree. If information about

an instance is currently unavailable, some of the cells in the

grid corresponding to that

instance are grayed out and display.

Start Database Mirroring Monitor (SQL Server Management Studio)

Displays a grid containing the most recent high-level mirroring status of each of the principal

and mirror server instances. The rows of the

grid are in the following order:

Principal server instance

Mirror server instance

The columns are as follows:

Description

Name of the server instance whose status is displayed in the

row.

Current role of the server instance, either

or.

The mirroring state reported by the server instance and an icon that indicates the severity

of the state. The possible statuses and their associated icons are as follows:

Icon: -, status. The monitor is not connected to either partner. The only

available information is what has been cached by the monitor.

Icon: Warning icon, status. The contents of the mirror database are lagging

behind the contents of the principal database. The principal server instance is sending log

records to the mirror server instance, which is applying the changes to the mirror

database to roll it forward. At the start of a database mirroring session, the mirror and

ﾉ

Expand table

---
title: "Set Warning Thresholds"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  Use this dialog box to enable and configure one or more warning thresholds for the database

  selected in the navigation tree of the

  dialog box.

  The d
tags:
  - "high-availability"
  - "set-warning-thresholds"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

Use this dialog box to enable and configure one or more warning thresholds for the database

selected in the navigation tree of the

dialog box.

The dialog box tries to connect to both server instances. These connections are established

asynchronously. The dialog shows the connection status of each partner. If the partner is not

connected, you can click

.

Start Database Mirroring Monitor (SQL Server Management Studio)

Server instance and its connection status

Name of a partner server instance in the form

SYSTEM

\*\*\*\*

INSTANCE_NAME

. For a default

server instance, only the system name is displayed.

This field also indicates whether the monitor is currently connected to this server instance. The

possible connection statuses are:

server_instance_name

server_instance_name

server_instance_name

The name of each of the partner server instances is displayed in a separate

Server instance and

its connection status

field. The top field lists the principal server when the monitor started

running.

/

A

/

button is associated with each

Server instance and its connection status

fields. The state of the button depends on the connection status:

７

Note

If you do are not a member of the

fixed server role, this status is

server_instance_name

.

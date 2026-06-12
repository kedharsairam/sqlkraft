---
title: "Wizard"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  Use the Add Database to Availability Group Wizard to help you add one or more databases to

  an existing Always On availability group.

  If you have neve
tags:
  - "high-availability"
  - "wizard-2"
pubDate: 2025-12-01
---

Article

•

03/03/2023

SQL Server

Use the Add Database to Availability Group Wizard to help you add one or more databases to

an existing Always On availability group.

If you have never added a database to an availability group, see the "Availability Databases"

section in

Prerequisites, Restrictions, and Recommendations for Always On Availability Groups

(SQL Server).

You must be connected to the server instance that hosts the current primary replica.

Prerequisites for using full initial data synchronization

All the database-file paths must be identical on every server instance that hosts a

replica for the availability group.

No primary database name can exist on any server instance that hosts a secondary

replica. This means that none of the new secondary databases can exist yet.

You will need to specify a network share in order for the wizard to create and access

backups. For the primary replica, the account used to start the Database Engine must

have read and write file-system permissions on a network share. For secondary

replicas, the account must have read permission on the network share.

If you are unable to use the wizard to perform full initial data synchronization, you need

to prepare your secondary databases manually. You can do this before or after running

the wizard. For more information, see

Manually Prepare a Secondary Database for an

Availability Group (SQL Server).

７

Note

For information about using Transact-SQL or PowerShell to add a database, see.

Prerequisites, Restrictions, and Recommendations

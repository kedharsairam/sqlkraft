---
title: "Transaction log shipping page"
topic: "collation"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Use this page to configure and modify the properties of log shipping for a database.

  For an explanation of log shipping concepts, see

  About Log Shipp
tags:
  - "collation"
  - "transaction-log-shipping-page"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Use this page to configure and modify the properties of log shipping for a database.

For an explanation of log shipping concepts, see

About Log Shipping (SQL Server).

Enables this database as a log shipping primary database. Select it and then configure the

remaining options on this page. If you clear this check box, the log shipping configuration will

be dropped for this database.

Click

to configure backup schedule, location, alert, and archiving parameters.

Shows the currently selected backup schedule for the primary database. Click

to modify these settings.

Indicates the time and date of the last transaction log backup of the primary database.

Lists the currently configured secondary servers and databases for this primary database.

Highlight a database, and then click

to modify the parameters associated with that

secondary database.

Click

to add a secondary database to the log shipping configuration for this primary

database.

Removes a selected database from this log shipping configuration. Select the database first

and then click.

Sets up a monitor server instance for this log shipping configuration. Select the

check box and then click

to specify the monitor server instance.

---
title: "Configure Publishing & Distribution"
topic: "migration"
description: "This topic describes how to configure publishing and distribution in SQL Server by using SQL Server Management Studio, Tra"
tags: ["migration","configure-publishing-distribution"]
pubDate: 2025-12-01
---

This topic describes how to configure publishing and distribution in SQL Server by using SQL

Server Management Studio, Transact-SQL, or Replication Management Objects (RMO).

For more information, see

View and modify replication security settings.

Configure distribution using the New Publication Wizard or the Configure Distribution Wizard.

After the Distributor is configured, view and modify properties in the

dialog box. Use the Configure Distribution Wizard if you want to configure a

Distributor so that members of the

fixed database roles can create publications, or

because you want to configure a remote Distributor that is not a Publisher.

1. In Microsoft SQL Server Management Studio, connect to the server that will be the

Distributor (in many cases, the Publisher and Distributor are the same server), and then

expand the server node.

2. Right-click the

folder, and then click.

3. Follow the Configure Distribution Wizard to:

Select a Distributor. To use a local Distributor, select. To use a remote

Distributor, select

, and then select a server.

The server must already be configured as a Distributor, and the Publisher must be

enabled to use the Distributor. For more information, see

Enable a Remote Publisher at a

Distributor (SQL Server Management Studio).

If you select a remote Distributor, you must enter a password on the

page for connections made from the Publisher to the Distributor. This

```cmd
db_owner
```

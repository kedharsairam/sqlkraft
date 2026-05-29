---
title: "Installation Wizard (Setup)"
topic: "upgrade"
description: |
  06/03/2025
  
  Applies to:
  
  SQL Server
  
  - Windows only
  
  The SQL Server Installation Wizard provides a single feature tree for an in-place upgrade of
  
  SQL Server components to the latest version of SQL Se
tags:
  - "upgrade"
  - "installation-wizard-setup"
pubDate: 2025-12-01
---

06/03/2025

Applies to:

SQL Server

- Windows only

The SQL Server Installation Wizard provides a single feature tree for an in-place upgrade of

SQL Server components to the latest version of SQL Server.

For many production and some development environments, a new installation upgrade or a

rolling upgrade is more appropriate than an in-place upgrade. For more information regarding

upgrade methods, see:

Choose a Database Engine upgrade method

Upgrade Data Quality Services

Upgrade Integration Services

Upgrade Master Data Services

Upgrade and migrate Reporting Services

Upgrade Analysis Services

Upgrade Power Pivot for SharePoint

.

You must run Setup as an administrator. If you install SQL Server from a remote share, you

must use a domain account that has read and execute permissions on the remote share, and is

a local administrator.

２

Warning

When you upgrade SQL Server, the previous version of SQL Server is overwritten, and no

longer exists on your computer. Before upgrading, back up SQL Server databases and

other objects associated with the previous SQL Server instance.

２

Warning

You can't change the features to be upgraded, and you can't add features during the

upgrade operation. For more information about how to add features to an upgraded

instance of SQL Server after the upgrade operation is complete, see

.
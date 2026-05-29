---
title: "Change Tracking page"
topic: "collation"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  Use this page to view or modify change tracking settings for the selected database. For more

tags:
  - "collation"
  - "change-tracking-page"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Use this page to view or modify change tracking settings for the selected database. For more

information about the options available on this page, see

Enable and Disable Change Tracking

(SQL Server)

.

Use to enable or disable change tracking for the database.

To enable change tracking, you must have permission to modify the database.

Setting the value to

sets a database option that allows change tracking to be enabled on

individual tables.

You can also configure change tracking by using

ALTER DATABASE

.

Specifies the minimum period for keeping change track information in the database. Data is

removed only if the

value is

.

The default value is 2.

Specifies the units for the Retention Period value. You can select

,

, or

. The

default value is

.

The minimum retention period is 1 minute. There is no maximum retention period.

Indicates whether change tracking information is automatically removed after the specified

retention period.

Enabling

resets any previous custom retention period to the default retention

period of 2 days.

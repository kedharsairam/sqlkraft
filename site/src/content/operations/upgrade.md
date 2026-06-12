---
title: "Upgrade"
topic: "high-availability"
description: |
  Article

  •

  04/15/2024

  Applies to:

  SQL Server

  When upgrading a SQL Server mirrored instance to a new version, to a new SQL Server service

  pack or cumulative update, or to a new Windows service pac
tags:
  - "high-availability"
  - "upgrade"
pubDate: 2025-12-01
---

Article

•

04/15/2024

SQL Server

When upgrading a SQL Server mirrored instance to a new version, to a new SQL Server service

pack or cumulative update, or to a new Windows service pack or cumulative update, you can

reduce downtime for each mirrored database to only a single manual failover by performing a

rolling upgrade (or two manual failovers if failing back to the original primary). A rolling

upgrade is a multi-stage process that in its simplest form involves upgrading the SQL Server

instance that is currently acting as the mirror server in a mirroring session, then manually

failing over the mirrored database, upgrading the former principal SQL Server instance, and

resuming mirroring. In practice, the exact process will depend on the operating mode and the

number and layout of mirroring session running on the SQL Server instances that you are

upgrading.

Before you begin, review the following important information:

Supported Version and Edition Upgrades

: Verify that you can upgrade to SQL Server from

your version of the Windows operating system and version of SQL Server. For example,

you cannot upgrade directly from a SQL Server 2005 instance to the latest version of SQL

Server.

Choose a Database Engine Upgrade Method

: Select the appropriate upgrade method and

steps based on your review of supported version and edition upgrades and also based on

other components installed in your environment to upgrade components in the correct

order.

Plan and Test the Database Engine Upgrade Plan

: Review the release notes and known

upgrade issues, the pre-upgrade checklist, and develop and test the upgrade plan.

Hardware and Software Requirements for Installing SQL Server 2016

: Review the software

requirements for installing SQL Server. If additional software is required, install it on each

node before you begin the upgrade process to minimize any downtime.

７

Note

For information on using database mirroring with log shipping during a migration,

download this.

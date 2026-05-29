---
title: "From SQL Server (upgrade)"
topic: "migration"
description: |
  In this guide, you learn how to upgrade your user databases from previous versions of SQL Server

  to SQL Server 2025 (17.x) by using the SQL Server migration component in SQL Server

  Management Studio
tags:
  - "migration"
  - "from-sql-server-upgrade"
pubDate: 2025-12-01
---

In this guide, you learn how to upgrade your user databases from previous versions of SQL Server

to SQL Server 2025 (17.x) by using the SQL Server migration component in SQL Server

Management Studio (SSMS).

For other migration guides, see

Azure Database Migration

.

Before beginning your migration project, address the associated prerequisites. Learn about the

supported versions and considerations for

upgrading SQL Server

.

To prepare for the migration, use the

SQL Server migration component in SSMS

.

Once you confirm that the source environment is supported and you address any prerequisites,

you can start the premigration stage. The process involves conducting an inventory of the

databases that you need to migrate. The next step is to assess the SQL Server instances. To assess

your source database, use the

SQL migration component in SQL Server Management Studio

before upgrading your SQL Server instance. After all database assessments are complete, select

to export the results to a JSON file for analyzing the data at your own convenience.

Next, review the reports for potential migration issues or blockers, and resolve any items that

were uncovered.

When you have the necessary prerequisites in place and complete the tasks associated with the

premigration stage, you're ready to complete the schema and data migration. A successful

migration and upgrade means you addressed all the issues discovered during the premigration

stage.

Review the preparation steps for migration of your databases and logins using

SQL Server

migration component in SQL Server Management Studio

.

Preserve backup logs, maintenance plans, and other automated tasks, including jobs, by creating

a backup of the system

database msdb

.

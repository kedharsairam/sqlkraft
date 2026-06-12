---
name: "Use hierarchyid columns in replicated tables"
title: "Use hierarchyid columns in replicated tables"
category: "statements"
description: "If a user type with conflicting name exists during the upgrade, no special steps are taken. After"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

## One-directional replication

## Bi-directional replication

If a user type with conflicting name exists during the upgrade, no special steps are taken. After

the upgrade, both the old user type and the new system type exist. The user type is available

only through two-part names.

Columns of type

can be used on any replicated table. The requirements for your

application depend on whether replication is one directional or bidirectional, and on the

versions of SQL Server that are used.

One-directional replication includes snapshot replication, transactional replication, and merge

replication in which changes aren't made at the Subscriber. How

columns work

with one directional replication depends on the version of SQL Server the Subscriber is

running.

A SQL Server Publisher can replicate

columns to a SQL Server Subscriber of

the same version without any special considerations.

A SQL Server Publisher must convert

columns to replicate them to a

Subscriber that's running SQL Server Compact or an earlier version of SQL Server. SQL

Server Compact and earlier versions of SQL Server don't support

columns. If

you're using one of these versions, you can still replicate data to a Subscriber. To do this,

you must set a schema option or the publication compatibility level (for merge

replication) so the column can be converted to a compatible data type.

Column filtering is supported in both of these scenarios. This includes filtering out

columns. Row filtering is supported as long as the filter doesn't include a

column.

Bi-directional replication includes transactional replication with updating subscriptions, peer-

to-peer transactional replication, and merge replication in which changes are made at the

Subscriber. Replication lets you configure a table with

columns for bi-directional

replication. Note the following requirements and considerations.

The Publisher and all Subscribers must be running the same version, on SQL Server 2016

(13.x) or a later version.

Replication replicates the data as bytes and doesn't perform any validation to assure the

integrity of the hierarchy.

The hierarchy of the changes that were made at the source (Subscriber or Publisher) isn't

maintained when they replicate to the destination.

The values for

columns can have identical binary representations across all

databases. Conflicts can occur in bi-directional replication when application logic

independently generates the same

for different entities. Therefore, the same

value could be generated on the Publisher and Subscriber, but it could be applied to

different rows. Replication doesn't check for this condition, and there's no built-in way to

partition

column values as there's for

columns. Applications must

use constraints or other mechanisms to avoid such undetected conflicts.

It's possible that rows that are inserted on the Subscriber can be orphaned. The parent

row of the inserted row might be deleted at the Publisher. This results in an undetected

conflict when the row from the Subscriber is inserted at the Publisher.

Column filters can't filter out non-nullable

columns. Inserts from the

Subscriber fail because there's no default value for the

column on the

Publisher.

Row filtering is supported as long as the filter doesn't include a

column.

Hierarchical data (SQL Server)

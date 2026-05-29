---
name: "sys.sysusers"
title: "sys.sysusers"
category: "security"
description: "Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Contains one row for each Microsoft Windows user, Windows group, Microsoft SQL Server user, or SQL Server role in the database. User ID, unique in this database. Overflows or returns NULL if the number of users and roles exceeds Identified for informational purposes only. Not supported. Future compatibility is not guarantee"
tags: ["security", "catalog-view"]
pubDate: 2026-05-29
syntax: "SELECT * FROM sys.sysusers"
---

## Description

Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Contains one row for each Microsoft Windows user, Windows group, Microsoft SQL Server user, or SQL Server role in the database. User ID, unique in this database. Overflows or returns NULL if the number of users and roles exceeds Identified for informational purposes only. Not supported. Future compatibility is not guaranteed.

## Syntax

```sql
SELECT * FROM sys.sysusers
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Many of the system tables from earlier releases of SQL Server are now implemented as a set of views. These views are known as compatibility views, and they are meant for backward compatibility only. The compatibility views expose the same metadata that was available in SQL Server 2000 (8.x). However, the compatibility views do not expose any of the metadata related to features that are introduced in SQL Server 2005 (9.x) and later. Therefore, when you use new features, such as Service Broker or partitioning, you must switch to using the catalog views. Another reason for upgrading to the catalog views is that compatibility view columns that store user IDs and type IDs may return NULL or trigger arithmetic overflows. This is because you can create more than 32,767 users, groups, and roles, and 32,767 data types. For example, if you were to create 32,768 users, and then run the following query: . If ARITHABORT is set to ON, the query fails with an arithmetic overflow error. If ARITHABORT is set to OFF, the column returns NULL. To avoid these problems, we recommend that you use the new catalog views that can handle the increased number of user IDs and type IDs. The following table lists the columns that are subject to this overflow. SQL Server 2005 view ﾉ Expand table

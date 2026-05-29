---
title: 'Discontinued features in SQL Server 2022 (16.x)'
topic: 'query-processing'
description: 'This article describes the Database Engine features that are no longer available in SQL Server.'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

This article describes the Database Engine features that are no longer available in SQL Server.

Data Quality Services (DQS) is

removed

in SQL Server 2025 (17.x). We continue to support

DQS in SQL Server 2022 (16.x) and earlier versions.

Master Data Services (MDS) is

removed

in SQL Server 2025 (17.x). We continue to support

MDS in SQL Server 2022 (16.x) and earlier versions.

Synapse Link is discontinued in this version of SQL Server. Use

Mirroring in Fabric

instead.

For more information, see

Mirroring in Fabric – What's new

.

Purview access policies (DevOps policies and data owner policies) are discontinued in SQL

Server 2025 (17.x). Use

Fixed server-level roles

instead.

In place of the

SQL Performance Monitoring

Purview policy action, use the

and/or

fixed server roles.

In place of

SQL Security Auditing

Purview policy action, use the

and/or

fixed

server roles.

Use the

server role with existing logins, to connect to a

database without the need to create a user in that database.

The following Machine Learning Services packages are no longer included with

installation of SQL Server 2022 (16.x). Instead, you can install any custom packages as

desired. For more information, see

What's new in SQL Server Machine Learning Services?

ﾉ

Expand table

```sql
##MS_ServerPerformanceStateReader##
```

```sql
##MS_PerformanceDefinitionReader##
```

```sql
##MS_ServerSecurityStateReader##
```

```sql
##MS_SecurityDefinitionReader##
```

```sql
##MS_DatabaseConnector##
```

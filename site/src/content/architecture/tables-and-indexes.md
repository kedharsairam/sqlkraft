---
title: "tables and indexes"
topic: "index-architecture"
description: "DB provider, thereby limiting users to only those data sources referenced by linked server"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

DB provider, thereby limiting users to only those data sources referenced by linked server

names defined by the administrators. By default, ad hoc access is enabled for the SQL Server

OLE DB provider, and disabled for all other OLE DB providers.

Distributed queries can allow users to access another data source (for example, files, non-

relational data sources such as Active Directory, and so on) using the security context of the

Microsoft Windows account under which the SQL Server service is running. SQL Server

impersonates the login appropriately for Windows logins; however, that isn't possible for SQL

Server logins. This can potentially allow a distributed query user to access another data source

for which they don't have permissions, but the account under which the SQL Server service is

running does have permissions. Use

to define the specific logins that are

authorized to access the corresponding linked server. This control isn't available for ad hoc

names, so use caution in enabling an OLE DB provider for ad hoc access.

When possible, SQL Server pushes relational operations such as joins, restrictions, projections,

sorts, and group by operations to the OLE DB data source. SQL Server doesn't default to

scanning the base table into SQL Server and performing the relational operations itself. SQL

Server queries the OLE DB provider to determine the level of SQL grammar it supports, and,

based on that information, pushes as many relational operations as possible to the provider.

SQL Server specifies a mechanism for an OLE DB provider to return statistics indicating how key

values are distributed within the OLE DB data source. This lets the SQL Server Query Optimizer

better analyze the pattern of data in the data source against the requirements of each

Transact-SQL statement, increasing the ability of the Query Optimizer to generate optimal

execution plans.

SQL Server 2008 (10.0.x) improved query processing performance on partitioned tables for

many parallel plans, changes the way parallel and serial plans are represented, and enhanced

the partitioning information provided in both compile-time and run-time execution plans. This

article describes these improvements, provides guidance on how to interpret the query

execution plans of partitioned tables and indexes, and provides best practices for improving

query performance on partitioned objects.

７

Note

`sp_addlinkedsrvlogin`

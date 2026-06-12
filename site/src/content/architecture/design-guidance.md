---
title: "Design guidance"
topic: "filestream"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Azure Synapse Analytics

  Analytics Platform System (PDW)

  SQL database in Microsoft

  Fabric

  High-level recommendations for des
tags:
  - "filestream"
  - "design-guidance"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

High-level recommendations for designing columnstore indexes. A few good design decisions

help you achieve the high data compression and query performance that columnstore indexes

are designed to provide.

This article assumes you are familiar with columnstore architecture and terminology. For more

information, see

Columnstore indexes: Overview

and

Columnstore Index Architecture.

Before designing a columnstore index, understand as much as possible about your data

requirements. For example, think through the answers to these questions:

How large is my table?

Do my queries mostly perform analytics that scan large ranges of values? Columnstore

indexes are designed to work well for large range scans rather than looking up specific

values.

Does my workload perform lots of updates and deletes? Columnstore indexes work well

when the data is stable. Queries should be updating and deleting less than 10% of the

rows.

Do I have fact and dimension tables for a data warehouse?

Do I need to perform analytics on a transactional workload? If so, see the

columnstore

design guidance for real-time operational analytics.

You might not need a columnstore index. Rowstore (or B-tree) tables with heaps or clustered

indexes perform best on queries that seek into the data, searching for a particular value, or for

queries on a small range of values. Use rowstore indexes with transactional workloads since

they tend to require mostly table seeks instead of large range table scans.

A columnstore index is either clustered or nonclustered. A clustered columnstore index can

have one or more nonclustered B-tree indexes. Columnstore indexes are easy to try. If you

---
name: "Examples: Microsoft Fabric Data Warehouse"
title: "Examples: Microsoft Fabric Data Warehouse"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

## I. Query data as of a point in time

## J. SELECT statement with a label in the OPTION clause

The following example prevents the pushdown of the

clause to the MapReduce job on

the external Hadoop table. All rows are returned to PDW where the

clause is applied.

For more information, see

FOR TIMESTAMP query hint.

Use the

## syntax in the

clause to query data as it existed in the past, in Fabric

Data Warehouse. The following sample query returns data as it appeared on March 13, 2024 at

7:39:35.28 PM UTC. The time zone is always in UTC.

The following example shows a

statement with a label in the

clause. For more

information, see

Query labels in Fabric Data Warehouse.

Query hints (Transact-SQL)

SELECT (Transact-SQL)

UPDATE (Transact-SQL)

MERGE (Transact-SQL)

DELETE (Transact-SQL)

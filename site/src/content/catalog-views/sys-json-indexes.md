---
name: "sys.json_indexes"
title: "sys.json_indexes"
category: "indexes"
description: "SQL Server 2025 (17.x) Preview Contains a row per json index. Indicates that array search optimization is enabled for JSON index. 1 = Array search optimization is enabled for JSON index. 0 = Array search optimization isn't enabled for JSON indexes. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For"
tags: ["indexes", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  DROP
  TABLE
  IF
  EXISTS
  dbo.Customers;
  CREATE
  TABLE
  dbo.Customers
  (
  customer_id
  INT
  IDENTITY
  PRIMARY
  KEY
  ,
  customer_info
  JSON
  NOT
  NULL
  );
  CREATE
  JSON
  INDEX
  CustomersJsonIndex
  ON
  dbo.Customers (customer_info);
  INSERT
  INTO
  dbo.Customers (customer_info)
---

## Description

SQL Server 2025 (17.x) Preview Contains a row per json index. Indicates that array search optimization is enabled for JSON index. 1 = Array search optimization is enabled for JSON index. 0 = Array search optimization isn't enabled for JSON indexes. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see

## Syntax

```sql
DROP
TABLE
IF
EXISTS dbo.Customers;
CREATE
TABLE dbo.Customers (
customer_id
INT
IDENTITY
PRIMARY
KEY
,
customer_info
JSON
NOT
NULL
);
CREATE
JSON
INDEX
CustomersJsonIndex
ON dbo.Customers (customer_info);
INSERT
INTO dbo.Customers (customer_info)
```

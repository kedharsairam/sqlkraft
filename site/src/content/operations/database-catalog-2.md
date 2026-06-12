---
title: "Database catalog"
topic: "monitor"
description: "Explanations for the schemas, tables, and stored procedures in the WideW"
tags: ["monitor","database-catalog-2"]
pubDate: "2025-12-01"
---

Analytics

Platform System (PDW)

Explanations for the schemas, tables, and stored procedures in the WideWorldImportersDW

database.

The WideWorldImportersDW database is used for data warehousing and analytical processing.

The transactional data about sales and purchases is generated in the WideWorldImporters

database, and loaded into the WideWorldImportersDW database using a.

The data in WideWorldImportersDW thus mirrors the data in WideWorldImporters, but the

tables are organized differently. While WideWorldImporters has a traditional normalized

schema, WideWorldImportersDW uses the

star schema

approach for its table design. Besides

the fact and dimension tables, the database includes a number of staging tables that are used

in the ETL process.

The different types of tables are organized in three schemas.

Description

Dimension

Dimension tables.

Fact

Fact tables.

Integration

Staging tables and other objects needed for ETL.

The dimension and fact tables are listed below. The tables in the Integration schema are used

only for the ETL process, and are not listed.

WideWorldImportersDW has the following dimension tables. The description includes the

relationship with the source tables in the WideWorldImporters database.

ﾉ

Expand table

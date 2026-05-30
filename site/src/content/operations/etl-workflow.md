---
title: "ETL workflow"
topic: "monitor"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Use the

  WWI_Integration

  ETL package to migrate data from the WideWorldImporters database

  to the WideWorldImportersDW database as
tags:
  - "monitor"
  - "etl-workflow"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Use the

WWI_Integration

ETL package to migrate data from the WideWorldImporters database

to the WideWorldImportersDW database as data changes. The package is run periodically

(usually daily).

The package ensures high performance by using SQL Server Integration Services to orchestrate

bulk T-SQL operations (instead of separate transformations in Integration Services).

Dimensions are loaded first, and then Fact tables are loaded. You can rerun the package any

time after a failure.

The workflow looks like this:

The workflow starts with an expression task that determines the appropriate cutoff time. The

cutoff time is the current time minus a few minutes. (This approach is more robust than

requesting data right to the current time.) Any milliseconds are truncated from the time.

The main processing starts by populating the Date dimension table. The processing ensures

that all dates for the current year have been populated in the table.

Next, a series of data flow tasks loads each dimension. Then, they load each fact.

---
title: "SQL Server features"
topic: "monitor"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure Synapse Analytics

  Analytics

  Platform System (PDW)

  WideWorldImportersDW is designed to showcase many of the key features of
tags:
  - "monitor"
  - "sql-server-features-2"
pubDate: 2025-12-01
---

Article

•

03/03/2023

SQL Server

Azure SQL Database

Azure Synapse Analytics

Analytics

Platform System (PDW)

WideWorldImportersDW is designed to showcase many of the key features of SQL Server that

are suitable for data warehousing and analytics. The following is a list of SQL Server features

and capabilities, and a description of how they are used in WideWorldImportersDW.

[Applies to SQL Server (2016 and later)]

PolyBase is used to combine sales information from WideWorldImportersDW with a public data

set about demographics to understand which cities might be of interest for further expansion

of sales.

To enable the use of PolyBase in the sample database, make sure it is installed, and run the

following stored procedure in the database:

This will create an external table

that references a public data

set that contains population data for cities in the United States, hosted in Azure Blob Storage.

You are encouraged to review the code in the stored procedure to understand the

configuration process. If you want to host your own data in Azure Blob Storage and keep it

secure from general public access, you will need to undertake additional configuration steps.

The following query returns the data from that external data set:

```cmd
dbo.CityPopulationStatistics
EXECUTE
[Application].[Configuration_ApplyPolyBase]
SELECT
CityID, StateProvinceCode, CityName,
YearNumber, LatestRecordedPopulation
FROM dbo.CityPopulationStatistics;
```

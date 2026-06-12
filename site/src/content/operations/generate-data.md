---
title: "Generate data"
topic: "monitor"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  Azure SQL Database

  The released versions of the WideWorldImporters and WideWorldImportersDW databases have

  data from January 1, 2013, up to the day t
tags:
  - "monitor"
  - "generate-data"
pubDate: 2025-12-01
---

Article

•

03/03/2023

SQL Server

Azure SQL Database

The released versions of the WideWorldImporters and WideWorldImportersDW databases have

data from January 1, 2013, up to the day that the databases were generated.

When you use these sample databases, you might want to include more recent sample data.

To generate sample data up to the current date:

1. If you haven't done so, install a clean version of the WideWorldImporters database. For

installation instructions, see

Installation and configuration.

2. Execute the following statement in the database:

This statement adds sample sales and purchase data to the database, up to the current

date. It displays the progress of the data generation by day. Because of a random factor

in the data generation, there are some differences in the data that's generated between

runs.

To increase or decrease the amount of data generated for orders per day, change the

value for the parameter. Use the parameters

and

to

determine the order volume for weekend days.



Tip

Forcing

on the database may improve data generation speed,

particularly when the database transaction log is on a high latency storage subsystem. Be

```cmd
@AverageNumberOfCustomerOrdersPerDay
@SaturdayPercentageOfNormalWorkDay
@SundayPercentageOfNormalWorkDay
EXECUTE DataLoadSimulation.PopulateDataToCurrentDate
@AverageNumberOfCustomerOrdersPerDay = 60,
@SaturdayPercentageOfNormalWorkDay = 50,
@SundayPercentageOfNormalWorkDay = 0,
@IsSilentMode = 1,
@AreDatesPrinted = 1;
```

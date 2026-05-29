---
title: "Query store page"
topic: "collation"
description: |
  Article
  
  •
  
  10/09/2024
  
  Applies to:
  
  SQL Server 2016 (13.x) and later versions, SQL Database
  
  Access this page from the principal database, and use it to configure and to modify the
  
  properties of the
tags:
  - "collation"
  - "query-store-page"
pubDate: 2025-12-01
---

Article

•

10/09/2024

Applies to:

SQL Server 2016 (13.x) and later versions, SQL Database

Access this page from the principal database, and use it to configure and to modify the

properties of the database Query Store. These options can also be configure by using the

ALTER DATABASE SET options

. For information about the Query Store, see

Monitoring

Performance By Using the Query Store

.

Operation Mode

Valid values are OFF, READ_ONLY, and READ_WRITE. OFF disables the Query Store. In

READ_WRITE mode, the Query Store collects and persists query plan and runtime execution

statistics information. In READ_ONLY mode, information can be read from the Query Store, but

new information is not added. If the maximum allocated space of the Query Store has been

exhausted, the Query Store will change its operation mode to READ_ONLY.

Operation Mode (Actual)

Gets the actual operation mode of the Query Store.

Operation Mode (Requested)

Gets and sets the desired operation mode of the Query Store.

Data Flush Interval (Minutes)

Determines the frequency at which data written to the Query Store is persisted to disk. To

optimize for performance, data collected by the Query Store is asynchronously written to the

disk. The frequency at which this asynchronous transfer occurs is configured.

Statistics Collection Interval

Gets and sets the statistics collection interval value.

Max Size (MB)

Gets and sets the total space allocated to the Query Store.

Query Store Capture Mode

None does not capture new queries.

All captures all queries.

Auto captures queries based on resource consumption.
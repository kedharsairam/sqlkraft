---
title: "srv_willconvert"
topic: "clr-integration"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Determines whether a specific data type conversion is available within the ODS Library.
  
  srctype
  
  Indicates the data type of the data to be converted. 
tags:
  - "clr-integration"
  - "srv-willconvert"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Determines whether a specific data type conversion is available within the ODS Library.

srctype

Indicates the data type of the data to be converted. This parameter can be any of the Extended

Stored Procedure API data types.

desttype

Indicates the data type to which the source data is converted. This parameter can be any of the

Extended Stored Procedure API data types.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
BOOL srv_willconvert (
int
srctype
,
int
desttype
);
```
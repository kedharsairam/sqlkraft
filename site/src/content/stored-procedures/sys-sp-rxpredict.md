---
name: 'sys.sp_rxpredict'
title: 'sp_rxpredict'
category: 'general'
description: 'SQL Server 2016 (13.x) and later - Windows only Generates a predicted value for a given input consisting of a machine learning model stored in a binary format in a SQL Server database. Provides scoring on R and Python machine learning models in near real time. stored procedure written in C++, and is optimized specifically for scoring operations. The model must be created using R or Python. However'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_rx
  P
  redict ( @model , @input )
  [ ; ]
---

## Description

SQL Server 2016 (13.x) and later - Windows only Generates a predicted value for a given input consisting of a machine learning model stored in a binary format in a SQL Server database. Provides scoring on R and Python machine learning models in near real time. stored procedure written in C++, and is optimized specifically for scoring operations. The model must be created using R or Python. However, once it's serialized and stored in a

## Syntax

```sql
sp_rx
P
redict ( @model , @input )
[ ; ]
```

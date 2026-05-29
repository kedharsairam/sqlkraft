---
title: "Change data capture (CDC)"
topic: "change-data-capture"
description: |
  08/22/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  In this article, learn about change data capture (CDC), which records activity on a database
  
  when tables and rows have been modified.
  
tags:
  - "change-data-capture"
  - "change-data-capture-cdc"
pubDate: 2025-12-01
---

08/22/2025

Applies to:

SQL Server

Azure SQL Managed Instance

In this article, learn about change data capture (CDC), which records activity on a database

when tables and rows have been modified.

This article explains how CDC works with SQL Server and Azure SQL Managed Instance. For

Azure SQL Database, see

CDC with Azure SQL Database

.

Change data capture utilizes the SQL Server Agent to log insertions, updates, and deletions

occurring in a table. So, it makes these data changes accessible to be easily consumed using a

relational format. The column data and essential metadata need to apply these change data to

a target environment are captured for the modified rows and stored in change tables that

mirror the column structure of the tracked source tables. Furthermore, table-valued functions

are available for systematic access to this change data by consumers.

A good example of a data consumer this technology targets is an extraction, transformation,

and loading (ETL) application. An ETL application incrementally loads change data from SQL

Server source tables to a data warehouse or data mart. Although the representation of the

source tables within the data warehouse must reflect changes in the source tables, an end-to-

end technology that refreshes a replica of the source isn't appropriate. Instead, you need a

reliable stream of change data that is structured so that consumers can apply it to dissimilar

target representations of the data. SQL Server change data capture provides this technology.

The following illustration shows the principal data flow for change data capture.
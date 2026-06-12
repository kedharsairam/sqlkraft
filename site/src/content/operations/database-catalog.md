---
title: "Database catalog"
topic: "monitor"
description: "The WideWorldImporters database contains all the transaction information and daily data for sales and purchases, as well as sensor"
tags: ["monitor","database-catalog"]
pubDate: 2025-12-01
---

The WideWorldImporters database contains all the transaction information and daily data for

sales and purchases, as well as sensor data for vehicles and cold rooms.

WideWorldImporters uses schemas for different purposes, such as storing data, defining how

users can access the data, and providing objects for data warehouse development and

integration.

These schemas contain the data. Many tables are needed by all other schemas and are located

in the Application schema.

Description

Application

Application-wide users, contacts, and parameters. This schema also contains reference

tables with data that is used by multiple schemas

Purchasing

Stock item purchases from suppliers and details about suppliers.

Sales

Stock item sales to retail customers, and details about customers and sales people.

Warehouse

Stock item inventory and transactions.

These schemas are used for external applications that are not allowed to access the data tables

directly. They contain views and stored procedures used by external applications.

Description

Website

All access to the database from the company website is through this schema.

Reports

All access to the database from Reporting Services reports is through this schema.

ﾉ

Expand table

ﾉ

Expand table

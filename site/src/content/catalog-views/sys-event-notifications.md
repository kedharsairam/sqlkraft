---
name: "sys.event_notifications"
title: "sys.event_notifications"
category: "compatibility"
description: "SQL database in Microsoft Fabric Returns a row for each object that is an event notification, with Object identification number. Is unique within a database. Non-zero ID of the parent object. 0 = The parent class is the database. Name of the target service to which the notification is sent. Broker instance to which the notification is sent. ID of the database principal that owns this event notific"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

SQL database in Microsoft Fabric Returns a row for each object that is an event notification, with Object identification number. Is unique within a database. Non-zero ID of the parent object. 0 = The parent class is the database. Name of the target service to which the notification is sent. Broker instance to which the notification is sent. ID of the database principal that owns this event notification.

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Returns a row for each object that is an event notification, with = EN. Description Event notification name. Object identification number. Is unique within a database. Class of parent. 0 = Database 1 = Object or Column DATABASE OBJECT_OR_COLUMN Non-zero ID of the parent object. 0 = The parent class is the database. Date created. Always equals . Name of the target service to which the notification is sent. Broker instance to which the notification is sent. ID of the database principal that owns this event notification. SID of the login who created the event notification. Is NULL if the FAN_IN option is not specified. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . ﾉ Expand table

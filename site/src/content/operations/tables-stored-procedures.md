---
title: "Tables & Stored Procedures"
topic: "high-availability"
description: "This topic describes all of the tables and stored procedures associated with a log shipping configuration. All log shipping tables are stored in on e"
tags: ["high-availability","tables-stored-procedures"]
pubDate: 2025-12-01
---

This topic describes all of the tables and stored procedures associated with a log shipping

configuration. All log shipping tables are stored in

on each server. The tables below

describe which tables and stored procedures are used on which servers in a log shipping

configuration.

Description

log_shipping_monitor_alert

Stores alert job ID. This table is only used on the primary server if a

remote monitor server has not been configured.

log_shipping_monitor_error_detail

Stores error detail for log shipping jobs associated with this

primary server.

log_shipping_monitor_history_detail

Stores history detail for log shipping jobs associated with this

primary server.

log_shipping_monitor_primary

Stores one monitor record for this primary database.

log_shipping_primary_databases

Contains configuration information for primary databases on a

given server. Stores one row per primary database.

log_shipping_primary_secondaries

Maps primary databases to secondary databases.

Description

sp_add_log_shipping_primary_database

Sets up the primary database for a log shipping

configuration, including the backup job, local monitor

record, and remote monitor record.

sp_add_log_shipping_primary_secondary

Adds a secondary database name to an existing primary

database.

ﾉ

Expand table

ﾉ

Expand table

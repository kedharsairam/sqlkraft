---
name: "sys.sp_replication_agent_checkup"
title: "sp_replication_agent_checkup"
category: "general"
description: "Checks each distribution database for replication agents that are running but haven't logged history within the specified heartbeat interval. This stored procedure is executed at the The maximum number of minutes that an agent can go without logging a progress message. raises error 14151 for each agent it detects as suspect."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "sp_replication_agent_checkup"
---

## Description

Checks each distribution database for replication agents that are running but haven't logged history within the specified heartbeat interval. This stored procedure is executed at the The maximum number of minutes that an agent can go without logging a progress message. raises error 14151 for each agent it detects as suspect. It also logs a failure history message about the agents.

## Syntax

`sp_replication_agent_checkup`

## Permissions

SQL) 06/23/2025 Checks each distribution database for replication agents that are running but haven't logged history within the specified heartbeat interval. This stored procedure is executed at the Distributor on any database. syntaxsql The maximum number of minutes that an agent can go without logging a progress message. @heartbeat_interval is , with a default of minutes. raises error 14151 for each agent it detects as suspect. It also logs a failure history message about the agents. is used in snapshot replication, transactional replication, and merge replication. Only members of the fixed server role can execute. System stored procedures (Transact-SQL)

---
name: "sys.sp_removedbreplication"
title: "sp_removedbreplication"
category: "general"
description: "This stored procedure removes all replication objects on the publication database on the Publisher instance of SQL Server, or on the subscription database on the Subscriber instance of in the appropriate database, or, if the execution is in the context of another database on the same instance, specify the database where the replication objects should be removed."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_removedbreplication"
---

## Description

This stored procedure removes all replication objects on the publication database on the Publisher instance of SQL Server, or on the subscription database on the Subscriber instance of in the appropriate database, or, if the execution is in the context of another database on the same instance, specify the database where the replication objects should be removed. This procedure doesn't remove objects from other

## Syntax

`sp_removedbreplication`

## Permissions

Only members of the fixed server role can execute . Disable Publishing and Distribution sp_adddistpublisher (Transact-SQL) sp_changedistpublisher (Transact-SQL) sp_helpdistpublisher (Transact-SQL) Replication stored procedures (Transact-SQL) Related content

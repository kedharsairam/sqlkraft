---
name: "sys.sp_restoredbreplication"
title: "sp_restoredbreplication"
category: "general"
description: "Removes replication settings if restoring a database to the non-originating server, database, or system that is otherwise not capable of running replication processes. When restoring a replicated database to a server or database other than the one where the backup was taken, replication settings can't be preserved. On the restore, the server calls directly to automatically remove replication metad"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_restoredbreplication"
---

## Description

Removes replication settings if restoring a database to the non-originating server, database, or system that is otherwise not capable of running replication processes. When restoring a replicated database to a server or database other than the one where the backup was taken, replication settings can't be preserved. On the restore, the server calls directly to automatically remove replication metadata from the restored database.

## Syntax

`sp_restoredbreplication`

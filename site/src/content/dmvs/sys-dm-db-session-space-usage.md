---
name: "sys.dm_db_session_space_usage"
title: "sys.dm_db_session_space_usage"
category: "io"
description: "Returns the number of pages allocated and deallocated by each session for the database. In Azure SQL Database, the values are unique within a single database or an elastic pool, but Number of pages reserved or allocated for user Number of pages deallocated and no longer reserved for user objects by this session."
tags: ["io","dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_pdw_nodes_db_session_space_usage"
---

## Description

Analytics Platform System (PDW) Returns the number of pages allocated and deallocated by each session for the database. In Azure SQL Database, the values are unique within a single database or an elastic pool, but Number of pages reserved or allocated for user Number of pages deallocated and no longer reserved for user objects by this session. Number of pages reserved or allocated for internal objects by this session.

## Syntax

`sys.dm_pdw_nodes_db_session_space_usage`

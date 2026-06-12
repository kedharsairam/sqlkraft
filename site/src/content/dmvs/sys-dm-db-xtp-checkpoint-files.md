---
name: "sys.dm_db_xtp_checkpoint_files"
title: "sys.dm_db_xtp_checkpoint_files"
category: "in-memory"
description: "Displays information about In-Memory OLTP checkpoint files, including file size, physical location and the transaction ID. A memory-optimized file group internally uses append-only files to store inserted and deleted rows for in-memory tables. There are two types of files. A data file contains inserted rows while a delta file contains references to deleted rows. SQL Server 2014 (12.x) is substanti"
tags: ["in-memory","dmv"]
pubDate: "2026-05-29"
syntax: "sys.dm_db_xtp_checkpoint_files"
---

## Description

Displays information about In-Memory OLTP checkpoint files, including file size, physical location and the transaction ID. A memory-optimized file group internally uses append-only files to store inserted and deleted rows for in-memory tables. There are two types of files. A data file contains inserted rows while a delta file contains references to deleted rows.

## Syntax

`sys.dm_db_xtp_checkpoint_files`

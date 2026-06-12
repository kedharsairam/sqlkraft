---
name: "sys.sp_filestream_force_garbage_collection"
title: "sp_filestream_force_garbage_collection"
category: "general"
description: "Forces the FILESTREAM garbage collector (GC) to run, deleting any unneeded FILESTREAM files. A FILESTREAM container can't be removed until all the deleted files within it are cleaned up by the GC. The FILESTREAM GC runs automatically. However, if you need to remove a container before the GC has run, you can use Signifies the name of the database to run the GC on."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "sp_filestream_force_garbage_collection"
---

## Description

Forces the FILESTREAM garbage collector (GC) to run, deleting any unneeded FILESTREAM files. A FILESTREAM container can't be removed until all the deleted files within it are cleaned up by the GC. The FILESTREAM GC runs automatically. However, if you need to remove a container before the GC has run, you can use Signifies the name of the database to run the GC on. If not specified, current database is assumed.

## Syntax

`sp_filestream_force_garbage_collection`

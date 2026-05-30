---
name: "sys.sp_addtabletocontents"
title: "sp_addtabletocontents"
category: "general"
description: "inserts references into the merge tracking tables, for any rows in a source table that aren't currently included in the tracking tables. Use this option if you bulk- loaded a large amount of data using , which won't fire merge tracking triggers. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the owner of the table. Specif"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_addtabletocontents"
---

## Description

inserts references into the merge tracking tables, for any rows in a source table that aren't currently included in the tracking tables. Use this option if you bulk- loaded a large amount of data using , which won't fire merge tracking triggers. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the owner of the table. Specifies a filter clause that controls which rows of the newly loaded data should be added to

## Syntax

`sp_addtabletocontents`

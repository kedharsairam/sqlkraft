---
name: "sys.sp_xtp_bind_db_resource_pool"
title: "sys.sp_xtp_bind_db_resource_pool"
category: "general"
description: "Binds the specified In-Memory OLTP database to the specified resource pool. Both the database and the resource pool must exist prior to executing This system procedure creates a binding between the Resource Governor pool identified by , and the database identified by the database has any memory-optimized objects at the time of binding. In the absence of memory-optimized objects, there's no memory"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sys.sp_xtp_bind_db_resource_pool"
---

## Description

Binds the specified In-Memory OLTP database to the specified resource pool. Both the database and the resource pool must exist prior to executing This system procedure creates a binding between the Resource Governor pool identified by , and the database identified by the database has any memory-optimized objects at the time of binding. In the absence of memory-optimized objects, there's no memory taken from the resource pool.

## Syntax

`sys.sp_xtp_bind_db_resource_pool`

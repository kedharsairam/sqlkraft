---
name: "sys.dm_os_memory_brokers"
title: "sys.dm_os_memory_brokers"
category: "os"
description: "Allocations that are internal to SQL Server use the SQL Server memory manager. Tracking the difference between process memory counters from counters can indicate memory use from external components in the SQL Server memory space. Memory brokers fairly distribute memory allocations between various components within SQL Server, based on current and projected usage. Me"
tags: ["os", "dmv"]
pubDate: 2026-05-29
---

## Description

Analytics Platform System (PDW) Allocations that are internal to SQL Server use the SQL Server memory manager. Tracking the difference between process memory counters from counters can indicate memory use from external components in the SQL Server memory space. Memory brokers fairly distribute memory allocations between various components within SQL Server, based on current and projected usage. Memory brokers do not perform allocations.

---
name: "sys.dm_exec_query_optimizer_memory_gateways"
title: "sys.dm_exec_query_optimizer_memory_gateways"
category: "execution"
description: "Requires VIEW SERVER PERFORMANCE STATE permission on the server. SQL Server uses a tiered gateway approach to reduce the number of permitted concurrent compilations. Three gateways are used, including small, medium, and big. Gateways help prevent the exhausting of overall memory resources by larger compilation memory-requiring Waits on a gateway result in delayed compilation. In addition to delays"
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_exec_query_optimizer_memory_gateways"
---

## Description

Requires VIEW SERVER PERFORMANCE STATE permission on the server. SQL Server uses a tiered gateway approach to reduce the number of permitted concurrent compilations. Three gateways are used, including small, medium, and big. Gateways help prevent the exhausting of overall memory resources by larger compilation memory-requiring Waits on a gateway result in delayed compilation. In addition to delays in compilation, reduced

## Syntax

`sys.dm_exec_query_optimizer_memory_gateways`

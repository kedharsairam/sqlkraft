---
name: "sys.dm_exec_distributed_requests"
title: "sys.dm_exec_distributed_requests"
category: "execution"
description: "2016 (13.x) and later versions Holds information about all requests currently or recently active in PolyBase queries. It lists one Based on session and request ID, a user can then retrieve the actual distributed requests generated to be executed - via sys.dm_exec_distributed_requests."
tags: ["execution","dmv"]
pubDate: "2026-05-29"
---

## Description

2016 (13.x) and later versions Holds information about all requests currently or recently active in PolyBase queries. It lists one Based on session and request ID, a user can then retrieve the actual distributed requests generated to be executed - via sys.dm_exec_distributed_requests. For example, a query involving regular SQL and external SQL tables will be decomposed into various statements/requests executed across the various compute nodes.

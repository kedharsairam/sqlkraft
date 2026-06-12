---
name: "sys.query_context_settings"
title: "sys.query_context_settings"
category: "compatibility"
description: "2016 (13.x) and later versions SQL database in Microsoft Fabric Contains information about the semantics affecting context settings associated with a query. There are several context settings available in SQL Server that influence the query semantics (defining the correct result of the query). The same query text compiled under different settings might produce different results (dependi"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

2016 (13.x) and later versions SQL database in Microsoft Fabric Contains information about the semantics affecting context settings associated with a query. There are several context settings available in SQL Server that influence the query semantics (defining the correct result of the query). The same query text compiled under different settings might produce different results (depending on the underlying data).

## Code Blocks

`context_settings_id`

`set_options`

`language_id`

`date_format`

`date_first`

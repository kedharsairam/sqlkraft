---
name: "sys.system_sql_modules"
title: "sys.system_sql_modules"
category: "compatibility"
description: "Returns one row per system object that contains a SQL language-defined module. System objects of type FN, IF, P, PC, TF, V have an associated SQL module. To identify the containing object, you can join this view to Object identification number of the containing object, unique SQL text that defines this module. 1 = Module was created"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns one row per system object that contains a SQL language-defined module. System objects of type FN, IF, P, PC, TF, V have an associated SQL module. To identify the containing object, you can join this view to Object identification number of the containing object, unique SQL text that defines this module. 1 = Module was created with the SET ANSI_NULLS database

---
name: "sys.database_permissions"
title: "sys.database_permissions"
category: "security"
description: "Returns a row for every permission or column-exception permission in the database. For columns, there is a row for every permission that is different from the corresponding object- level permission. If the column permission is the same as the corresponding object permission, there is no row for it and the permission applied is that o"
tags: ["security", "catalog-view"]
pubDate: 2026-05-29
syntax: "sys.database_permissions"
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns a row for every permission or column-exception permission in the database. For columns, there is a row for every permission that is different from the corresponding object- level permission. If the column permission is the same as the corresponding object permission, there is no row for it and the permission applied is that of the object.

## Syntax

`sys.database_permissions`

## Permissions

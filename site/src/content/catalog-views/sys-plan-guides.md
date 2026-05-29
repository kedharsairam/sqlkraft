---
name: 'sys.plan_guides'
title: 'sys.plan_guides'
category: 'objects'
description: 'object_id of the object defining the scope of the plan guide, if the'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
object_id of the object defining the scope of the plan guide, if the

scope is OBJECT.

NULL if the plan guide is not scoped to OBJECT.

Batch text, if

is SQL.

NULL if batch type is not SQL.

If NULL and

is SQL, the value of

applies.

The string defining the list of parameters associated with the plan

guide.

NULL = No parameter list is associated with the plan guide.

The OPTION clause hints associated with the plan guide.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Catalog Views (Transact-SQL)

sp_create_plan_guide (Transact-SQL)

sp_create_plan_guide_from_handle (Transact-SQL)

Last updated on 11/18/2025

See Also

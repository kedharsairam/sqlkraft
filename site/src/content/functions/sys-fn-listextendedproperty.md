---
name: 'sys.fn_listextendedproperty'
title: 'sys.fn_listextendedproperty'
category: 'text-image'
description: 'SQL database in Microsoft Fabric Returns extended property values of database objects. Transact-SQL syntax conventions . Valid inputs are default, NULL, or a Is the user or user-defined type.'
tags: ["text-image", "function"]
pubDate: 2026-05-29
syntax: |
  fn_listextendedproperty (
  { default | 'property_name' | NULL }
  , { default | 'level0_object_type' | NULL }
  , { default | 'level0_object_name' | NULL }
  , { default | 'level1_object_type' | NULL }
  , { default | 'level1_object_name' | NULL }
  , { default | 'level2_object_type' | NULL }
  , { default | 'level2_object_name' | NULL }
  )
---

## Description

SQL database in Microsoft Fabric Returns extended property values of database objects. Transact-SQL syntax conventions . Valid inputs are default, NULL, or a Is the user or user-defined type.

## Syntax

```sql
fn_listextendedproperty (
{ default | 'property_name' | NULL }
, { default | 'level0_object_type' | NULL }
, { default | 'level0_object_name' | NULL }
, { default | 'level1_object_type' | NULL }
, { default | 'level1_object_name' | NULL }
, { default | 'level2_object_type' | NULL }
, { default | 'level2_object_name' | NULL }
)
```

## Arguments

Applies to:


Azure SQL Database


Azure SQL Managed Instance


SQL database in Microsoft Fabric


Returns extended property values of database objects.


Transact-SQL syntax conventions


{ default | '


property_name


Is the name of the property.


property_name


. Valid inputs are default, NULL, or a


property name.


{ default | '


level0_object_type


Is the user or user-defined type.


level0_object_type


, with a default of NULL.


Valid inputs are:


EVENT NOTIFICATION


MESSAGE TYPE


PARTITION FUNCTION


PARTITION SCHEME


REMOTE SERVICE BINDING

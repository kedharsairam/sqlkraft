---
name: "sys.dm_audit_class_type_map"
title: "sys.dm_audit_class_type_map"
category: "security-audit"
description: "Returns a table that lists securable classes that can be mapped to the audit log. For more information about SQL Server Audit, see The class type of the entity that was audited."
tags: ["security-audit", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_audit_actions."
---

## Description

Returns a table that lists securable classes that can be mapped to the audit log. For more information about SQL Server Audit, see The class type of the entity that was audited. Maps to written to the audit log returned by The name of the class of the object that was audited. The securable class that maps to the map to a securable object. Can be joined with This view is visible to the public. function, SQL Server 2019 (15.x) and earlier versions require

## Syntax

`sys.dm_audit_actions.`

## Examples

### Example 1

`class_type`

### Example 2

`class_type`

### Example 3

`class_type`

### Example 4

`get_audit_file()`

### Example 5

`class_type_desc`

### Example 6

`securable_class_desc`

### Example 7

`class_type`

### Example 8

`NULL`

### Example 9

`class_type`

### Example 10

`class_desc`

_(... and 6 more examples)_

---
name: "sys.sp_server_info"
title: "sp_server_info"
category: "general"
description: "Returns a list of attribute names and matching values for SQL Server, the database gateway, or the underlying data source. Used in ODBC only. The integer ID of the attribute. Current setting of the attribute."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_server_info [ [ @attribute_id = ] attribute_id ]
      [ ; ]
---

## Description

Returns a list of attribute names and matching values for SQL Server, the database gateway, or the underlying data source. Used in ODBC only. The integer ID of the attribute. Current setting of the attribute.

## Syntax

```sql
sp_server_info [ [ @attribute_id = ] attribute_id ]
[ ; ]
```

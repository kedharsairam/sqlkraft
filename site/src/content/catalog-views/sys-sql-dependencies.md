---
name: "sys.sql_dependencies"
title: "sys.sql_dependencies"
category: "compatibility"
description: "Contains a row for each dependency on a referenced entity as referenced in the Transact-SQL expression or statements that define some other referencing object. Identifies the class of the referenced entity: 0 = Object or column (non-schema-bound references only) 1 = Object or column (schema-bound references) 2 = Types (schema-bound references) 3 = XML Schema collections (schema-bound references) 4"
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
syntax: "<schema_name.table_name>"
---

## Description

Contains a row for each dependency on a referenced entity as referenced in the Transact-SQL expression or statements that define some other referencing object. Identifies the class of the referenced entity: 0 = Object or column (non-schema-bound references only) 1 = Object or column (schema-bound references) 2 = Types (schema-bound references) 3 = XML Schema collections (schema-bound references) 4 = Partition function (schema-bound references)

## Syntax

```sql
<schema_name.table_name>
```

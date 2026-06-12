---
name: "To View Masking Function of Column in Table"
title: "To View Masking Function of Column in Table"
description: "diagnostic script for database operations."
category: database
tags: ["database", "table"]
pubDate: 2025-03-15
---

```sql
select object_name(object_id) tablename, name as column_name, is_masked, masking_function from sys.masked_columns order by tablename, column_name
```

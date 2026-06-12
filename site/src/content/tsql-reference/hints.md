---
name: "Hints"
title: "Hints"
category: "hints"
description: ""
tags: ["tsql","hints"]
pubDate: "2026-05-29"
---

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

database in Microsoft Fabric

Hints are options or strategies specified for enforcement by the SQL Server query processor on

,

,

, or

statements. The hints override any execution plan the query

optimizer might select for a query.

The following hints are described in this section:

Join hints

Query hints

Table hints

Ｕ

Caution

Because the SQL Server query optimizer typically selects the best execution plan for a

query, we recommend that

,

, and

be used only as

a last resort by experienced developers and database administrators.

`SELECT`

`INSERT`

`UPDATE`

`DELETE`

```sql
<join_hint>
```

```sql
<query_hint>
```

```sql
<table_hint>
```

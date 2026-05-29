---
name: '@@PACK_RECEIVED'
title: '@@PACK_RECEIVED'
category: 'variables'
description: 'table (trigger scope). For'
tags: ["tsql", "variables"]
pubDate: 2026-05-29
---

In this example,


## returns the
from the

table (current

scope), while


## returns the
from the

table (trigger scope). For

most application scenarios,

is the safer choice because it isn't affected by

trigger activity.

SCOPE_IDENTITY (Transact-SQL)

IDENT_CURRENT (Transact-SQL)

System Functions by category for Transact-SQL

CREATE TABLE (Transact-SQL)

INSERT (Transact-SQL)

SELECT (Transact-SQL)

Last updated on 02/26/2026

Related content

### integer

### sp_monitor

```sql
SCOPE_IDENTITY()
```

```sql
ProductID
```

```sql
Products
```

```sql
@@IDENTITY
```

```sql
AuditID
```

```sql
ProductAudit
```

```sql
SCOPE_IDENTITY()
```

```sql
SELECT
ProductID,
'INSERT'
FROM
inserted;
END
;
GO
-- Insert a product and compare identity values
INSERT
INTO
dbo.Products (ProductName)
VALUES
(
'Test Product'
);
SELECT
@@
IDENTITY
AS
[@@
IDENTITY
],
SCOPE_IDENTITY()
AS
[SCOPE_IDENTITY];
GO
```

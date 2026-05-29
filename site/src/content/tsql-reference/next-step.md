---
name: 'Next step'
title: 'Next step'
category: 'statements'
description: 'DROP SYNONYM (Transact-SQL)'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

### Create Synonyms

DROP SYNONYM (Transact-SQL)

EVENTDATA (Transact-SQL)

GRANT (Transact-SQL)

Synonyms (Database Engine)

Last updated on 11/18/2025

Related content

```sql
SET
@OrderAmt += 12 - (@OrderAmt % 12)
END
RETURN
(@OrderAmt);
END
;
GO
-- Using the dbo.OrderDozen function
DECLARE
@Amt
INT
;
SET
@Amt = 15;
SELECT
@Amt
AS
OriginalOrder,
dbo.OrderDozen(@Amt)
AS
ModifiedOrder;
-- Create a synonym dbo.CorrectOrder for the dbo.OrderDozen function.
CREATE
SYNONYM
dbo.CorrectOrder
FOR
dbo.OrderDozen;
GO
-- Using the dbo.CorrectOrder synonym.
DECLARE
@Amt
INT
;
SET
@Amt = 15;
SELECT
@Amt
AS
OriginalOrder,
dbo.CorrectOrder(@Amt)
AS
ModifiedOrder;
```

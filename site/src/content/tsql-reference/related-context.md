---
name: "Related context"
title: "Related context"
category: "statements"
description: "@@TRANCOUNT (Transact-SQL)"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

@@TRANCOUNT (Transact-SQL)

BEGIN TRANSACTION (Transact-SQL)

COMMIT TRANSACTION (Transact-SQL)

ROLLBACK TRANSACTION (Transact-SQL)

SAVE TRANSACTION (Transact-SQL)

TRY.CATCH (Transact-SQL)

```sql
-- Test whether the transaction is uncommittable.
IF
XACT_STATE() = -1
BEGIN
PRINT
'The transaction is in an uncommittable state.'
+
' Rolling back transaction.'
ROLLBACK
TRANSACTION
;
END
;
-- Test whether the transaction is active and valid.
IF XACT_STATE() = 1
BEGIN
PRINT
'The transaction is committable.'
+
' Committing transaction.'
COMMIT
TRANSACTION
;
END
;
END
CATCH;
```

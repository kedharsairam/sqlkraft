---
name: "Remarks"
title: "Remarks"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

Specifies whether SQL Server automatically rolls back the current transaction when a Transact-

SQL statement raises a run-time error.

## syntaxsql

When SET XACT_ABORT is ON, if a Transact-SQL statement raises a run-time error, the entire

transaction is terminated and rolled back.

When SET XACT_ABORT is OFF, in some cases only the Transact-SQL statement that raised the

error is rolled back and the transaction continues processing. Depending upon the severity of

the error, the entire transaction may be rolled back even when SET XACT_ABORT is OFF. OFF is

the default setting in a T-SQL statement, while ON is the default setting in a trigger.

Compile errors, such as syntax errors, are not affected by SET XACT_ABORT.

XACT_ABORT must be set ON for data modification statements in an implicit or explicit

transaction against most OLE DB providers, including SQL Server. The only case where this

option is not required is if the provider supports nested transactions.

When ANSI_WARNINGS=OFF, permissions violations cause transactions to abort.

The setting of SET XACT_ABORT is set at execute or run time and not at parse time.

７

Note

The

statement honors.

does not. New applications

should use

instead of.

```sql
SET
XACT
_
ABORT
{
ON
|
OFF
}
```

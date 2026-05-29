---
name: 'sys.sp_oadestroy'
title: 'sp_OADestroy'
category: 'general'
description: 'Destroys a created OLE object. Transact-SQL syntax conventions The object token of an OLE object that was previously created by using (success) or a nonzero number (failure) that is the integer value of the HRESULT returned by the OLE Automation object. For more information about HRESULT return codes, see OLE automation return codes and error Arguments for extended stored procedures must be entere'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_
  OAD
  estroy objecttoken
  [ ; ]
---

## Description

Destroys a created OLE object. Transact-SQL syntax conventions The object token of an OLE object that was previously created by using (success) or a nonzero number (failure) that is the integer value of the HRESULT returned by the OLE Automation object. For more information about HRESULT return codes, see OLE automation return codes and error Arguments for extended stored procedures must be entered in the specific order as described in the section. If the parameters are entered out of order, an error message occurs.

## Syntax

```sql
sp_
OAD
estroy objecttoken
[ ; ]
```

## Remarks

Applies to:

Destroys a created OLE object.

Transact-SQL syntax conventions

The object token of an OLE object that was previously created by using

(success) or a nonzero number (failure) that is the integer value of the HRESULT returned by

the OLE Automation object.

For more information about HRESULT return codes, see

OLE automation return codes and error

information

Arguments for extended stored procedures must be entered in the specific order as

described in the

section. If the parameters are entered out of order, an error

message occurs.

## Examples

### Example 1

```sql
sp_OADestroy
```

### Example 2

```sql
SQLServer
```

### Example 3

```sql
EXECUTE
@hr = sp_OADestroy
@
object
;
IF @hr <> 0
BEGIN
EXECUTE
sp_OAGetErrorInfo @
object
;
RETURN;
END
```

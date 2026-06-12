---
title: "OLE automation return codes & error information"
topic: "spatial-data"
description: "The OLE automation system stored procedures return an return code that is the HRESULT returned by the underlying OLE automation operation. An HRESULT"
tags: ["spatial-data","ole-automation-return-codes-error-information"]
pubDate: "2025-12-01"
---

The OLE automation system stored procedures return an

return code that is the HRESULT

returned by the underlying OLE automation operation. An HRESULT of 0 indicates success. A

nonzero HRESULT is an OLE error code of the hexadecimal form 0x800

nnnnn

, but when

returned as an

value in a stored procedure return code, HRESULT has the form

-214

nnnnnnn.

For example, passing an invalid object name (SQLDMO.Xyzzy) to sp_OACreate causes the

procedure to return an

HRESULT of 2147221005, which is 0x800401f3 in hexadecimal.

You can use

to convert an

HRESULT to a

value.

For examples of supported conversion, see

H. Using CONVERT with binary and character data.

sp_OAGetErrorInfo (Transact-SQL)

```sql
CONVERT(binary(4), @hresult)
```

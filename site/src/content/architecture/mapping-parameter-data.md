---
title: "Mapping parameter data"
topic: "clr-integration"
description: |
  07/15/2025

  Applies to:

  SQL Server

  The following table lists SQL Server data types, their equivalents in the common language

  runtime (CLR) for SQL Server in the

  namespace, and their native CLR

  eq
tags:
  - "clr-integration"
  - "mapping-parameter-data"
pubDate: 2025-12-01
---

07/15/2025

Applies to:

SQL Server

The following table lists SQL Server data types, their equivalents in the common language

runtime (CLR) for SQL Server in the

namespace, and their native CLR

equivalents in the .NET Framework.

SQL Server data

,

,

,

None

None

None

None

,

,

None

,

,

,

,

None

None

None

None

None

,

,

ﾉ

Expand table

1

1

1

```sql
System.Data.SqlTypes
System.Data.SqlTypes
Microsoft.SqlServer.Types
SqlInt64
Int64
Nullable<Int64>
SqlBytes
SqlBinary
Byte[]
SqlBoolean
Boolean
Nullable<Boolean>
SqlDateTime
DateTime
Nullable<DateTime>
SqlDateTime
DateTime
Nullable<DateTime>
DateTime
Nullable<DateTime>
None
DateTimeOffset
Nullable<DateTimeOffset>
SqlDecimal
Decimal
Nullable<Decimal>
SqlDouble
Double
Nullable<Double>
SqlGeography
SqlGeometry
SqlHierarchyId
SqlInt32
Int32
Nullable<Int32>
SqlMoney
Decimal
Nullable<Decimal>
```

---
title: "Custom attributes for CLR routines"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  The attributes listed can be applied to common language runtime (CLR) routines, user-defined

  types, and user-defined aggre
tags:
  - "clr-integration"
  - "custom-attributes-for-clr-routines"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

Azure SQL Managed Instance

The attributes listed can be applied to common language runtime (CLR) routines, user-defined

types, and user-defined aggregates that are registered in SQL Server. If the attribute isn't

applied, SQL Server assumes the default value. The attributes listed are defined in the

namespace.

The

attribute indicates that the method should be registered as a

user-defined aggregate. Every user-defined aggregate must be annotated with this attribute.

For more information, see

SqlUserDefinedAggregateAttribute

.

The

attribute indicates the method should be registered as a function, with the

appropriate function attributes set.

For more information, see

SqlFunctionAttribute

.

The

attribute is used to return information about the return type of a user-defined

type (UDT) expression.

For more information, see

SqlFacetAttribute

.

The

attribute indicates the method should be registered as a stored procedure.

This attribute is used only by Visual Studio to register the specified method as a stored

procedure automatically; it isn't used by SQL Server.

```sql
Microsoft.SqlServer.Server
SqlUserDefinedAggregate
SqlFunction
SqlFacet
SqlProcedure
```

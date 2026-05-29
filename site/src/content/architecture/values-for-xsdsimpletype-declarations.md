---
title: "Values for <xsd:simpleType> Declarations"
topic: "xml-data"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  The following table outlines the restrictions that are applied, based on all recognized XSD

  simple typ
tags:
  - "xml-data"
  - "values-for-xsdsimpletype-declarations"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The following table outlines the restrictions that are applied, based on all recognized XSD

simple type enumerations.

Also, SQL Server doesn't support the NaN value in

declarations. Schemas

that include

values are rejected by the server.

The year part has to be within the range of -2^31 to 2^31-1. The month, day, hour,

minute, and second must all be within the range of 0 to 9999. The seconds part has an

additional three digits of precision to the right of the decimal point.

The hour part in the time zone subfield must be within the accepted range of -14 to +14.

The year part must be within the range of 1 to 9999. The month part must be within the

range of 1 to 12. The day part must be within the range of 1 to 31 and must be a valid

calendar date. For example, SQL Server detects and returns an error for an invalid date,

such as 1974-02-31, because the month of February doesn't have 31 days.

The second component supports 100-nanosecond precision. The timezone indication is

optional.

SQL Server 2005 supported years in the range -9999 to 9999. SQL Server now supports a

more restricted range of years. For more information, see

Compare Typed XML to Untyped

XML

.

The year part must be within the range of 1 to 9999. The month part must be within the

range of 1 to 12. The day part must be within the range of 1 to 31 and must be a valid

calendar date. For example, SQL Server detects and returns an error for an invalid date,

such as 1974-02-31, because the month of February doesn't have 31 days.

SQL Server 2005 supported years in the range -9999 to 9999. SQL Server now supports a

more restricted range of years. For more information, see

Compare Typed XML to Untyped

XML

.

The year part must be within the range of -9999 to 9999.

The year part must be within the range of -9999 to 9999.

The month part must be within the range of 1 to 12. The day part must be within the

range of 1 to 31.

ﾉ

Expand table

```sql
<xsd:simpleType>
NaN
```

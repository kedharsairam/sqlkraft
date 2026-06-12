---
name: "Example: Cross-domain Query Using sql:variable()"
title: "Example: Cross-domain Query Using sql:variable()"
category: "variables"
description: ""
tags: ["tsql","variables"]
pubDate: "2026-05-29"
---

You can specify

xml Data Type Methods

against an

data type variable or column. For

example, the

query() Method (xml Data Type)

executes the specified XQuery against an XML

instance. When you construct XML in this manner, you may want to bring in a value from a

non-XML type column or a Transact-SQL variable. This process is referred to as binding

relational data inside XML.

To bind the non-XML relational data inside XML, the SQL Server Database Engine provides the

following pseudo-functions:

sql:column() Function (XQuery)

Lets you use the values from a relational column in your

XQuery or XML DML expression.

sql:variable() Function (XQuery). Lets you use the value of a SQL variable in your XQuery

or XML DML expression.

You can use these functions with

data type methods whenever you want to expose a

relational value inside XML.

You cannot use these functions to reference data in columns or variables of the

, CLR user-

defined types, datetime, smalldatetime,

,

,

sql_variant

, and

types.

Also, this binding is for read-only purposes. That is, you cannot write data in columns that use

these functions. For example, sql:variable("@x")="

some expression"

is not allowed.

This example shows how

sql:variable()

can enable an application to parameterize a query. The

ISBN is passed in by using a SQL variable @isbn. By replacing the constant with

sql:variable()

,

the query can be used to search for any ISBN and not just the one whose ISBN is 0-7356-1588-

2.

sql:column()

can be used in a similar manner and provides additional benefits. Indexes over

the column may be used for efficiency, as decided by the cost-based query optimizer. Also, the

computed column may store a promoted property.

xml Data Type Methods

See Also

```sql
DECLARE
@isbn
VARCHAR (20)
SET
@isbn =
'0-7356-1588-2'
SELECT xCol
FROM
T
WHERE xCol.exist (
'/book/@ISBN[. = sql:variable("@isbn")]'
) = 1
```

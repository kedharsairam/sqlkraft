---
name: 'Converting float and real data'
title: 'Converting float and real data'
category: 'data-types'
description: '- 3.40E + 38 to -1.18E - 38, 0 and 1.18E - 38 to 3.40E + 38'
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

- 3.40E + 38 to -1.18E - 38, 0 and 1.18E - 38 to 3.40E + 38

4 Bytes

The float and real data types are known as approximate data types. The behavior of float and

real follows the

IEEE 754

specification on approximate numeric data types. To understand

how the Microsoft Visual C (MSVC) compiler uses the IEEE 754 standard, see

IEEE Floating-Point

Representation

Approximate numeric data types don't store the exact values specified for many numbers; they

store a close approximation of the value. For some applications, the tiny difference between

the specified value and the stored approximation isn't relevant. For others though, the

difference is important. Because of the approximate nature of the float and real data types,

don't use these data types when exact numeric behavior is required. Examples that require

precise numeric values are financial or business data, operations involving rounding, or equality

checks. In those cases, use the integer, decimal, numeric, money, or smallmoney data types.

Avoid using float or real columns in WHERE clause search conditions, especially the = and <>

operators. It's best to limit float and real columns to > or < comparisons.

Values of

are truncated when they're converted to any integer type.

When you want to convert from

or

to character data, using the STR string function is

typically more useful than CAST( ). The reason is that STR() enables more control over

formatting. For more information, see

STR (Transact-SQL)

and

Functions (Transact-SQL)

.

Prior to SQL Server 2016 (13.x), conversion of

values to

or

is restricted to

values of precision 17 digits only. Any

value less than 5E-18 (when set using either the

scientific notation of 5E-18 or the decimal notation of 0.000000000000000005) rounds down to

0. This is no longer a restriction as of SQL Server 2016 (13.x).

ALTER TABLE (Transact-SQL)

CAST and CONVERT (Transact-SQL)

CREATE TABLE (Transact-SQL)

Data type conversion (Database Engine)

Data types (Transact-SQL)

DECLARE @local_variable (Transact-SQL)

SET @local_variable (Transact-SQL)

Related content

Last updated on 11/18/2025

---
name: "Function collation"
title: "Function collation"
category: "statements"
description: "Perform logical operations."
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

## Description

Logical Functions

Perform logical operations.

Mathematical Functions

the functions, and return numeric values.

Metadata Functions

Return information about the database and database objects.

Security Functions

Return information about users and roles.

String Functions

Perform operations on a string (

or

) input value and return a

string or numeric value.

System Functions

settings in an instance of SQL Server.

System Statistical Functions

Return statistical information about the system.

Text and Image Functions

Perform operations on text or image input values or columns, and return

information about the value.

Scalar functions perform an operation on a string input value and return a string or numeric

value, for example,

ASCII (Transact-SQL).

All built-in string functions except

are deterministic.

value any time they are called with a specific set of input values.

Deterministic and Nondeterministic Functions.

implicitly converted to a text data type.

Data Type Conversion

(Database Engine).

built-in functions are either deterministic or nondeterministic.

deterministic when they always return the same result anytime they're called by using a specific

set of input values. Functions are nondeterministic when they could return different results

every time they're called, even with the same specific set of input values. For more information,

see

Deterministic and nondeterministic functions

`FORMAT`

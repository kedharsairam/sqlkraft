---
name: "Scalar functions"
title: "Scalar functions"
category: "statements"
description: "Configuration functions are scalar functions that return information about current"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

## Categories of scalar functions

Configuration functions are scalar functions that return information about current

configuration option settings, for example,

@@SERVERNAME (Transact-SQL).

All configuration functions operate in a nondeterministic way. In other words, these functions

do not always return the same results every time they are called, even with the same set of

input values. For more information about function determinism, see

Deterministic and

Nondeterministic Functions.

Ranking functions return a ranking value for each row in a partition. Depending on the function

that is used, some rows might receive the same value as other rows. Ranking functions are

nondeterministic.

Rowset functions Return an object that can be used like table references in a SQL statement.

Operate on a single value and then return a single value. Scalar functions can be used wherever

an expression is valid.

## Description

Configuration Functions

Return information about the current configuration.

Conversion Functions

Support data type casting and converting.

Cursor Functions

Return information about cursors.

Perform operations on a date and time input values and return string,

numeric, or date and time values.

Graph Functions

graph node and edge IDs.

Validate, query, or change JSON data.

#### Function category

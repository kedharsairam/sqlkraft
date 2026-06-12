---
name: "xquery-error-handling"
title: "XQuery - Error Handling"
category: "xquery"
description: "XQuery Language Reference: Error Handling"
syntax: "XML DML"
tags: ["xquery","error-handling"]
pubDate: "2025-12-01"
---

The W3C specification allows type errors to be raised statically or dynamically, and defines

static, dynamic, and type errors.

Compilation errors are returned from syntactically incorrect Xquery expressions and

statements. The compilation phase checks static type correctness of XQuery expressions and

DML statements, and uses XML schemas for type inferences for typed XML. It raises static type

errors if an expression could fail at run time because of a type safety violation. Examples of

static error are the addition of a string to an integer and querying for a nonexistent node for

typed data.

As a deviation from the W3C standard, XQuery run-time errors are converted into empty

sequences. These sequences might propagate as empty XML or

to the query result,

depending upon the invocation context.

Explicit casting to the correct type allows users to work around static errors, although run-time

cast errors will be transformed to empty sequences.

Static errors are returned by using the Transact-SQL error mechanism. In SQL Server, XQuery

type errors are returned statically. For more information, see

XQuery and Static Typing.

In XQuery, most dynamic errors are mapped to an empty sequence ("()"). However, these are

the two exceptions: Overflow conditions in XQuery aggregator functions and XML-DML

７

Note

Parsing errors raised by the XQuery parser (such as syntax errors in the XML referenced as

part of the XML data type method, for example), abort the active transaction, regardless of

the

setting of the current session.

```sql
XML DML
NULL
```

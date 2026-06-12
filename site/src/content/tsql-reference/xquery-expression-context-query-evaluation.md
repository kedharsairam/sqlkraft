---
name: "xquery-expression-context-query-evaluation"
title: "XQuery - Expression Context & Query Evaluation"
category: "xquery"
description: "XQuery Language Reference: Expression Context & Query Evaluation"
syntax: |
  declare @x xml
            set @x=''
            select @x.query('<a>  {"Hello"}  </a>,
            <b> {"Hello2"}  </b>')
            <a>Hello</a><b>Hello2</b>
tags: ["xquery","expression-context-query-evaluation"]
pubDate: 2025-12-01
---

The context of an expression is the information that is used to analyze and evaluate it.

Following are the two phases in which XQuery is evaluated:

- This is the query compilation phase. Based on the information available,

errors are sometimes raised during this static analysis of the query.

- This is the query execution phase. Even if a query has no static errors,

such as errors during query compilation, the query may return errors during its execution.

Static context initialization refers to the process of putting together all the information for

static analysis of the expression. As part of static context initialization, the following is

completed:

The

policy is set to strip. Therefore, the boundary white space is

not preserved by the

and

constructors in the query. For example:

This query returns the following result, because the boundary space is stripped away

during parsing of the XQuery expression:

The prefix and the namespace binding are initialized for the following:

A set of predefined namespaces.

```sql
declare @x xml set @x=''
select @x.query('<a> {"Hello"} </a>,
<b> {"Hello2"} </b>')
<a>Hello</a><b>Hello2</b>
```

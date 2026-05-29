---
name: "xquery-xquery-static-typing"
title: "XQuery - XQuery & Static Typing"
category: "xquery"
description: "XQuery Language Reference: XQuery & Static Typing"
syntax: "element(age,xs:integer)*"
tags:
  - "xquery"
  - "xquery-static-typing"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

XQuery in SQL Server is a statically typed language. That is, it raises type errors during query

compilation when an expression returns a value that has a type or cardinality that is not

accepted by a particular function or operator. Additionally, static type checking can also detect

if a path expression on a typed XML document has been mistyped. The XQuery compiler first

applies the normalization phase that adds the implicit operations, such as atomization, and

then performs static type inference and static type checking.

Static type inference determines the return type of an expression. It determines this by taking

the static types of the input parameters and the static semantics of the operation and inferring

the static type of the result. For example, the static type of the expression 1 + 2.3 is determined

in the following way:

The static type of 1 is

and the static type of 2.3 is

. Based on the

dynamic semantics, the static semantics of the

operation converts the integer to a

decimal and then returns a decimal. The inferred static type would then be

.

For untyped XML instances, there are special types to indicate that the data was not typed. This

information is used during static type checking and to perform certain implicit casts).

For typed data, the input type is inferred from the XML schema collection that constrains the

XML data type instance. For example, if the schema allows only elements of type

, the

results of a path expression using that element will be zero or more elements of type

. This is currently expressed by using an expression such as

where the asterisk (\*) indicates the cardinality of the resulting type.

In this example, the expression may result in zero or more elements of name "age" and type

. Other cardinalities are exactly one and are expressed by using the type name alone,

zero or one and expressed by using a question mark (

), and 1 or more and expressed by using

a plus sign (

).

Sometimes, the static type inference can infer that an expression will always return the empty

sequence. For example, if a path expression on a typed XML data type looks for a <name>

element inside a <customer> element (/customer/name), but the schema does not allow a

<name> inside a <customer>, the static type inference will infer that the result will be empty.

This will be used to detect incorrect queries and will be reported as a static error, unless the

expression was () or

.

```sql
element(age,xs:integer)*
```

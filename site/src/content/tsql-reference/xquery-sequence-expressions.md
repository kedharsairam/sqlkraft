---
name: "xquery-sequence-expressions"
title: "XQuery - Sequence Expressions"
category: "xquery"
description: "XQuery Language Reference: Sequence Expressions"
syntax: |
  declare @x xml
  set @x=''
  select @x.query('(1,2,3,4,5)')
  go
  -- result 1 2 3 4 5
  -- sequence of 2 nodes
  declare @x xml
  set @x=''
  select @x.query('(<a/>, <b/>)')
  go
  -- result
  <a />
  <b />
tags:
  - "xquery"
  - "sequence-expressions"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

SQL Server supports the XQuery operators that are used to construct, filter, and combine a

sequence of items. An item can be an atomic value or a node.

You can use the comma operator to construct a sequence that concatenates items into a single

sequence.

A sequence can contain duplicate values. Nested sequences, a sequence within a sequence, are

collapsed. For example, the sequence (1, 2, (3, 4, (5))) becomes (1, 2, 3, 4, 5). These are

examples of constructing sequences.

The following query returns a sequence of five atomic values:

The following query returns a sequence of two nodes:

The following query returns an error, because you are constructing a sequence of atomic

values and nodes. This is a heterogeneous sequence and is not supported.

```sql
declare @x xml set @x=''
select @x.query('(1,2,3,4,5)') go
-- result 1 2 3 4 5
-- sequence of 2 nodes declare @x xml set @x=''
select @x.query('(<a/>, <b/>)') go
-- result
<a />
<b />
```

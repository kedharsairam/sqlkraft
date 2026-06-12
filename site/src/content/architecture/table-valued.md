---
title: "Table-valued"
topic: "clr-integration"
description: "A table-valued function is a user-defined function that returns a table."
tags: ["clr-integration","table-valued"]
pubDate: "2025-12-01"
---

A table-valued function is a user-defined function that returns a table.

extends the functionality of table-valued functions by allowing you to define a

table-valued function in any managed language. Data is returned from a table-valued function

through an

or

object.

For table-valued functions, the columns of the return table type can't include timestamp

columns or non-Unicode string data type columns (such as

,

, and

). The

constraint isn't supported.

Transact-SQL table-valued functions materialize the results of calling the function into an

intermediate table. Since they use an intermediate table, they can support constraints and

unique indexes over the results. These features can be useful when large results are returned.

In contrast, common language runtime (CLR) table-valued functions represent a streaming

alternative. There's no requirement that the entire set of results be materialized in a single

table. The

object returned by the managed function is directly called by the

execution plan of the query that calls the table-valued function, and the results are consumed

in an incremental manner. This streaming model ensures that results can be consumed

immediately after the first row is available, instead of waiting for the entire table to be

populated. It's also a better alternative if you have large numbers of rows returned, because

they don't have to be materialized in memory as a whole. For example, a managed table-

valued function could be used to parse a text file and return each line as a row.

Implement table-valued functions as methods on a class in a.NET Framework assembly. Your

table-valued function code must implement the

interface. The

interface is defined in the.NET Framework. Types representing arrays and collections in the.NET Framework already implement the

interface. This makes it easy for writing

table-valued functions that convert a collection or an array into a result set.

```sql
IEnumerable
IEnumerator
NOT
NULL
IEnumerable
IEnumerable
IEnumerable
IEnumerable
```

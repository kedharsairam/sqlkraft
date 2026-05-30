---
name: "Generic ODBC"
title: "Generic ODBC"
category: "statements"
description: "Make sure to configure the driver to sample all the necessary data."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Key name

Default

Required

## Description

Make sure to configure the driver to sample all the necessary data.

Documents that aren't sampled don't get included in the schema

definition, and thus don't become available in ODBC applications.

Typically, sampling a large number of documents results in a schema

definition that is more accurate and better able to represent all the

data in the database. However, the sampling process might take longer

than expected when many documents are sampled, especially if the

database contains complex, nested data structures.

Forward

No

This option specifies how the driver samples data when generating a

temporary schema definition.

Forward

: The driver samples data starting from the first record in the

database, then samples the next record, and so on.

Backward

: The driver samples data starting from the last record in the

database, then samples the preceding record, and so on.

Random

: The driver selects sample records from the data source at

random until the SamplingLimit is reached.

Clear

(

)

No

This option specifies whether the driver uses SSL to connect to the

server.

Enabled

(1): The driver uses SSL to connect to the server.

Disabled

(0): The driver doesn't use SSL to connect to the server.

Valid

that you can specify for PolyBase Generic ODBC External Data Source are driver

specific. If not using a Microsoft-provided ODBC provider (see previous section), consult the driver's

documentation for valid key-value pairs.

There are some valid key-value pairs in PolyBase that are available to all generic ODBC drivers. The following

keys were added to SQL Server 2019 in CU5.

Key

Possible

values

## Description

,

Indicates whether or not the driver supports the SQLRowCount

function being called on ODBC catalog functions. Default is false. For

example:

.

,

Indicates whether or not the driver supports setting the

statement attribute. Default is false. For example:

.

,

Indicates whether or not the driver supports bind offsets for row-wise

binding of result sets. If not, use column binding. Default is false. For

example:

.

Expand table

Key

Possible

values

## Description

,

Contains information specifying how to push down the

operator

to the backend. The default is an empty string, indicating a lack of

support for

pushdown. If the user specifies

,

is used

as the format string. If the user specifies

,

is used as

the format string. This implementation is driver-specific, consult the

external data source and/or driver documentation. For example:

.

Data virtualization with PolyBase in SQL Server

CREATE EXTERNAL DATA SOURCE (Transact-SQL)

PolyBase Frequently asked questions

Related content

`SamplingStrategy`

`SSL`

```sql
0
```

`CONNECTION_OPTIONS`

```sql
PolyBaseOdbcSupportsRowCount
TRUE
```

`FALSE`

```sql
CONNECTION_OPTIONS='PolyBaseOdbcSupportsRowCount=TRUE'
```

```sql
PolyBaseOdbcSupportsMetadataIdAttributes
TRUE
```

`FALSE`

`METADATA_ID`

```sql
CONNECTION_OPTIONS='PolyBaseOdbcSupportsMetadataIdAttributes=TRUE'
```

```sql
PolyBaseOdbcSupportsBindOffset
TRUE
```

`FALSE`

```sql
CONNECTION_OPTIONS='PolyBaseOdbcSupportsBindOffset=TRUE'
```

```sql
PolyBaseQoTopPushdownSyntax
TOP
```

`LIMIT`

`TOP`

`TOP`

`TOP`

```sql
top {0}
```

`LIMIT`

```sql
limit {0}
```

```sql
CONNECTION_OPTIONS=PolyBaseQoTopPushdownSyntax=TOP'
```

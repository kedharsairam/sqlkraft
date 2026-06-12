---
name: "FOR XML"
title: "FOR XML"
category: "queries"
description: "Specifies that the results of a query are to be returned as an XML document."
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

## XML

## RAW [ ('

## ElementName

## ') ]

## AUTO

## EXPLICIT

## XMLDATA

Specifies that the results of a query are to be returned as an XML document. One of the

following XML modes must be specified:

,

,. For more information about

XML data and SQL Server, see

FOR XML (SQL Server).

Takes the query result and transforms each row in the result set into an XML element with a

generic identifier

as the element tag. You can optionally specify a name for the row

element. The resulting XML output uses the specified

as the row element

generated for each row. For more information, see

Use RAW mode with FOR XML.

## Returns query results in a simple, nested XML tree. Each table in the

clause, for which at

least one column is listed in the

clause, is represented as an XML element. The columns

listed in the

clause are mapped to the appropriate element attributes. For more

information, see

Use AUTO mode with FOR XML.

Specifies that the shape of the resulting XML tree is defined explicitly. Using this mode, you

must write queries in a particular way so that they specify additional information about the

desired nesting explicitly. For more information, see

Use EXPLICIT mode with FOR XML.

## Returns inline XDR schema, but doesn't add the root element to the result. If you specify

, the XDR schema is appended to the document.

If the columns that are included in the unique index don't accept

values, all the

values in the result set were introduced by the

statement.

）

Important

### Suppress unwanted line breaks

### True

### The

#### XMLDATA

### directive is deprecated.

## XMLSCHEMA [ ('

## TargetNameSpaceURI

## ') ]

## ELEMENTS

## XSINIL

: You might use SQL Server Management Studio (SSMS) to run

a query that uses the

clause. Sometimes a large amount of XML is returned and

displayed in one grid cell. The XML string could be longer than one SSMS grid cell can hold on

a single line. In these cases, SSMS might insert line break characters between long segments of

the whole XML string. Such line breaks might occur in the middle of a substring that shouldn't

be split across lines. You can prevent the line breaks by using a cast. This solution

can also apply when you use

, as in the following Transact-SQL sample

statement:

## Returns inline XSD schema. You can optionally specify a target namespace URI when you

specify this directive, which returns the specified namespace in the schema. For more

information, see

Generate an inline XSD schema.

Specifies that the columns are returned as subelements. Otherwise, the query maps them to

XML attributes. This option is supported in

,

, and

modes only. For more

information, see

Use RAW mode with FOR XML.

Specifies that an element with

attribute set to

is created for

column values.

You can only specify this option with the

directive. For more information, see:

Generate elements for NULL values with the XSINIL parameter.

Use XSD generation for

and

modes.

There's no replacement for the

directive in

mode. This feature will be

removed in a future version of SQL Server. Avoid using this feature in new development

work, and plan to modify applications that currently use this feature.

## ABSENT

## PATH [ ('

## ElementName

## ') ]

## BINARY BASE64

## TYPE

## ROOT [ ('

## RootName

## ') ]

## Example

FOR XML (SQL Server)

Indicates that for

column values, corresponding XML elements aren't added in the XML

result. Specify this option only with.

Generates a

element wrapper for each row in the result set. You can optionally specify

an element name for the

element wrapper. If you provide an empty string, such as

, a wrapper element isn't generated. Using

might provide a simpler

alternative to queries written using the

directive. For more information, see

Use PATH

mode with FOR XML.

Specifies that the query returns the binary data in binary base64-encoded format. When you

retrieve binary data by using

and

mode, you must specify this option. This

option is the default in

mode.

Specifies that the query returns results as

type. For more information, see

TYPE directive in

FOR XML queries.

Specifies that a single top-level element is added to the resulting XML. You can optionally

specify the name of the root element to generate. If you don't specify the root name, the

default

element is added.

For more information, see

FOR XML (SQL Server).

The following example specifies

with the

and

options. Because

of the

option, the query returns the result set to the client as an

type. The

option specifies that the inline XSD schema is included in the XML data returned, and the

option specifies that the XML result is element-centric.

`RAW`

`AUTO`

`EXPLICIT`

```sql
<row />
```

`ElementName`

`FROM`

`SELECT`

`SELECT`

`XMLDATA`

`NULL`

`NULL`

```sql
RIGHT OUTER JOIN
```

```sql
FOR XML
```

```sql
AS XMLDATA
```

```sql
FOR JSON PATH
```

`SELECT`

`RAW`

`AUTO`

`PATH`

```sql
xsi:nil
```

`NULL`

`ELEMENTS`

`RAW`

`AUTO`

`XMLDATA`

`EXPLICIT`

```sql
SELECT
CAST (
(
SELECT column1,
column2
FROM my_table
FOR
XML
PATH (
''
))
AS
VARCHAR (
MAX
)
)
AS
XMLDATA;
```

`NULL`

`ELEMENTS`

```sql
<row>
```

```sql
<row>
```

```sql
FOR
XML PATH (''))
```

`PATH`

`EXPLICIT`

`RAW`

`EXPLICIT`

`AUTO`

```sql
<root>
```

```sql
FOR XML AUTO
```

`TYPE`

`XMLSCHEMA`

`TYPE`

`XMLSCHEMA`

`ELEMENTS`

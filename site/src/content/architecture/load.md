---
title: "Load"
topic: "xml-data"
description: "You can transfer XML data into SQL Server in several ways. For example: If you have your data in an [n]text or image column in a S"
tags: ["xml-data","load"]
pubDate: "2025-12-01"
---

You can transfer XML data into SQL Server in several ways. For example:

If you have your data in an [n]text or image column in a SQL Server database, you can

import the table by using Integration Services. Change the column type to XML by using

the ALTER TABLE statement.

You can bulk copy your data from another SQL Server database by using bcp out, and

then bulk insert the data into the later version database by using bcp in.

If you have data in relational columns in a SQL Server database, create a new table with

an [n]text column and, optionally, a primary key column for a row identifier. Use client-

side programming to retrieve the XML that is generated at the server with FOR XML and

write it into the

column. Then, use the previously mentioned techniques to

transfer data to a later version database. You can choose to write the XML into an XML

column in the later version database directly.

You can bulk load XML data into the server by using the bulk loading capabilities of SQL Server,

such as bcp. OPENROWSET allows you to load data into an XML column from files. The

following example illustrates this point.

This example shows how to insert a row in table T. The value of the XML column is loaded from

file

as CLOB, and the integer column is supplied the value 10.

```sql
C:\MyFile\xmlfile.xml
INSERT
INTO
T
SELECT
10, xCol
FROM (
SELECT
*
FROM
OPENROWSET (
BULK
'C:\MyFile\xmlfile.xml'
, SINGLE_BLOB)
AS xCol)
AS
R(xCol);
```

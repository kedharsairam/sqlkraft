---
title: "Updating UDT columns with DataAdapters"
topic: "clr-integration"
description: |
  Applies to:
  
  SQL Server
  
  You can retrieve and modify user-defined types (UDTs) by using a
  
  and a
  
  .
  
  The code examples in this article use
  
  , which is available as a NuGet
  
  package. To add this depend
tags:
  - "clr-integration"
  - "updating-udt-columns-with-dataadapters"
pubDate: 2025-12-01
---

Applies to:

SQL Server

You can retrieve and modify user-defined types (UDTs) by using a

and a

.

The code examples in this article use

, which is available as a NuGet

package. To add this dependency to your project, run the following command:

Use a Transact-SQL

statement to select UDT column values to populate a dataset by

using a data adapter. The following example assumes that you have a

table defined

with the following structure and some sample data. The following Transact-SQL statements

create the

table and insert a few rows.

SQL

The following ADO.NET code fragment retrieves a valid connection string, creates a new

, and populates a

with the rows of data from the

```sql
System.Data.DataSet
Microsoft.Data.SqlClient.SqlDataAdapter
Microsoft.Data.SqlClient
SELECT
Points
Points
SqlDataAdapter
System.Data.DataTable
Points
dotnet
add
package Microsoft.Data.SqlClient
CREATE
TABLE
dbo.Points
(
id
INT
PRIMARY
KEY
,
p Point
);
INSERT
INTO
dbo.Points
VALUES
(1,
CONVERT
(Point,
'1,3'
));
INSERT
INTO
dbo.Points
VALUES
(2,
CONVERT
(Point,
'2,4'
));
INSERT
INTO
dbo.Points
VALUES
(3,
CONVERT
(Point,
'3,5'
));
INSERT
INTO
dbo.Points
VALUES
(4,
CONVERT
(Point,
'4,6'
));
GO
```
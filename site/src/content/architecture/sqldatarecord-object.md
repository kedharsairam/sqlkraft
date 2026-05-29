---
title: "SqlDataRecord Object"
topic: "clr-integration"
description: |
  SqlDataRecord object

  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  In the .NET common language runtime (CLR), the

  object represents a single row

  of data, along with its related metadata.

  Manage
tags:
  - "clr-integration"
  - "sqldatarecord-object"
pubDate: 2025-12-01
---

SqlDataRecord object

Article

•

12/30/2024

Applies to:

SQL Server

In the .NET common language runtime (CLR), the

object represents a single row

of data, along with its related metadata.

Managed stored procedures might send to the client result sets that aren't from a

. The

class, along with

,

, and

methods of the

object, allows stored procedures to send custom

result sets to the client.

For more information, see

Microsoft.SqlServer.Server.SqlDataRecord

.

The following example creates a new employee record and returns it to the caller.

C#

```sql
SqlDataRecord
SqlDataReader
SqlDataRecord
SendResultsStart
SendResultsRow
SendResultsEnd
SqlPipe
[Microsoft.SqlServer.Server.SqlProcedure]
public static void CreateNewRecordProc()
{
// Variables.
SqlDataRecord record;
// Create a new record with the column metadata.  The constructor
// is able to accept a variable number of parameters.
record = new SqlDataRecord(new SqlMetaData("EmployeeID", SqlDbType.Int),
new SqlMetaData("Surname", SqlDbType.NVarChar,
20),
new SqlMetaData("GivenName",
SqlDbType.NVarChar, 20),
new SqlMetaData("StartDate",
SqlDbType.DateTime) );
// Set the record fields.
record.SetInt32(0, 0042);
record.SetString(1, "Funk");
record.SetString(2, "Don");
record.SetDateTime(3, new DateTime(2005, 7, 17));
// Send the record to the calling program.
SqlContext.Pipe.Send(record);
```

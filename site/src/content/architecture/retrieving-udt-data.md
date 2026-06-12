---
title: "Retrieving UDT data"
topic: "clr-integration"
description: "To create a user-defined type (UDT) on the client, the assembly registered as a UDT in a SQL Server database must be available to the client application."
tags: ["clr-integration","retrieving-udt-data"]
pubDate: 2025-12-01
---

To create a user-defined type (UDT) on the client, the assembly registered as a UDT in a SQL

Server database must be available to the client application. The UDT assembly can be placed in

the same directory with the application, or in the Global Assembly Cache (GAC). You can also

set a reference to the assembly in your project.

The assembly loaded in SQL Server and the assembly on the client must be compatible for the

UDT to be created on the client. For UDTs defined with the

serialization format, the

assemblies must be structurally compatible. For assemblies defined with the

format, the assembly must be available on the client.

You don't need a copy of the UDT assembly on the client to retrieve the raw data from a UDT

column in a table.

The code examples in this article use

, which is available as a NuGet

package. To add this dependency to your project, run the following command:

Use a

from client code to retrieve a result set that

contains a UDT column, which is exposed as an instance of the object.

７

Note

might fail to load a UDT if UDT versions are mismatched or other problems

occur. In this case, use regular troubleshooting mechanisms to determine why the

assembly containing the UDT can't be found by the calling application. For more

information, see.

```sql
Native
UserDefined
Microsoft.Data.SqlClient
Microsoft.Data.SqlClient.SqlDataReader
SqlClient dotnet add package Microsoft.Data.SqlClient
```

---
name: 'sys.sp_data_source_table_columns'
title: 'sys.sp_data_source_table_columns'
category: 'general'
description: 'SQL Server 2019 (15.x)'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

Teradata

MongoDB

Azure Cosmos DB

The stored procedure doesn't support generic ODBC data source or Hadoop connectors.

The notion of empty vs. non-empty relates to the behavior of the ODBC driver and the

SQLTables

function. Non-empty indicates an object contains tables, not rows. For example, an

empty schema contains no tables in SQL Server. An empty database contains with no tables

inside Teradata. The results are a SQL Server representation of the backend schema as

interpreted by the PolyBase connector for the backend. The distinction here is that instead of

merely passing along the results of the ODBC call to the backend, the results are based on the

outcome of the PolyBase type-mapping code.

Use

sp_data_source_objects

and

to discover external objects.

These system stored procedures return the schema of tables that are available to be virtualized.

Use

to discover external table schemas represented in SQL

Server data types.

Due to differences between collations in Hadoop source data and supported collations in SQL

Server 2019 (15.x), the recommended data type lengths for varchar data type columns in

external tables might be much larger than expected. This is by design.

Oracle synonyms aren't supported for usage with PolyBase.

The following example returns the table columns for an external table in a SQL Server named

, belonging to a schema named

.

SQL

Data virtualization with PolyBase in SQL Server

System stored procedures (Transact-SQL)

Related content

CREATE EXTERNAL TABLE AS SELECT (CETAS) (Transact-SQL)

CREATE EXTERNAL TABLE (Transact-SQL)

Last updated on 01/29/2026

```sql
sp_data_source_table_columns
```

```sql
sp_data_source_table_columns
```

```sql
server
```

```sql
schema
```

```sql
DECLARE
@data_source
AS
SYSNAME = N
'ExternalDataSourceName'
;
DECLARE
@table_location
AS
NVARCHAR
(400) = N
'[database].[schema].[table]'
;
EXECUTE
sp_data_source_table_columns
@data_source,
@table_location;
```

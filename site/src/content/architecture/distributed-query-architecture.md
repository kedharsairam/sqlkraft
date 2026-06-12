---
title: "Distributed query architecture"
topic: "query-processing"
description: "operations, where each key range is estimated to cover similar numbers of rows. For"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

operations, where each key range is estimated to cover similar numbers of rows. For

example, if there are four million rows in the table and the degree of parallelism is 4, the

coordinating worker thread will determine the key values that delimit four sets of rows

with 1 million rows in each set. If enough key ranges can't be established to use all CPUs,

the degree of parallelism is reduced accordingly.

The coordinating worker thread dispatches a number of worker threads equal to the

degree of parallel operations and waits for these worker threads to complete their work.

Each worker thread scans the base table using a filter that retrieves only rows with key

values within the range assigned to the worker thread. Each worker thread builds an index

structure for the rows in its key range. In the case of a partitioned index, each worker

thread builds a specified number of partitions. Partitions aren't shared among worker

threads.

After all the parallel worker threads have completed, the coordinating worker thread

connects the index subunits into a single index. This phase applies only to offline index

operations.

Individual

or

statements can have multiple constraints that require

that an index be created. These multiple index creation operations are performed in series,

although each individual index creation operation might be a parallel operation on a computer

that has multiple CPUs.

Microsoft SQL Server supports two methods for referencing heterogeneous OLE DB data

sources in Transact-SQL statements:

Linked server names

The system stored procedures

and

are used to

give a server name to an OLE DB data source. Objects in these linked servers can be

referenced in Transact-SQL statements using four-part names. For example, if a linked

server name of

is defined against another instance of SQL Server, the

following statement references a table on that server:

The linked server name can also be specified in an

statement to open a rowset

from the OLE DB data source. This rowset can then be referenced like a table in Transact-

SQL statements.

Ad hoc connector names

For infrequent references to a data source, the

or

functions

are specified with the information needed to connect to the linked server. The rowset can

then be referenced the same way a table is referenced in Transact-SQL statements:

uses OLE DB to communicate between the relational engine and the storage

engine. The relational engine breaks down each Transact-SQL statement into a series of

operations on simple OLE DB rowsets opened by the storage engine from the base tables. This

means the relational engine can also open simple OLE DB rowsets on any OLE DB data source.

The relational engine uses the OLE DB application programming interface (API) to open the

rowsets on linked servers, fetch the rows, and manage transactions.

For each OLE DB data source accessed as a linked server, an OLE DB provider must be present

on the server running SQL Server. The set of Transact-SQL operations that can be used against

a specific OLE DB data source depends on the capabilities of the OLE DB provider.

For each instance of SQL Server, members of the

fixed server role can enable or

disable the use of ad hoc connector names for an OLE DB provider using the SQL Server

property. When ad hoc access is enabled, any user logged on to that

instance can execute Transact-SQL statements containing ad hoc connector names, referencing

any data source on the network that can be accessed using that OLE DB provider. To control

access to data sources, members of the

role can disable ad hoc access for that OLE

```sql
CREATE TABLE
```

```sql
ALTER TABLE
```

`sp_addlinkedserver`

`sp_addlinkedsrvlogin`

`DeptSQLSrvr`

`OPENQUERY`

```sql
SELECT
JobTitle, HireDate
FROM
DeptSQLSrvr.AdventureWorks2022.HumanResources.Employee;
```

`OPENROWSET`

`OPENDATASOURCE`

`sysadmin`

`DisallowAdhocAccess`

`sysadmin`

```sql
SELECT
*
FROM
OPENROWSET(
'Microsoft.Jet.OLEDB.4.0'
,
'c:\MSOffice\Access\Samples\Northwind.mdb'
;'Admin';'';
Employees);
```

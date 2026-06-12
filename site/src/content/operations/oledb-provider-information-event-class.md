---
title: "OLEDB Provider Information Event Class"
topic: "event-classes"
description: ""
tags: ["event-classes","oledb-provider-information-event-class"]
pubDate: "2025-12-01"
---

The

event class occurs when a distributed query is run and

collects information corresponding to the provider connection.

This event class contains all the properties that are collected from the remote provider by using

various property sets, including the following:

DBPROPSET_DATASOURCEINFO

SQLPROPSET_OPTHINTS

DBPROPSET_SQLSERVERDATASOURCEINFO (SQL Server only)

DBPROPSET_SQLSERVERDBINIT (SQL Server only)

DBPROPSET_ROWSET

IDBInfo interface

These properties, along with available metadata, are used by the query optimizer to choose the

optimal execution plan for the query. This information is useful for tracing execution and

analyzing OLE DB calls and events in distributed query profiler traces.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

ﾉ

Expand table

---
title: "Analyze Script Performance"
topic: "ssb-diagnose"
description: |
  09/10/2025
          
            You can use the tools provided by SQL Server Data Tools to determine whether you can
          
            improve the performance of your query, stored procedures, or scripts. For example, by
          
            monitoring clie
tags: ["ssb-diagnose","analyze-script-performance"]
pubDate: 2025-12-01
---

You can use the tools provided by SQL Server Data Tools to determine whether you can

improve the performance of your query, stored procedures, or scripts. For example, by

monitoring client statistics such as the response times for frequently used queries, you can

determine whether changes to the query or indexes on the tables are required. Such statistics

can include client execution time, query profile, and packets/bytes sent and received.

In addition, certain performance problems are better addressed by analyzing the application

queries and updates that the application submits to the database, and how these queries and

updates interact with the data contained in the database and the database schema. Execution

plans graphically display the data retrieval methods chosen by the SQL Server query optimizer,

and show the execution cost of specific statements and queries. Thus they can help you

understand how SQL Server processes your SQL query, and determine what is causing

performance slowdown.

When you run a script or query in the Transact-SQL Editor, you can choose to collect client

statistics such as application profile, network, and time statistics for the execution. Such metrics

allow you to gauge the efficiency of your script, or benchmark different scripts.

To toggle the gathering of client statistics, when the Transact-SQL Editor is open, on the

menu, point to

, select

and.

Alternatively, select the

button (the fifth one from the right) on the

Transact-SQL Editor toolbar, or by right-clicking in the Transact-SQL editor and then selecting

and. In order to gather statistics for a query, you

have to turn on this feature before executing it.

If you turned on client statistics, the

tab appears next to the

tab upon query

execution. If you turned off client statistics, the

tab doesn't appear. Statistics from

successive query executions are listed along with the average values.

For more information on the statistics collected, see

Query Window Statistics pane

and

Client

Statistics Tab.

Execution plans display how the database engine navigates tables and uses indexes to access

or process the data for a query or other DML statement, such as an update. This graphical

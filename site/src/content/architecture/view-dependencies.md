---
title: "View dependencies"
topic: "spatial-data"
description: "This topic describes how to view s"
tags: ["spatial-data","view-dependencies"]
pubDate: "2025-12-01"
---

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

This topic describes how to view stored procedure dependencies in SQL Server by using SQL

Server Management Studio or Transact-SQL.

Limitations and Restrictions

,

Security

Management Studio

,

Transact-SQL

System Function:

Requires CONTROL permission on the referenced entity and SELECT permission on

sys.dm_sql_referencing_entities. When the referenced entity is a partition function, CONTROL

permission on the database is required. By default, SELECT permission is granted to public.

System Function:

Requires SELECT permission on sys.dm_sql_referenced_entities and VIEW DEFINITION

permission on the referencing entity. By default, SELECT permission is granted to public.

Requires VIEW DEFINITION permission on the database or ALTER DATABASE DDL TRIGGER

permission on the database when the referencing entity is a database-level DDL trigger.

Requires VIEW ANY DEFINITION permission on the server when the referencing entity is a

server-level DDL trigger.

Object Catalog View:

Requires VIEW DEFINITION permission on the database and SELECT permission on

sys.sql_expression_dependencies for the database. By default, SELECT permission is granted

only to members of the db_owner fixed database role. When SELECT and VIEW DEFINITION

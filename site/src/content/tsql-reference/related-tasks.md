---
name: "Related tasks"
title: "Related tasks"
category: "statements"
description: "The following example creates a server audit called"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

The following example creates a server audit called

and then

a database audit specification called

that audits

,

, and

statements by users in a new database role

, for all objects

in the

schema.

Server audit specifications:

CREATE SERVER AUDIT SPECIFICATION (Transact-SQL)

ALTER SERVER AUDIT SPECIFICATION (Transact-SQL)

DROP SERVER AUDIT SPECIFICATION (Transact-SQL)

Database audit specifications:

CREATE DATABASE AUDIT SPECIFICATION (Transact-SQL)

ALTER DATABASE AUDIT SPECIFICATION (Transact-SQL)

DROP DATABASE AUDIT SPECIFICATION (Transact-SQL)

Catalog views and DMVs:

sys.server_audits (Transact-SQL)

sys.server_file_audits (Transact-SQL)

sys.server_audit_specifications (Transact-SQL)

sys.server_audit_specification_details (Transact-SQL)

sys.database_audit_specifications (Transact-SQL)

sys.database_audit_specification_details (Transact-SQL)

Create a Server Audit and Server Audit Specification

CREATE SERVER AUDIT (Transact-SQL)

ALTER SERVER AUDIT (Transact-SQL)

DROP SERVER AUDIT (Transact-SQL)

ALTER AUTHORIZATION (Transact-SQL)

sys.fn_get_audit_file (Transact-SQL)

sys.dm_server_audit_status (Transact-SQL)

sys.dm_audit_actions (Transact-SQL)

Related content

`DataModification_Security_Audit`

`Audit_Data_Modification_On_All_Sales_Tables`

`INSERT`

`UPDATE`

`DELETE`

`SalesUK`

`Sales`

```sql
WITH (STATE = ON);
GO
```

```sql
USE master
;
GO
-- Create the server audit.
-- Change the path to a path that the SQLServer Service has access to.
CREATE
SERVER
AUDIT
DataModification_Security_Audit
TO
FILE (FILEPATH =
'D:\SQLAudit\'); -- make sure this path exists
GO
-- Enable the server audit.
ALTER SERVER AUDIT DataModification_Security_Audit
WITH (STATE = ON);
GO
-- Move to the target database.
USE AdventureWorks2022;
GO
CREATE ROLE SalesUK
GO
-- Create the database audit specification.
CREATE DATABASE AUDIT SPECIFICATION Audit_Data_Modification_On_All_Sales_Tables
FOR SERVER AUDIT DataModification_Security_Audit ADD (
INSERT, UPDATE, DELETE ON SCHEMA::Sales BY SalesUK
)
WITH (STATE = ON);
GO
```

---
title: "Service Script Example"
topic: "service-broker"
description: |
  09/15/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  This Transact-SQL code sample defines a service that archives untyped XML documents. Two
  
  scripts are included: the contract script and
tags:
  - "service-broker"
  - "service-script-example"
pubDate: 2025-12-01
---

09/15/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This Transact-SQL code sample defines a service that archives untyped XML documents. Two

scripts are included: the contract script and the service-definition script. The contract script

defines the message types and the contract for the service. The message-type definition and

the contract definition should match for both the initiating service and the target service.

Therefore, the definitions are included in a separate service-definition script that can be

distributed to the databases that host the initiating service. The service-definition script defines

the service itself. This script should be run only in a database that implements the target

service.

SQL

７

Note

The service-definition script defines the target service, but doesn't include an

implementation of the service.

７

Note

The code samples in this article were tested using the

sample

database, which you can download from the

home page.

```sql
AdventureWorks2022
-- The contract script contains definitions that must be present
-- for both the initiating service and the target service.
USE
AdventureWorks2008R2;
GO
-- Create messages for each broker-to-broker
-- communication needed to complete the task.
-- Message for the initiator to send XML
-- to be archived.
CREATE
MESSAGE
TYPE
[//Adventure-Works.com/messages/ArchiveXML]
VALIDATION
= WELL_FORMED_XML;
GO
```
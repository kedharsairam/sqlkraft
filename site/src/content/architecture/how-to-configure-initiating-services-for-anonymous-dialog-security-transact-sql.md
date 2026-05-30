---
title: "How to: Configure Initiating Services for Anonymous Dialog Security (Transact-SQL)"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  SQL Server uses dialog security for any conversation to a service for which a remote service

  binding exists. If the database that host
tags:
  - "service-broker"
  - "how-to-configure-initiating-services-for-anonymous-dialog-security-transact-sql"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server uses dialog security for any conversation to a service for which a remote service

binding exists. If the database that hosts the target service doesn't contain a user that

corresponds to the user that created the dialog, the dialog uses anonymous security.

1. Obtain a certificate for a user in the remote database from a trusted source.

2. Create a user without a login.

3. Install the certificate for the remote service. The user created in step 3 owns the

certificate. By default the certificate is active for

.

4. Create a remote service binding that specifies the user and the target service. For

anonymous dialog security, the remote service binding specifies

.

This example configures anonymous dialog security for conversations between the service

named

in the current instance and the service named

in the

remote instance.

７

Note

Only install certificates from trusted sources.

７

Note

The code samples in this article were tested using the

sample

database, which you can download from the

home page.

```sql
BEGIN DIALOG
ANONYMOUS = ON
OrderParts
SupplierOrders
AdventureWorks2022
```

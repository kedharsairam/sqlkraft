---
title: "Example: Configure with Windows Authentication (T-SQL)"
topic: "high-availability"
description: "SQL) This example shows all the stages required to create a database mirroring session with a witness using Windows Authentication. The examples in t"
tags: ["high-availability","example-configure-with-windows-authentication-t-sql"]
pubDate: "2025-12-01"
---

SQL)

This example shows all the stages required to create a database mirroring session with a

witness using Windows Authentication. The examples in this topic use Transact-SQL. Note that

as an alternative to using Transact-SQL steps, you can use the Configure Database Mirroring

Security Wizard for database mirroring setup. For more information, see

Establish a Database

Mirroring Session Using Windows Authentication (SQL Server Management Studio).

The example uses the

sample database, which uses the simple recovery

model by default. To use database mirroring with this database, you must alter it to use the full

recovery model. To do this in Transact-SQL, use the ALTER DATABASE statement, as follows:

For information on changing the recovery model in SQL Server Management Studio, see

View

or Change the Recovery Model of a Database (SQL Server).

Requires ALTER permission on the database and CREATE ENDPOINT permission, or

membership in the

fixed server role.

In this example, the two partners and the witness are the default server instances on three

computer systems. The three server instances run the same Windows domain, but the user

```cmd
USE master;
GO
ALTER DATABASE AdventureWorks
SET RECOVERY FULL;
GO
```

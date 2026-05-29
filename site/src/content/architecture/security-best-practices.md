---
title: "Security best practices"
topic: "collation"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Contained databases have some unique threats that should be understood and mitigated by
  
  SQL Server Database Engine adminis
tags:
  - "collation"
  - "security-best-practices"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Managed Instance

Contained databases have some unique threats that should be understood and mitigated by

SQL Server Database Engine administrators. Most of the threats are related to the

authentication process, which moves the authentication boundary from the

Database Engine level to the database level.

Users in a contained database that have the

permission, such as members of

the

and

fixed database roles, can grant access to the database

without the knowledge or permission or the SQL Server administrator. Granting users access to

a contained database increases the potential attack surface area against the whole SQL Server

instance. Administrators should understand this delegation of access control, and be very

careful about granting users in the contained database the

permission. All

database owners have the

permission. SQL Server administrators should

periodically audit the users in a contained database.

Database owners and database users with the

permission can create

contained database users. After connecting to a contained database on an instance of SQL

Server, a contained database user can access other databases on the Database Engine, if the

other databases have enabled the

account.

Some applications might require that a user to have access to more than one database. This

can be done by creating identical contained database users in each database. Use the SID

option when creating the second user with password. The following example creates two

identical users in two databases.

```sql
USE DB1;
GO
CREATE USER Carlo WITH PASSWORD = '<strong password>';
```
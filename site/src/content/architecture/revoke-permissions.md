---
title: "Revoke Permissions"
topic: "xml-data"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  The permission to create an XML schema collection can be revoked by using one of the

  following:

  Revok
tags:
  - "xml-data"
  - "revoke-permissions"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The permission to create an XML schema collection can be revoked by using one of the

following:

Revoke the ALTER permission for the relational schema. Then, the principal can't create an

XML schema collection in the relational schema. However, the principal can still do so in

other relational schemas in the same database.

Revoke the ALTER ANY SCHEMA permission on the database for the principal. Then, the

principal can't create an XML schema collection anywhere in the database.

Revoke the CREATE XML SCHEMA COLLECTION or ALTER XML SCHEMA COLLECTION

permission on the database for the principal. This prevents the principal from importing

an XML schema collection within the database. Revoking the ALTER or CONTROL

permission on the database has the same effect.

Following are the permissions that can be revoked on an XML schema collection and the

results:

Revoking the ALTER permission revokes a principal's ability to modify the content of the

XML schema collection.

Revoking the TAKE OWNERSHIP permission revokes a principal's ability to transfer

ownership of the XML schema collection.

Revoking the REFERENCES permission revokes a principal's ability to use the XML schema

collection for typing or constraining xml type columns, in tables and views, and

parameters. It also revokes the permission to refer to this schema collection from other

XML schema collections.

Revoking the VIEW DEFINITION permission revokes a principal's ability to view the

contents of an XML schema collection.

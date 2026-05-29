---
title: "Deny Permissions"
topic: "xml-data"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  Permission can be denied to either create a new XML schema collection or use an existing one.
tags:
  - "xml-data"
  - "deny-permissions"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Permission can be denied to either create a new XML schema collection or use an existing one.

You can deny permission to create an XML schema collection in the following ways:

Deny ALTER permission on the relational schema.

Deny CONTROL on the relational schema to deny all permissions on the relational

schema and on all the contained objects.

Deny ALTER ANY SCHEMA on the database. In this case, the principal can't create an XML

schema collection anywhere in the database. Note also that denying ALTER or CONTROL

permission on the database denies all permissions on all objects in the database.

Following are the permission that can be denied on an existing XML schema collection and the

results:

Denying the ALTER permission denies the principal the ability to modify the contents of

the XML schema collection.

Denying the CONTROL permission denies the principal the ability to perform any

operation on the XML schema collection.

Denying the REFERENCES permission denies the principal the ability to type or constrain

xml type columns and parameters using the XML schema collection. It also denies the

principal the ability to refer to this XML schema collection from other XML schema

collections.

Denying the VIEW DEFINITION permission denies the principal the ability to view the

contents of an XML schema collection.
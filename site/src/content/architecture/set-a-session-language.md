---
title: "Set a session language"
topic: "collation"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The session language can be used to set how the following elements are displayed on the
  
  serv
tags:
  - "collation"
  - "set-a-session-language"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The session language can be used to set how the following elements are displayed on the

server, based on language and cultural preference:

The language that will be used for error and other system messages. SQL Server supports

having multiple copies of all system error strings and messages in all the languages in

which SQL Server is available. These messages can be viewed in the

sys.messages

catalog

view. When you install a localized version of SQL Server, these system messages are

translated for the language version that you install. By default, you also obtain the U.S.

English set of these messages. Additionally, you can add user-defined messages in a

specific language by using

sp_addmessage

.

The format of date and time data.

The names of days and months, including abbreviations.

The first day of the week.

Currency data.

There are 33 languages available for use as session settings. For a list of languages, see

sys.syslanguages

.

To set the session language from the server side, use

SET LANGUAGE

.

The session language can be set on the client side by using OLE DB, ODBC or ADO.NET. For

OLE DB, use the SSPROP_INIT_CURRENTLANGUAGE property. For more information, see

Initialization and Authorization Properties

.

For ODBC, use the Language keyword. For more information, see

SQLConfigDataSource

.

For ADO.NET, use the

parameter of the

object. For more

information, see the Microsoft Data Access Components (MDAC) software development kit

(SDK) documentation.
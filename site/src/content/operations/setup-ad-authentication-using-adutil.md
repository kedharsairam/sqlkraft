---
title: "Setup AD Authentication using adutil"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This tutorial explains how to configure SQL Server on Linux containers to support Active Directory

  authentication, also known as integrated authentication. For an o
tags:
  - "linux-operations"
  - "setup-ad-authentication-using-adutil"
pubDate: 2025-12-01
---

SQL Server

on Linux

This tutorial explains how to configure SQL Server on Linux containers to support Active Directory

authentication, also known as integrated authentication. For an overview, see

Active Directory

authentication for SQL Server on Linux.

This tutorial consists of the following tasks:

The following are required before configuring Active Directory authentication:

Have an Active Directory Domain Controller (Windows) in your network.

Install

on a Linux host machine, which is joined to a domain. Follow the

Install adutil

section for details.

７

Note

For current guidance about network configuration, refer to the documentation for your

operating system (OS).

Install

＂

Join Linux host to Active Directory domain

＂

Create an Active Directory user for SQL Server and set the Service Principal Name (SPN)

using the

tool

＂

Create the SQL Server service keytab file

＂

Create the

and

files to be used by the SQL Server container

＂

Mount the config files and deploy the SQL Server container

＂

Create Active Directory-based SQL Server logins using Transact-SQL

＂

Connect to SQL Server using Active Directory authentication

＂

```cmd
mssql.conf krb5.conf
```

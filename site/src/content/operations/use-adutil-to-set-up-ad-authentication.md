---
title: "Use adutil to set up AD Authentication"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This tutorial explains how to configure Windows Active Directory authentication for SQL Server

  on Linux using

  . For another method of configuring Active Directory
tags:
  - "linux-operations"
  - "use-adutil-to-set-up-ad-authentication"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

This tutorial explains how to configure Windows Active Directory authentication for SQL Server

on Linux using

. For another method of configuring Active Directory authentication using

, see

Tutorial: Use Active Directory authentication with SQL Server on Linux

.

This tutorial consists of the following tasks:

Before configuring Active Directory authentication, you need:

A Windows Domain Controller running Active Directory Domain Services in your network.

The

tool installed on a domain-joined host machine.

Make sure there's a forwarding host (A) entry added in Active Directory for the Linux host IP

address. In this tutorial, the IP address of

host machine is

. We add the forwarding

host entry in Active Directory in the following example. The entry ensures that when users

connect to

, it reaches the right host.

Install

＂

Join Linux machine to your Active Directory domain

＂

Create an Active Directory user for SQL Server and set the Service Principal Name (SPN)

using

＂

Create the SQL Server service keytab (key table) file

＂

Configure SQL Server to use the keytab file

＂

Create Active Directory-based SQL Server logins using Transact-SQL

＂

Connect to SQL Server using Active Directory authentication

＂

```cmd
sql1
10.0.0.10
sql1.contoso.com
```

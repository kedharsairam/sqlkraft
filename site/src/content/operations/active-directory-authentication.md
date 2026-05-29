---
title: "Active Directory authentication"
topic: "linux-operations"
description: |
  07/03/2025

  Applies to:

  SQL Server

  - Linux

  This article provides an overview of Active Directory authentication for SQL Server on Linux.

  Active Directory authentication is also known as Integrated
tags:
  - "linux-operations"
  - "active-directory-authentication"
pubDate: 2025-12-01
---

07/03/2025

Applies to:

SQL Server

- Linux

This article provides an overview of Active Directory authentication for SQL Server on Linux.

Active Directory authentication is also known as Integrated authentication in SQL Server.

Active Directory authentication enables domain-joined clients on either Windows or Linux to

authenticate to SQL Server using their domain credentials and the Kerberos protocol.

Active Directory Authentication has the following advantages over SQL Server Authentication:

Users authenticate via single sign-on, without being prompted for a password.

By creating logins for Active Directory groups, you can manage access and permissions in

SQL Server using Active Directory group memberships.

Each user has a single identity across your organization, so you don't have to keep track

of which SQL Server logins correspond to which people.

Active Directory enables you to enforce a centralized password policy across your

organization.

In order to use Active Directory authentication, you must have an Active Directory Domain

Controller (Windows) on your network.

The details for how to configure Active Directory authentication are provided in the tutorial,

Tutorial: Use Active Directory authentication with SQL Server on Linux

. The following list

provides a summary with a link to each section in the tutorial:

1.

Join SQL Server on a Linux host to an Active Directory domain

.

2.

Create an Active Directory user for SQL Server and set the Service Principal Name

.

3.

Configure the SQL Server service keytab

.

4.

Secure the keytab file

.

5.

Configure SQL Server to use the keytab file for Kerberos authentication

.

6.

Create Active Directory-based SQL Server logins in Transact-SQL

.

7.

Connect to SQL Server using Active Directory authentication

.

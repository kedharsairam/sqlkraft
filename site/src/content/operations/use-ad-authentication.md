---
title: "Use AD authentication"
topic: "linux-operations"
description: "on Linux This tutorial explains how to configure SQL Server on Linux to support Active Directory authentication, also known as integrated authentication."
tags: ["linux-operations","use-ad-authentication"]
pubDate: 2025-12-01
---

on Linux

This tutorial explains how to configure SQL Server on Linux to support Active Directory

authentication, also known as integrated authentication. For an overview, see

Active Directory

authentication for SQL Server on Linux.

This tutorial consists of the following tasks:

Before you configure Active Directory Authentication, you need to:

Set up an Active Directory Domain Controller (Windows) on your network

Install SQL Server

Quickstart: Install SQL Server and create a database on Red Hat Enterprise Linux

Quickstart: Install SQL Server and create a database on SUSE Linux Enterprise Server

Quickstart: Install SQL Server and create a database on Ubuntu

Join your SQL Server Linux host with an Active Directory domain controller. For information on

how to join an active directory domain, see

Join SQL Server on a Linux host to an Active Directory

Join SQL Server host to Active Directory domain

＂

Create Active Directory user for SQL Server and set SPN

＂

Configure SQL Server service keytab

＂

Secure the keytab file

＂

Configure SQL Server to use the keytab file for Kerberos authentication

＂

Create Active Directory-based logins in Transact-SQL

＂

Connect to SQL Server using Active Directory Authentication

＂

７

Note

Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES) isn't supported.

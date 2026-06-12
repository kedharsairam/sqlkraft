---
title: "Understand AD Authentication"
topic: "linux-operations"
description: "on Linux This article provides you details on how Active Directory authentication works for SQL Server deployed on Linux or containers."
tags: ["linux-operations","understand-ad-authentication"]
pubDate: "2025-12-01"
---

on Linux

This article provides you details on how Active Directory authentication works for SQL Server

deployed on Linux or containers.

LDAP is an application protocol for working with various directory services, including Active

Directory. Directory services store user and account information, and security information such as

passwords. That information is encrypted and then shared with other devices on the network.

To find out more about securing LDAP, see

How to enable LDAP signing in Windows Server.

Kerberos is an authentication protocol used to verify the identity of a user or host computer. You

can think of it as a way to verify the client and server.

When you work in a heterogeneous (mixed) environment where you have Windows and non-

Windows servers and clients, there are two kinds of files you need to work with Active Directory-

based directory services:

Keytab files (short for "key tables")

Kerberos configuration files (

or

)

Server processes on Linux or Unix systems can't be configured to run processes with a Windows

service account. When you want a Linux or Unix system to automatically log into Active Directory

on startup, you must use a

keytab

file.

A keytab is a cryptographic file containing a representation of a Kerberos-protected service and

its long-term

key

of its associated service principal name in the Key Distribution Center (KDC).

```cmd
krb5.conf krb5.ini
```

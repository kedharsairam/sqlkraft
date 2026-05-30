---
title: "Transport security"
topic: "high-availability"
description: |
  Applies to:

  SQL Server

  Transport security involves authentication and, optionally, encryption of messages exchanged

  between the databases. For database mirroring and Always On availability groups,
tags:
  - "high-availability"
  - "transport-security"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Transport security involves authentication and, optionally, encryption of messages exchanged

between the databases. For database mirroring and Always On availability groups, authentication

and encryption are configured on the database mirroring endpoint. For an introduction to

database mirroring endpoints, see

The database mirroring endpoint (SQL Server)

.

Authentication is the process of verifying that a user is who the user claims to be. Connections

between database mirroring endpoints require authentication. Connection requests from a

partner or witness, if any, must be authenticated.

The type of authentication used by a server instance for database mirroring or Always On

availability groups is a property of the database mirroring endpoint. Two types of transport

security are available for database mirroring endpoints: Windows Authentication (the Security

Support Provider Interface (SSPI)) and certificate-based authentication.

Under Windows Authentication, each server instance logs in to the other side using the Windows

credentials of the Windows user account under which the process is running. Windows

Authentication might require some manual configuration of login accounts, as follows:

If the instances of SQL Server run as services under the same domain account, no extra

configuration is required.

If the instances of SQL Server run as services under different domain accounts (in the same

or trusted domains), the login of each account must be created in

on each of the

other server instances, and that login must be granted

permissions on the

endpoint.

If the instances of SQL Server run as the Network Service account, the login of each host

computer account (

) must be created in

on each of

the other servers, and that login must be granted

permissions on the endpoint.

```cmd
master
CONNECT
<domain-name>\<computer-name>$
master
CONNECT
```

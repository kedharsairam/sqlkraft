---
title: "Allow access to an endpoint"
topic: "high-availability"
description: ""
tags: ["high-availability","allow-access-to-an-endpoint"]
pubDate: "2025-12-01"
---

Using Windows Authentication for connecting the database mirroring endpoints of two

instances of SQL Server requires manual configuration of login accounts under the following

conditions:

If the instances of SQL Server run as services under different domain accounts (in the

same or trusted domains), the login of each account must be created in

on each

of the remote server instances and that login must be granted CONNECT permissions on

the endpoint.

If the instances of SQL Server run as the Network Service account, the login of the each

host computer account (

DomainName

\*\*\*\*

ComputerName$

) must be created in

on each of the remote server instances and that login must be granted CONNECT

permissions on the endpoint. This is because a server instance running under the Network

Service account authenticates using the domain account of the host computer.

1. For the user account of each instance of SQL Server, create a login on the other instances

of SQL Server. Use a

CREATE LOGIN

statement with the

clause.

For more information, see

Create a Login.

2. Also, to ensure that the login user has access to the endpoint, use the

GRANT

statement

to grant connect permissions on the endpoint to the login. Note that granting connect

permissions to the endpoint is unnecessary if the user is an Administrator.

For more information, see

Grant a Permission to a Principal.

７

Note

Ensure that an endpoint exists for each of the server instances. For more information, see.

```cmd
FROM WINDOWS
```

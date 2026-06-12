---
title: "Get started with security features"
topic: "linux-operations"
description: |
  SQL Server on Linux

  Article

  •

  11/21/2024

  Applies to:

  SQL Server

  - Linux

  If you're a Linux user who is new to SQL Server, the following tasks walk you through some of

  the security tasks. These
tags:
  - "linux-operations"
  - "get-started-with-security-features"
pubDate: 2025-12-01
---

on Linux

Article

•

11/21/2024

SQL Server

- Linux

If you're a Linux user who is new to SQL Server, the following tasks walk you through some of

the security tasks. These aren't unique or specific to Linux, but it helps to give you an idea of

areas to investigate further. In each example, a link is provided to the in-depth documentation

for that area.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

Grant others access to SQL Server by creating a login in the

database using the

CREATE

LOGIN

statement. For example:

Logins can connect to SQL Server and have access (with limited permissions) to the

database. To connect to a user-database, a login needs a corresponding identity at the

database level, called a database user. Users are specific to each database and must be

separately created in each database to grant them access. The following example moves you

into the

database, and then uses the

CREATE USER

statement to create a

user named Larry that is associated with the login named. Though the login and the user

Ｕ

Caution

Your password should follow the SQL Server default. By default, the

password must be at least eight characters long and contain characters from three of the

following four sets: uppercase letters, lowercase letters, base-10 digits, and symbols.

Passwords can be up to 128 characters long. Use passwords that are as long and complex

as possible.

```cmd
AdventureWorks2022
AdventureWorksDW2022 master master
AdventureWorks2022
```

---
title: "Database Engine error severities"
topic: "monitor"
description: |
  08/26/2025

  Applies to:

  SQL Server

  When an error is raised by the SQL Server Database Engine, the severity of the error indicates

  the type of problem encountered by SQL Server.

  The following table
tags:
  - "monitor"
  - "database-engine-error-severities"
pubDate: 2025-12-01
---

08/26/2025

Applies to:

SQL Server

When an error is raised by the SQL Server Database Engine, the severity of the error indicates

the type of problem encountered by SQL Server.

The following table lists and describes the severity levels of the errors raised by the SQL Server

Database Engine.

Description

0-9

Indicate informational messages that return status information or report errors that aren't

severe. The Database Engine doesn't raise system errors with severities of 0 through 9.

10

Indicates informational messages that return status information or report errors that aren't

severe. For compatibility reasons, the Database Engine converts severity 10 to severity 0

before returning the error information to the calling application.

11-16

Indicate errors that can be corrected by the user.

11

Indicates that the given object or entity doesn't exist.

12

A special severity for queries that don't use locking because of special query hints. In some

cases, read operations performed by these statements could result in inconsistent data

because locks aren't taken to guarantee consistency.

13

Indicates transaction deadlock errors.

14

Indicates security-related errors, such as permission denied.

15

Indicates syntax errors in the Transact-SQL command.

16

Indicates general errors that can be corrected by the user.

17-19

Indicate software errors that can't be corrected by the user. Inform your system administrator

of the problem.

17

Indicates that the statement caused SQL Server to run out of resources (such as memory,

locks, or disk space for the database) or to exceed some limit set by the system administrator.

ﾉ

Expand table

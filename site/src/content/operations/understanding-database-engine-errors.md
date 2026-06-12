---
title: "Understanding Database Engine errors"
topic: "monitor"
description: "SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft F"
tags: ["monitor","understanding-database-engine-errors"]
pubDate: 2025-12-01
---

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

Errors raised by the Microsoft SQL Server Database Engine have the attributes described in the

following table.

Description

Error

number

Each error message has a unique error number.

Error

message

string

The error message contains diagnostic information about the cause of the error. Many

error messages have substitution variables in which information, such as the name of the

object generating the error, is inserted.

Severity

The severity indicates how serious the error is. Errors that have a low severity, such as 1 or

2, are information messages or low-level warnings. Errors that have a high severity indicate

problems that should be addressed as soon as possible. For more information about

severities, see

Database Engine Error Severities.

State

Some error messages can be raised at multiple points in the code for the Database Engine.

For example, an 1105 error can be raised for several different conditions. Each specific

condition that raises an error assigns a unique state code.

When you are viewing databases that contain information about known issues, such as the

Microsoft Knowledge Base, you can use the state number to determine whether the

recorded issue is the same as the error you have encountered. For example, if a Knowledge

Base Article describes an 1105 error that has a state of 2 and the 1105 error message you

received had a state of 3, the error probably has a different cause than the one reported in

the article.

A Microsoft support engineer can also use the state code from an error to find the location

in the source code where that error code is being raised. This information might provide

additional ideas on how to diagnose the problem.

Procedure

name

Is the name of the stored procedure or trigger in which the error has occurred.

Line

number

Indicates which statement in a batch, stored procedure, trigger, or function generated the

error.

All system and user-defined error messages in an instance of the Database Engine are

contained in the

catalog view. You can use the RAISERROR statement to return

ﾉ

Expand table

---
title: "Performance"
topic: "clr-integration"
description: "This article discusses some of the design choices that enhance the performance of SQL Server integration with the .NET Fra"
tags: ["clr-integration","performance"]
pubDate: 2025-12-01
---

This article discusses some of the design choices that enhance the performance of SQL Server

integration with the.NET Framework common language runtime (CLR).

During compilation of SQL expressions, when a reference to a managed routine is

encountered, a common intermediate language (CIL) stub is generated. This stub includes code

to marshal the routine parameters from SQL Server to the CLR, invoke the function, and return

the result. This

glue

code is based on the type of parameter and on parameter direction (

in

,

out

,

or

reference

).

The glue code enables type-specific optimizations and ensures efficient enforcement of SQL

Server semantics, such as nullability, constraining facets, by-value, and standard exception

handling. By generating code for the exact types of the arguments, you avoid type coercion or

wrapper object creation costs (called "boxing") across the invocation boundary.

The generated stub is then compiled to native code and optimized for the particular hardware

architecture on which SQL Server executes, using the just-in-time (JIT) compilation services of

the CLR. The JIT services are invoked at the method level and allow the SQL Server hosting

environment to create a single compilation unit that spans both SQL Server and CLR execution.

Once the stub is compiled, the resulting function pointer becomes the run-time

implementation of the function. This code generation approach ensures that there are no extra

invocation costs related to reflection or metadata access at run time.

The compilation process yields a function pointer that can be called at run time from native

code. For scalar-valued user-defined functions, this function invocation happens on a per-row

basis. To minimize the cost of transitioning between SQL Server and the CLR, statements that

contain any managed invocation have a startup step to identify the target application domain.

This identification step reduces the cost of transitioning for each row.

---
title: "Architecture - CLR Hosted Environment"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  SQL Server integration with the .NET Framework common language runtime (CLR) enables

  database programmers to use languages
tags:
  - "clr-integration"
  - "architecture-clr-hosted-environment"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server integration with the .NET Framework common language runtime (CLR) enables

database programmers to use languages such as C#, Visual Basic .NET, and Visual C++.

Functions, stored procedures, triggers, data types, and aggregates are among the kinds of

business logic that programmers can write with these languages.

The CLR features garbage-collected memory, preemptive threading, metadata services (type

reflection), code verifiability, and code access security. The CLR uses metadata to locate and

load classes, lay out instances in memory, resolve method invocations, generate native code,

enforce security, and set run-time context boundaries.

The CLR and SQL Server differ as run-time environments in the way they handle memory,

threads, and synchronization. This article describes the way in which these two run times are

integrated so that all system resources are managed uniformly. This article also covers the way

in which CLR code access security (CAS) and SQL Server security are integrated to provide a

reliable and secure execution environment for user code.

In the .NET Framework, a programmer writes in a high-level language that implements a class

defining its structure (for example, the fields or properties of the class) and methods. Some of

these methods can be static functions. The compilation of the program produces a file called

an assembly that contains the compiled code in the common intermediate language (CIL), and

a manifest that contains all references to dependent assemblies.

The assembly manifest contains metadata about the assembly, describing all of the structures,

fields, properties, classes, inheritance relationships, functions, and methods defined in the

program. The manifest establishes the assembly identity, specifies the files that make up the

７

Note

Assemblies are a vital element in the architecture of the CLR. They are the units of

packaging, deployment, and versioning of application code in .NET Framework. Using

assemblies, you can deploy application code inside the database and provide a uniform

way to administer, back up, and restore complete database applications.

---
title: "Unpack a dacpac file"
topic: "ssms"
description: |
  A data-tier application (DAC) is a self-contained unit of the entire database model and is
  
  portable in an artifact known as a DAC package, or
  
  . It's a good practice to review the
  
  contents of a
  
  bef
tags:
  - "ssms"
  - "unpack-a-dacpac-file"
pubDate: 2025-12-01
---

A data-tier application (DAC) is a self-contained unit of the entire database model and is

portable in an artifact known as a DAC package, or

. It's a good practice to review the

contents of a

before deploying it in production, and to validate the upgrade actions

before upgrading an existing DAC. Validation of the

contents is especially important

when deploying packages that weren't developed in your organization. This article describes

several ways to unpack the database model from a

for Windows, macOS, and Linux.

Options for examining the content of a

include:

importing the

to a SQL project in Visual Studio

using the SqlPackage command-line utility to extract the

decompressing the file to view the XML contents

deploying the

to a test instance

Unpacking a

immediately after it was extracted from a database to view the object

definitions is more efficiently accomplished by using

Extract

in SqlPackage with the property

. The result directly creates a single

file that contains the object

definitions from the specified source database.

Importing a

to a SQL project in Visual Studio results in the contents of the

being transformed into

.sql

files and organized into folders. Following the import, post-

deployment scripts and predeployment scripts from the

are visible in the solution

explorer.

1. Install

SQL Server Data Tools

as a part of Visual Studio and create a new SQL project.

２

Warning

Don't deploy a

from unknown or untrusted sources. Such DACs could contain

malicious code that might execute unintended code or cause errors by modifying the

schema. Before you use a DAC from an unknown or untrusted source, deploy it on an

isolated test instance of the Database Engine, unpack the DAC and examine the code,

such as stored procedures or other user-defined code.

```cmd
.dacpac
.dacpac
.dacpac
.dacpac
.dacpac
```
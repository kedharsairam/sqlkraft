---
title: "Verify a dacpac file"
topic: "ssms"
description: ""
tags: ["ssms","verify-a-dacpac-file"]
pubDate: 2025-12-01
---

The process of converting an

existing SQL project to an SDK-style project

is done by manually

editing the

file to include the Microsoft.Build.Sql SDK-style project format. Backing

up the project file and archiving a

of the project before beginning the conversion is

recommended. By comparing a "before" and "after"

built from the project, you can

ensure that the conversion process was correctly completed.

The

DacpacVerify CLI (preview)

is a command line tool that compares two

files and

outputs the differences between the files. The tool is useful for verifying that a project

conversion was successful by comparing the

files before and after the conversion.

Similar to the SqlPackage command line tool, the DacpacVerify CLI (preview) is available as a

dotnet tool. DacpacVerify can be installed on Windows, macOS, and Linux and requires the.NET SDK

to be installed on your machine. To install the DacpacVerify CLI, run the following

command:

Bash

The basic usage of the DacpacVerify tool involves running the

command

followed by the paths to the two

files that you want to compare.

Bash

The tool outputs a summary of the differences between the two files. The verification of the

files includes:

pre-deployment scripts

post-deployment scripts

```cmd.sqlproj.dacpac.dacpac.dacpac.dacpac
```

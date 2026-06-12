---
title: "Install sqlpackage"
topic: "sqlpackage"
description: |
  ﾃ
          
            Summarize this article for me
          
            SqlPackage runs on Windows, macOS, and Linux, and is available to install through
          
            or as a standalone zip download. For details about the latest release, see the
          
            rel
tags: ["sqlpackage","install-sqlpackage"]
pubDate: 2025-12-01
---

ﾃ

SqlPackage runs on Windows, macOS, and Linux, and is available to install through

or as a standalone zip download. For details about the latest release, see the

release

notes.

170.3.93

170.3.93.6

February 10, 2026

SqlPackage is developed and released for both.NET and.NET Framework. Installing the.NET

10 SqlPackage version is recommended via the

convenient dotnet tool method

, which is cross-

platform and easy to update, or via the

portable self-contained.zip download. The.NET 10

SqlPackage releases benefit from the continual advances to the performance and scalability of.NET as part of the

focus on for modern applications

, which contrasts to the maintenance

support of.NET Framework for Windows. The.NET Framework version is only available as a.msi Windows installer.

Installing SqlPackage as a

dotnet tool

requires the.NET SDK

to be installed on your machine.

Installing SqlPackage as a global tool makes it available on your path as

and is the

recommended method to install SqlPackage for Windows, macOS, and Linux. SqlPackage is

available as a dotnet tool for.NET 8 and later versions.

To install SqlPackage as a global.NET tool, run the following command:

More information on the options available with the

command can be

found in the

dotnet tool install documentation.

７

Note

Previously, SqlPackage had a distinct version number (19) and build number (160.x).

Beginning with version 161, the version number of SqlPackage matches the DacFx version

number it's associated with (for example, 162.0.52).

```cmd
dotnet tool sqlpackage dotnet tool install dotnet tool install -g microsoft.sqlpackage
```

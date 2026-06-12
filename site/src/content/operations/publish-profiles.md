---
title: "Publish profiles"
topic: "ssms"
description: "A publish profile is a file that stores deployment configuration for a SQL project. Publish"
tags: ["ssms","publish-profiles"]
pubDate: "2025-12-01"
---

A publish profile is a file that stores deployment configuration for a SQL project. Publish

profiles can encapsulate target connection information, deployment options, and SQLCMD

variable values in a reusable

file. Publish profiles are especially useful when your

deployment requires specific settings, like excluding certain object types or ignoring target

platform differences. Instead of specifying these options each time you deploy, save them in a

publish profile and reuse it.

When working with SQL projects, you can create and store multiple publish profiles. During

deployment, select a publish profile to apply consistent settings without manually selecting

multiple options.

A publish profile is an XML file with the

extension. The file contains properties

and items that define deployment behavior in the XML path.

A publish profile can include the following information:

- the connection string for the target database server

- the name of the database to deploy to

- settings that control deployment behavior, such as whether to

drop objects not in the source or block on possible data loss

SQLCMD variable values

- values for SQLCMD variables defined in the SQL project,

applied at deployment time

The following example shows a publish profile that targets a local SQL Server instance. It sets

two deployment options and provides a value for one SQLCMD variable:

```cmd.publish.xml.publish.xml
/Project/PropertyGroup
<?xml version="1.0" encoding="utf-8"?>
<Project >
```

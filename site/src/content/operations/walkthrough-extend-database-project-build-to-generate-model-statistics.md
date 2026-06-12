---
title: "Walkthrough: Extend Database Project Build to Generate Model Statistics"
topic: "ssb-diagnose"
description: |
  09/10/2025
          
            You can create a build contributor to perform custom actions when you build a database
          
            project. In this walkthrough, you create a build contributor named ModelStatistics that outputs
          
            sta
tags: ["ssb-diagnose","walkthrough-extend-database-project-build-to-generate-model-statistics"]
pubDate: 2025-12-01
---

You can create a build contributor to perform custom actions when you build a database

project. In this walkthrough, you create a build contributor named ModelStatistics that outputs

statistics from the SQL database model when you build a database project. Because this build

contributor takes parameters when you build, some extra steps are required.

In this walkthrough, you accomplish the following major tasks:

Create a build contributor

Install the build contributor

Test your build contributor

You need the following components to complete this walkthrough:

You must have installed a version of Visual Studio that includes SQL Server Data Tools

(SSDT) and supports C# or Visual Basic (VB) development.

You must have a SQL project that contains SQL objects.

Build contributors are run during project build, after the model representing the project has

been generated but before the project is saved to disk. They can be used for several scenarios,

such as:

Validating the model contents and reporting validation errors to the caller. This can be

done by adding errors to a list passed as a parameter to the OnExecute method.

Generating model statistics and reporting to the user. This is the example shown here.

７

Note

This walkthrough is intended for users who are already familiar with the SQL features of

SSDT. You're also expected to be familiar with basic Visual Studio concepts, such as how to

create a class library and how to use the code editor to add code to a class.

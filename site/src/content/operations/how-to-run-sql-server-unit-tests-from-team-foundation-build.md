---
title: "How to: Run SQL Server Unit Tests from Team Foundation Build"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
    You can use Team Foundation Build to run your SQL Server unit tests as part of a build
  
    verification test (BVT). You can configure your unit tests to deploy the database, generate test
  
    da
tags: ["ssb-diagnose","how-to-run-sql-server-unit-tests-from-team-foundation-build"]
pubDate: "2025-12-01"
---

You can use Team Foundation Build to run your SQL Server unit tests as part of a build

verification test (BVT). You can configure your unit tests to deploy the database, generate test

data, and then run selected tests. If you aren't familiar with Team Foundation Build, you should

review the following information before you follow the procedures in this article:

Create and define SQL Server unit tests

How to: Configure and Run Scheduled Tests After Building Your Application

Create a Basic Build Definition

Before you use these procedures, you must first configure your working environment by

performing the following tasks:

Install Team Foundation Build and Team Foundation version control. You probably have to

install Team Foundation Build and Team Foundation version control on different

computers.

Install Microsoft SQL Server Data Tools Build Utilities on the same computer as Team

Foundation Build. To install the SQL Server Data Tools Build Utilities, first perform an

administrative installation point. For more information about an administrative installation

point, see

Install SQL Server Data Tools (SSDT) for Visual Studio. Then install

SSDTBuildUtilities.msi onto the build server from the location (/location) used for the

administrative installation point.

Connect to an instance of Azure DevOps Server.

After you configure your working environment, you must then follow these steps:

1. Create a database project.

2. Import or create the schema and objects for the database project.

3. Configure the database project properties for build and deployment.

4. Create one or more unit tests.

5. Add the solution that contains the database project and the unit test project to version

control, and check in all files.

The procedures in this article describe how to create a build definition to run your unit tests as

part of an automated test run:

1.

Configure Test Settings to Run Database Unit Tests on an x64 Build Agent

2.

Assign Tests to a Test Category (Optional)

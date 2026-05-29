---
title: "Walkthrough: Extend Database Project Deployment to Modify the Deployment Plan"
topic: "ssb-diagnose"
description: |
  09/09/2025

  You can create deployment contributors to perform custom actions when you deploy a SQL

  project. You can create either a

  DeploymentPlanModifier

  or a

  DeploymentPlanExecutor

  . Use a

  Dep
tags:
  - "ssb-diagnose"
  - "walkthrough-extend-database-project-deployment-to-modify-the-deployment-plan"
pubDate: 2025-12-01
---

09/09/2025

You can create deployment contributors to perform custom actions when you deploy a SQL

project. You can create either a

DeploymentPlanModifier

or a

DeploymentPlanExecutor

. Use a

DeploymentPlanModifier

to change the plan before it's executed and a

DeploymentPlanExecutor

to perform operations while the plan is being executed. In this

walkthrough, you create a

DeploymentPlanModifier

named SqlRestartableScriptContributor.

The DeploymentPlanModifier SqlRestartableScriptContributor adds

statements to the

batches in the deployment script to enable the script to be rerun until they're completed if an

error occurs during execution.

In this walkthrough, you accomplish the following major tasks:

Create the DeploymentPlanModifier type of deployment contributor

Install the deployment contributor

Run or Test your deployment contributor

You need the following components to complete this walkthrough:

You must have installed a version of Visual Studio that includes SQL Server Data Tools and

supports C# development.

You must have a SQL project that contains SQL objects.

An instance of SQL Server to which you can deploy a database project.

７

Note

This walkthrough is intended for users who are already familiar with the SQL features of

SQL Server Data Tools. You're also expected to be familiar with basic Visual Studio

concepts, such as how to create a class library and how to use the code editor to add code

to a class.

```cmd
IF
```

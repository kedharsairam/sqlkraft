---
title: "Walkthrough: Extend Database Project Deployment to Analyze the Deployment Plan"
topic: "ssb-diagnose"
description: |
  09/10/2025
  
  You can create deployment contributors to perform custom actions when you deploy a SQL
  
  project. You can create either a DeploymentPlanModifier or a DeploymentPlanExecutor. Use a
  
  Deployme
tags:
  - "ssb-diagnose"
  - "walkthrough-extend-database-project-deployment-to-analyze-the-deployment-plan"
pubDate: 2025-12-01
---

09/10/2025

You can create deployment contributors to perform custom actions when you deploy a SQL

project. You can create either a DeploymentPlanModifier or a DeploymentPlanExecutor. Use a

DeploymentPlanModifier to change the plan before it's executed and a

DeploymentPlanExecutor to perform operations while the plan is being executed. In this

walkthrough, you create a DeploymentPlanExecutor named

DeploymentUpdateReportContributor that creates a report about the actions that are

performed when you deploy a database project. Because this build contributor accepts a

parameter to control whether the report is generated, you must perform another required step.

In this walkthrough, you accomplish the following major tasks:

Create the DeploymentPlanExecutor type of deployment contributor

Install the deployment contributor

Test your deployment contributor

You need the following components to complete this walkthrough:

You must have installed a version of Visual Studio that includes SQL Server Data Tools

(SSDT) and supports C# or VB development.

You must have a SQL project that contains SQL objects.

An instance of SQL Server to which you can deploy a database project.

To create a deployment contributor, you must perform the following tasks:

７

Note

This walkthrough is intended for users who are already familiar with the SQL features of

SSDT. You're also expected to be familiar with basic Visual Studio concepts, such as how to

create a class library and how to use the code editor to add code to a class.
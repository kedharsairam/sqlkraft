---
title: "Creating and deploying a SQL project"
topic: "ssms"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The development cycle of a SQL database project enables database development to be
  
  integrate
tags:
  - "ssms"
  - "creating-and-deploying-a-sql-project"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The development cycle of a SQL database project enables database development to be

integrated into a continuous integration and continuous deployment (CI/CD) workflows

familiar as a development best practice. While deployment of a SQL database project can be

done manually, it's recommended to use a deployment pipeline to automate the deployment

process such that ongoing deployments are run based on your continued local development

without additional effort.

This article steps through creating a new SQL project, adding objects to the project, and setting

up a continuous deployment pipeline for building and deploying the project with GitHub

actions. The tutorial is a superset of the contents of the

Get started with SQL database projects

article. While the tutorial implements the deployment pipeline in GitHub actions, the same

concepts apply to Azure DevOps, GitLab, and other automation environments.

In this tutorial, you:

1. Create a new SQL project

2. Add objects to the project

3. Build the project locally

4. Check the project into source control

5. Add a project build step to a continuous deployment pipeline

6. Add a

deployment step to a continuous deployment pipeline

If you've already completed the steps to

get started with SQL database projects

, you can skip

to

step 4

. At this end of this tutorial, your SQL project will be automatically building and

deploying changes to a target database.

.NET 8 SDK

Visual Studio 2022 Community, Professional, or Enterprise

Install SQL Server Data Tools (SSDT) for Visual Studio

Make sure you have the following items to complete the pipeline setup in GitHub:

A GitHub account where you can create a repository.

Create one for free

.

GitHub actions is

enabled

on your repository.

```cmd
.dacpac
```
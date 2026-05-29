---
title: "SQL projects automation"
topic: "ssms"
description: |
  SQL projects automation
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  This article provides an overview of automation options for SQL projects across different
  
  software de
tags:
  - "ssms"
  - "sql-projects-automation"
pubDate: 2025-12-01
---

SQL projects automation

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

This article provides an overview of automation options for SQL projects across different

software delivery platforms. Use automation to integrate SQL database projects into CI/CD

pipelines, and deploy database changes consistently and repeatedly.

SQL projects automation typically involves two key tasks in a CI/CD pipeline:

: Validate the project and produce the deployment artifact (

)

by running

on the SQL database project to compile. Optionally, execute

code analysis

rules to check code quality during project build.

: Publish the

to a target database using SqlPackage or a

platform-specific task. Deployment can target Azure SQL Database, Azure SQL Managed

Instance, SQL Server, or SQL database in Fabric.

When you integrate these steps into your CI/CD pipeline, database changes are validated on

every commit and deployed consistently across environments.

: A typical pipeline separates the build and deploy stages. The build stage

compiles the SQL project and produces a

file, which is then published as a pipeline

artifact. In a subsequent deploy job (potentially after manual approval), the artifact is

downloaded and deployed to the target database. This separation allows you to build once

and deploy the same artifact to multiple environments, ensuring consistency.

: Before deploying to sensitive environments, you can review the deployment

plan. SqlPackage supports a

action that generates the T-SQL script that would be

executed during deployment, without applying changes. The provided T-SQL script allows



```cmd
.dacpac
dotnet build
.dacpac
.dacpac
Script
```
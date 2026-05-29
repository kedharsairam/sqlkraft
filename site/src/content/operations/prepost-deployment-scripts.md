---
title: "Pre/post deployment scripts"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  Pre-deployment and post-deployment scripts are SQL scripts that are included in the project t
tags:
  - "ssms"
  - "prepost-deployment-scripts"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Pre-deployment and post-deployment scripts are SQL scripts that are included in the project to

be executed during deployment. Pre/post-deployment scripts are included in the

but

they aren't compiled into or validated with database object model. A pre-deployment script is

executed before the deployment plan is executed but the deployment plan is calculated before

the script executes. A post-deployment script is executed after the deployment plan completes.

A SQL project file can have a single pre-deployment script and a single post-deployment script

specified.

The following example from a SQL project file adds the file

as a pre-deployment

script.

The following example from a SQL project file adds the file

as post-

deployment script.

Multiple files can be executed as part of a pre-deployment or post-deployment script by using

a SQLCMD script that calls each file in order.

SQL

SQL project file sample and syntax

```cmd
.dacpac
prep-db.sql
populate-app-settings.sql
...
<ItemGroup>
<PreDeploy
Include
=
"prep-db.sql"
/>
</ItemGroup>
...
<ItemGroup>
<PostDeploy
Include
=
"populate-app-settings.sql"
/>
</ItemGroup>
</Project>
```

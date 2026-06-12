---
title: "SQL projects extensibility"
topic: "ssms"
description: "The .NET Data-tier Application Framework (DacFx) library provides extensibility points that you can use to modify the behavior of the build and deployment actions for database"
tags: ["ssms","sql-projects-extensibility"]
pubDate: 2025-12-01
---

The.NET Data-tier Application Framework (DacFx) library provides extensibility points that you

can use to modify the behavior of the build and deployment actions for database projects.

This type of extension is executed when the SQL project is built

after the project model is completely validated. The build contributor can access the

completed model, in addition to all properties of the Build task and any custom

arguments.

This type of extension is executed when the SQL

project is deployed, as part of the deployment pipeline, after the deployment plan is

generated, but before the deployment plan is executed. You can use a

DeploymentPlanModifier to modify the deployment plan by adding or removing steps.

Deployment contributors can access the deployment plan, the comparison results, and

the source and target models.

This type of extension is executed when the

deployment plan is executed and provides read-only access to the deployment plan. The

DeploymentPlanExecutor performs actions based on the deployment plan.

You can implement build or deployment contributors to enable the following example

scenarios:

- To support this scenario, you

implement a

BuildContributor

and override the OnExecute method to generate the

schema documentation. You can create a targets file that defines default arguments that

control whether the extension runs and to specify the name of the output file.

- To support this scenario,

you implement a

DeploymentPlanExecutor

that generates the XML file when the SQL

project is deployed.

- To support this

scenario, you implement a

DeploymentPlanModifier

and iterate over the deployment

plan. For each SqlTableMigrationStep in that plan, you examine the comparison result to

determine whether that step should be performed or skipped.

- To support this

scenario, you implement a deployment contributor and override the

OnEstablishDeploymentConfiguration method to specify which files that are marked as

DeploymentExtensionConfiguration by the project system. These files should be copied to

the output folder and added inside the generated dacpac. You can also modify the

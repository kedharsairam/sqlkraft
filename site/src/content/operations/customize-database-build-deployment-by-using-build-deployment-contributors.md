---
title: "Customize Database Build & Deployment by Using Build & Deployment Contributors"
topic: "ssb-diagnose"
description: |
  09/09/2025

  Visual Studio provides extensibility points that you can use to modify the behavior of the build

  and deployment actions for database projects.

  You can create an extension for the extensi
tags:
  - "ssb-diagnose"
  - "customize-database-build-deployment-by-using-build-deployment-contributors"
pubDate: 2025-12-01
---

09/09/2025

Visual Studio provides extensibility points that you can use to modify the behavior of the build

and deployment actions for database projects.

You can create an extension for the extensibility points, as shown in the following table:

Notes

Build

BuildContributor

This type of extension is executed when the SQL project is built after

the project model has been completely validated. The build

contributor can access the completed model, in addition to all

properties of the Build task and any custom arguments.

Deploy

DeploymentPlanModifier

This type of extension is executed when the SQL project is deployed,

as part of the deployment pipeline, after the deployment plan has

been generated, but before the deployment plan is executed. You

can use a DeploymentPlanModifier to modify the deployment plan

by adding or removing steps. Deployment contributors can access

the deployment plan, the comparison results, and the source and

target models.

Deploy

DeploymentPlanExecutor

This type of extension is executed when the deployment plan is

executed and provides read-only access to the deployment plan.

The DeploymentPlanExecutor performs actions based on the

deployment plan.

You can implement build or deployment contributors to enable the following example

scenarios:

- To support this scenario, you

implement a

BuildContributor

and override the OnExecute method to generate the

ﾉ

Expand table

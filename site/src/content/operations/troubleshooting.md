---
title: "Troubleshooting"
topic: "high-availability"
description: |
  10/21/2025

  Applies to:

  SQL Server

  This article provides information about the following issues:

  Basic troubleshooting steps

  Recover from a failover cluster failure

  Resolve the most common failov
tags:
  - "high-availability"
  - "troubleshooting"
pubDate: 2025-12-01
---

10/21/2025

SQL Server

This article provides information about the following issues:

Basic troubleshooting steps

Recover from a failover cluster failure

Resolve the most common failover clustering problems

Use extended stored procedures and COM objects

The first diagnostic step is to run a fresh cluster validation check. For details on validation, see

Create a Failover Cluster: Validate the Configuration. This can be completed without any

interruption of service as it doesn't affect any online cluster resources.

Validation can be run at any time once the Failover Clustering feature has been installed,

including before the cluster has been deployed, during cluster creation and while the cluster is

running. In fact, additional tests are executed once the cluster is in use, which check that best

practices are being followed for highly available workloads. Across these dozens of tests, only a

few of them affect running cluster workloads and these are all within the storage category, so

skipping this entire category is an easy way to avoid disruptive tests.

Failover clustering comes with a built-in safeguard to prevent accidental downtime when

running the storage tests during validation. If the cluster has any online groups when validation

is initiated, and the storage tests remain selected, it prompts the user for confirmation whether

they want to run all the tests (and cause downtime), or to skip testing the disks of any online

groups to avoid downtime. If the entire storage category was excluded from being tested, then

this prompt isn't displayed. This enables cluster validation with no downtime.

1. In the Failover Cluster snap-in, in the console tree, make sure

is selected and then, under

, select.

2. Follow the instructions in the wizard to specify the servers and the tests, and run the tests.

The

page appears after the tests run.

3. While still on the

page, select

to view the test results.

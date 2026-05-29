---
name: 'sys.partition_range_values'
title: 'sys.partition_range_values'
category: 'partitions'
description: 'Displays one row for each Policy-Based Management policy and target query expression'
tags: ["catalog-view", "partitions"]
pubDate: 2026-05-29
---

SQL)

Article

•

12/17/2024

Applies to:

SQL Server

Displays one row for each Policy-Based Management policy and target query expression

combination. Use the syspolicy_system_health_state view to programmatically check the policy

health of the server. The following table describes the columns in the

syspolicy_system_health_state view.


## Description
health_state_id

Identifier of the policy health state record.

policy_id

Identifier of the policy.

last_run_date

Date and time the policy was last run.

target_query_expression_with_id

The target expression, with values assigned to

identity variables, that defines the target against

which the policy is evaluated.

target_query_expression

The expression that defines the target against which

the policy is evaluated.

result

Health state of this target with regard to the policy:

0 = Failure

1 = Success

The syspolicy_system_health_state view displays the most recent health state of target query

expression for each active (enabled) policy. The SQL Server Management Studio Object

Explorer and Object Explorer Details page aggregates policy health from this view to show the

critical health state.

Requires membership in the PolicyAdministratorRole role in the msdb database.

ﾉ

Expand table

Administer Servers by Using Policy-Based Management

Policy-Based Management Views (Transact-SQL)

See Also

SQL)

Article

•

02/11/2025

Applies to:

Azure SQL Database

Azure SQL Managed Instance

This section contains resource governor information for the following catalog views.

sys.resource_governor_configuration (Transact-SQL)

sys.resource_governor_external_resource_pools (Transact-SQL)

sys.resource_governor_resource_pools (Transact-SQL)

sys.resource_governor_workload_groups (Transact-SQL)

Resource governor related dynamic management views (Transact-SQL)

Resource governor

Related content

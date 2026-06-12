---
title: "Assess"
topic: "azure-synapse"
description: "enabled by Azure Arc The best practices assessment feature provides a mechanism to evaluate the configuration of your SQL Server instanc"
tags: ["azure-synapse","assess"]
pubDate: "2025-12-01"
---

enabled by Azure Arc

The

best practices assessment

feature provides a mechanism to evaluate the configuration of

your SQL Server instance. After you enable the feature, an assessment scans your SQL Server

instance and databases to provide recommendations for things like:

and database configurations

Index management

Deprecated features

Enabled or missing trace flags

Statistics

The duration of an assessment run can be a few minutes to an hour, depending on your

environment (for example, number of databases and objects). The size of an assessment result

also depends on your environment.

An assessment runs against your instance and all databases on that instance. In our testing, we

observed that an assessment run can have up to 10% CPU impact on the machine. In these

tests, we ran the assessment while an application similar to the TPC-C benchmark ran against

the SQL Server instance.

This article provides instructions for using best practices assessment on an instance of SQL

Server enabled by Azure Arc.

Make sure that your Windows-based SQL Server instance is connected to Azure. Follow

the instructions at

Automatically connect your SQL Server to Azure Arc.

）

Important

Best practices assessment is available only for SQL Server instances purchased through

either

or

licensing options.

For instructions to configure the appropriate license type, review.

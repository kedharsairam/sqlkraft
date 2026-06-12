---
title: "Use activity logs"
topic: "azure-synapse"
description: "06/24/2025 Activity logs for SQL Server enabled by Azure Arc provide insight into events related to SQL Server enabled by Azure Arc and View Azure Arc-enabled inventory"
tags: ["azure-synapse","use-activity-logs"]
pubDate: "2025-12-01"
---

Activity logs for SQL Server enabled by Azure Arc provide insight into events related to

Server enabled by Azure Arc

and

View Azure Arc-enabled inventory

resources. Activity logs

contain events that correspond to the creation and modification of resources. These events

include SQL Server instance updates (

), SQL Server database updates

(

), and writing of tags to resources.

This feature helps in auditing operations performed on a resource. The logs provide crucial

information such as the time when an operation started, the operation's status, and the party

responsible for event creation.

You can access an activity log from most menus in the Azure portal. Go to the Azure Arc-

enabled SQL Server resource, and then select.

The initial filter depends on the page where you access the activity log. You can change the

filter to view all other entries. To add more properties to the filter, select.



```cmd
SqlServerInstance_Update
SqlServerDatabases_Update
```

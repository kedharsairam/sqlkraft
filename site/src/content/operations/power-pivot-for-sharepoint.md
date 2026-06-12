---
title: "Power Pivot for SharePoint"
topic: "upgrade"
description: "06/03/2025 - Windows only This article summarizes the steps required to upgrade a deployment of Power Pivot for SharePoint to Microsoft SQL Server 2016 (13.x) Power Pivot f"
tags: ["upgrade","power-pivot-for-sharepoint"]
pubDate: 2025-12-01
---

- Windows only

This article summarizes the steps required to upgrade a deployment of Power Pivot for

SharePoint to Microsoft SQL Server 2016 (13.x) Power Pivot for SharePoint. The specific steps

depend on the version of SharePoint your environment is currently running and include the

Power Pivot for SharePoint Add-in (

).

SharePoint 2010 | SharePoint 2013

For release notes, see

2016 release notes.

If you're upgrading a multi-server SharePoint 2010 farm that has two or more Power Pivot

for SharePoint instances, you must fully upgrade each server

continuing to the

next server. A full upgrade includes running SQL Server Setup to upgrade Power Pivot for

SharePoint program files, followed by SharePoint upgrade actions that configure the

upgraded services. Server availability is limited until you run upgrade actions in the

appropriate Power Pivot Configuration Tool or Windows PowerShell.

All instances of Power Pivot System Service and Analysis Services in a SharePoint 2010

farm must be the same version. For information on how to verify the version, see the

section

Verify the Versions of Power Pivot Components and Services

in this article.

The Power Pivot configuration tools are one of the SQL Server shared features and all

shared features upgrade at the same time. If during an upgrade process you select other

instances or features that require a shared feature upgrade, then the Power

Pivot configuration tool is also upgraded. You might have issues if the Power Pivot

configuration tool is upgraded but your Power Pivot instance isn't. For more information

about SQL Server shared features, see

Upgrade SQL Server Using the Installation Wizard

(Setup).

The Power Pivot for SharePoint Add-in (

) installs side by side with

previous versions. For example, the add-in installs to the folder. See

File locations

for information

about SQL Server installation files.

```cmd
c:\Program
Files\Microsoft SQL Server\nnn\Tools\PowerPivotTools
```

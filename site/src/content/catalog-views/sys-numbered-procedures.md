---
name: "sys.numbered_procedures"
title: "sys.numbered_procedures"
category: "compatibility"
description: "Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Contains a row for each SQL Server stored procedure that was created as a numbered procedure. This does not show a row for the base (number = 1) stored procedure. Entries for the base stored procedures can be found in views such as ID of the object of the stored procedure. Number of this procedure within the object, 2 or gr"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  sys.numbered_procedures
  sys.numbered_procedure_parameters
---

## Description

Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Contains a row for each SQL Server stored procedure that was created as a numbered procedure. This does not show a row for the base (number = 1) stored procedure. Entries for the base stored procedures can be found in views such as ID of the object of the stored procedure. Number of this procedure within the object, 2 or greater.

## Syntax

```sql
sys.numbered_procedures
sys.numbered_procedure_parameters
```

## Permissions

Article • 05/23/2023 Applies to: SQL Server Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric Contains a row for each SQL Server stored procedure that was created as a numbered procedure. This does not show a row for the base (number = 1) stored procedure. Entries for the base stored procedures can be found in views such as and . Description ID of the object of the stored procedure. Number of this procedure within the object, 2 or greater. The SQL Server text that defines this procedure. NULL = encrypted. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . ） Important Numbered procedures are deprecated. Use of numbered procedures is discouraged. A DEPRECATION_ANNOUNCEMENT event is fired when a query that uses this catalog view is compiled. ﾉ Expand table ７ Note XML and CLR parameters are not supported for numbered procedures. See Also Category Deprecated feature Replacement Feature name sysdevices sysfilegroups sysfiles sysforeignkeys sysfulltextcatalogs sysindexes sysindexkeys syslockinfo syslogins sysmembers sysmessages sysobjects sysoledbusers sysopentapes sysperfinfo syspermissions sysprocesses sysprotects sysreferences sysremotelogins sysservers systypes sysusers sysdevices sysfilegroups sysfiles sysforeignkeys sysfulltextcatalogs sysindexes sysindexkeys syslockinfo syslogins sysmembers sysmessages sysobjects sysoledbusers sysopentapes sysperfinfo syspermissions sysprocesses sysprotects sysreferences sysremotelogins sysservers systypes sysusers System tables None numbered_procedures numbered_procedure_pa System functions fn_virtualservernodes fn_servershareddrives fn_virtualservernodes fn_servershareddrives System views Table compression The use of the vardecimal storage format. Vardecimal storage format is deprecated. Data compression in this version compresses decimal values and other data types. We recommend that you use data compression instead of the vardecimal storage format. Vardecimal storage form Table compression Use of the procedure. Vardecimal storage format is deprecated. The SQL Server data compression feature compresses decimal values as well as other data types. We recommend that you use data compression instead of the vardecimal storage format. Table compression Use of the procedure. Use data compression and the

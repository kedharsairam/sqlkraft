---
title: "Disallowed Types & Members in Microsoft.VisualBasic.dll"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  SQL Server common language integration (CLR) programming disallows the use of a type or

  member that has a

  that specifies a

  enumeration with a value
tags:
  - "clr-integration"
  - "disallowed-types-members-in-microsoftvisualbasicdll"
pubDate: 2025-12-01
---

Article

•

12/30/2024

SQL Server

common language integration (CLR) programming disallows the use of a type or

member that has a

that specifies a

enumeration with a value of

,

,

,

,

,

,

,

, or. The

following table lists the members and types of the

assembly whose

Host Protection Attribute (HPA) values are disallowed.

７

Note

This list was generated from the supported assemblies. For more information, see.

ﾉ

Expand table

```sql
HostProtectionAttribute
System.Security.Permissions.HostProtectionResource
ExternalProcessMgmt
ExternalThreading
MayLeakOnAbort
SecurityInfrastructure
SelfAffectingProcessMgmt
SelfAffectingThreading
SharedState
Synchronization
UI
Microsoft.VisualBasic.dll
Type or Member
HPA Value(s)
Microsoft.VisualBasic.ApplicationServices.ApplicationBase
ExternalProcessMgmt
Microsoft.VisualBasic.ApplicationServices.ApplicationBase.ChangeCulture()
ExternalProcessMgmt
Microsoft.VisualBasic.ApplicationServices.ApplicationBase.get_Info()
ExternalProcessMgmt
Microsoft.VisualBasic.ApplicationServices.AssemblyInfo
ExternalProcessMgmt
Microsoft.VisualBasic.ApplicationServices.BuiltInRoleConverter
SharedState
Microsoft.VisualBasic.ApplicationServices.ConsoleApplicationBase
ExternalProcessMgmt
Microsoft.VisualBasic.ApplicationServices.User
ExternalProcessMgmt
Microsoft.VisualBasic.ApplicationServices.WebUser
ExternalProcessMgmt
Microsoft.VisualBasic.ApplicationServices.WindowsFormsApplicationBase
ExternalProcessMgmt
Microsoft.VisualBasic.CompilerServices.HostServices
SharedState
Microsoft.VisualBasic.CompilerServices.ProjectData.EndApp()
SelfAffectingProcessMgmt
```

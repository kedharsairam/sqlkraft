---
title: "Disallowed Types & Members in System.Data.dll"
topic: "clr-integration"
description: ""
tags: ["clr-integration","disallowed-types-members-in-systemdatadll"]
pubDate: 2025-12-01
---

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

following table lists the members and types of the System.Data.dll assembly whose Host

Protection Attribute (HPA) values are disallowed.

,

Host protection attributes and CLR integration programming

Disallowed types and members in Microsoft.VisualBasic.dll

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
System.Data.SqlClient.SqlCommand.BeginExecuteNonQuery()
ExternalThreading
System.Data.SqlClient.SqlCommand.BeginExecuteReader()
ExternalThreading
System.Data.SqlClient.SqlCommand.BeginExecuteXmlReader()
ExternalThreading
System.Data.SqlClient.SqlDependency.ctor()
ExternalThreading
System.Data.SqlClient.SqlDependency.Start()
ExternalThreading
System.Data.SqlClient.SqlDependency.Stop()
ExternalThreading
System.Data.TypedDataSetGenerator
SharedState
Synchronization
System.Xml.XmlDataDocument
Synchronization
```

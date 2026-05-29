---
title: "Disallowed Types & Members in System.Core.dll"
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
  - "disallowed-types-members-in-systemcoredll"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

SQL Server common language integration (CLR) programming disallows the use of a type or

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

, or

. The

following table lists the members and types of the System.Core.dll assemblies whose Host

Protection Attribute (HPA) values are disallowed.

７

Note

This list was generated from the supported assemblies. For more information, see

.

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
System.Diagnostics.Eventing.EventDescriptor
MayLeakOnAbort
System.Diagnostics.Eventing.EventProvider
MayLeakOnAbort
System.Diagnostics.Eventing.EventProviderTraceListener
MayLeakOnAbort
System.Management.Instrumentation.ManagementEntityAttribute
MayLeakOnAbort
System.Management.Instrumentation.WmiConfigurationAttribute
MayLeakOnAbort
System.Management.Instrumentation.ManagementMemberAttribute
MayLeakOnAbort
System.Management.Instrumentation.ManagementNewInstanceAttribute
MayLeakOnAbort
System.Management.Instrumentation.ManagementBindAttribute
MayLeakOnAbort
System.Management.Instrumentation.ManagementCreateAttribute
MayLeakOnAbort
System.Management.Instrumentation.ManagementRemoveAttribute
MayLeakOnAbort
System.Management.Instrumentation.ManagementEnumeratorAttribute
MayLeakOnAbort
```
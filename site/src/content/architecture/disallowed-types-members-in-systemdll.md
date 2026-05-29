---
title: "Disallowed Types & Members in System.dll"
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
  - "disallowed-types-members-in-systemdll"
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

following table lists the members and types of the System.dll assembly whose Host Protection

Attribute (HPA) values are disallowed.

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
Microsoft.Win32.NativeMethods
MayLeakOnAbort
Microsoft.Win32.PowerModeChangedEventArgs
MayLeakOnAbort
Microsoft.Win32.PowerModeChangedEventHandler
MayLeakOnAbort
Microsoft.Win32.SafeHandles.SafeEventHandle
MayLeakOnAbort
Microsoft.Win32.SafeHandles.SafeEventLogReadHandle
MayLeakOnAbort
Microsoft.Win32.SafeHandles.SafeEventLogWriteHandle
MayLeakOnAbort
Microsoft.Win32.SafeHandles.SafeFileMappingHandle
MayLeakOnAbort
Microsoft.Win32.SafeHandles.SafeFileMapViewHandle
MayLeakOnAbort
Microsoft.Win32.SafeHandles.SafeLibraryHandle
MayLeakOnAbort
Microsoft.Win32.SafeHandles.SafeLocalMemHandle
MayLeakOnAbort
Microsoft.Win32.SafeHandles.SafeProcessHandle
MayLeakOnAbort
```

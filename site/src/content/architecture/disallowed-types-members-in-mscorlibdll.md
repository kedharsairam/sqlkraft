---
title: "Disallowed Types & Members in mscorlib.dll"
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
  - "disallowed-types-members-in-mscorlibdll"
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

following table lists the members and types of the mscorlib.dll assembly whose Host Protection

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
SyncStream.BeginRead()
ExternalThreading
SyncStream.BeginWrite()
ExternalThreading
System.Collections.ArrayList.Synchronized()
Synchronization
System.Collections.Hashtable.Synchronized()
Synchronization
System.Collections.Queue.Synchronized()
Synchronization
System.Collections.SortedList.Synchronized()
Synchronization
System.Collections.Stack.Synchronized()
Synchronization
System.Console.Beep()
UI
System.Console.get_Error()
UI
System.Console.get_In()
UI
System.Console.get_KeyAvailable()
UI
```
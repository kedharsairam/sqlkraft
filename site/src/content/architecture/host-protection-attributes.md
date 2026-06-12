---
title: "Host Protection Attributes"
topic: "clr-integration"
description: "The common language runtime (CLR) provides a mechanism to annotate managed application programming interfaces (APIs) that are part of the .NET Framewo"
tags: ["clr-integration","host-protection-attributes"]
pubDate: "2025-12-01"
---

The common language runtime (CLR) provides a mechanism to annotate managed application

programming interfaces (APIs) that are part of the.NET Framework. These attributes might be

of interest to a host of the CLR, such as SQL Server. Examples of such host protection attributes

(HPAs) include:

, which indicates whether the API exposes the ability to create or manage

shared state (for example, static class fields).

, which indicates whether the API exposes the ability to perform

synchronization between threads.

, which indicates whether the API exposes a way to control the host

process.

Given these attributes, SQL Server specifies a list of HPAs that are disallowed in the hosted

environment through code access security (CAS). The CAS requirements are specified by one of

three SQL Server permission sets:

,

, or. One of these three

security levels is specified when the assembly is registered on the server, using the

statement. Code executing within the

or

permission sets must

avoid certain types or members that have the

attribute applied. For more information,

see

Create an assembly

and

CLR integration programming model restrictions.

The

isn't a security permission as much as a way to improve

reliability, in that it identifies specific code constructs, either types or methods, that the host

might disallow. The use of the

enforces a programming model that

helps protect the stability of the host.

HPAs identify types or members that don't fit the host programming model and represent the

following increasing levels of reliability threat:

Are otherwise benign.

Could lead to destabilization of server-managed user code.

```sql
SharedState
Synchronization
ExternalProcessMgmt
SAFE
EXTERNAL_ACCESS
UNSAFE
CREATE
ASSEMBLY
SAFE
EXTERNAL_ACCESS
System.Security.Permissions.HostProtectionAttribute
HostProtectionAttribute
HostProtectionAttribute
```

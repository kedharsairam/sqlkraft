---
title: "Impersonation & credentials"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  In the SQL Server common language runtime (CLR) integration, using Windows Authentication

  is complex, but is more secure than using SQL Server Authent
tags:
  - "clr-integration"
  - "impersonation-credentials"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

In the SQL Server common language runtime (CLR) integration, using Windows Authentication

is complex, but is more secure than using SQL Server Authentication. When using Windows

Authentication, keep in mind the following considerations.

By default, a SQL Server process that connects out to Windows acquires the security context of

the SQL Server Windows service account. But it's possible to map a CLR function to a proxy

identity, so that its outbound connections have a different security context than the Windows

service account.

In some cases, you might want to impersonate the caller by using the

property instead of running as the service account. The

instance represents the identity of the client that invoked the calling code,

and is only available when the client used Windows Authentication. After you obtain the

instance, you can call

to change the security token of the thread,

and then open ADO.NET connections on behalf of the client.

After you call

, you can't access local data and you

can't access system data. To access data again, you have to call

.

The following C# example shows how to impersonate the caller by using the

property.

C#

```sql
SqlContext.WindowsIdentity
WindowsIdentity
WindowsIdentity
Impersonate
SQLContext.WindowsIdentity.Impersonate
WindowsImpersonationContext.Undo
SqlContext.WindowsIdentity
WindowsIdentity clientId =
null
;
WindowsImpersonationContext impersonatedUser =
null
;
clientId = SqlContext.WindowsIdentity;
// This outer try block is used to protect from
// exception filter attacks which would prevent
// the inner finally block from executing and
// resetting the impersonation.
try
{
try
{
impersonatedUser = clientId.Impersonate();
if
(impersonatedUser !=
null
)
```

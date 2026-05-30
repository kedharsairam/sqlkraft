---
title: "Failed components after an upgrade"
topic: "query-processing"
description: "You might see the following behavior after the upgrade:"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

You might see the following behavior after the upgrade:

Replication continues to succeed but changes to the publication fail.

Replication Monitor in SQL Server Management Studio (SSMS) fails.

Agent status in the SSMS UI fails.

A remote distributor uses a linked server for communication between the publisher and

distributor. The secure default introduced in SQL Server 2025 (17.x) of the OLEDB 19 provider

requires that

.

You can resolve this issue preemptively before you start the upgrade, or you can resolve the

issue if replication components fail after an upgrade.

If you know that your SQL Server instance is going to encounter this issue after an upgrade,

you can preemptively mitigate the failure by configuring the SQL Server instance to use a

public commercial certificate

or a certificate from an

internal certificate authority

.

This is the recommended option for maximum security.

If your replication components fail after an upgrade, you can still configure the SQL Server

instance to use a

public commercial certificate

or a certificate from an

internal certificate

authority

.

Alternatively, you can choose the less secure option to override the secure default of the

OLEDB 19 provider and set

so the distributor trusts the

self-signed certificate.

To override the new secure default, use the

sp_changedistributor_property

stored procedure to

set the

option to

:

７

Note

### sp_changedistributor_property

```sql
TrustServerCertificate=False
```

```sql
trust_distributor_certificate=yes
```

`trust_distributor_certificate`

`yes`

```sql
EXECUTE sp_changedistributor_property
@property = N
'trust_distributor_certificate'
,
@
value
= N
'yes'
;
```

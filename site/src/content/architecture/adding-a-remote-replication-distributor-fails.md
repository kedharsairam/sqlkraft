---
title: "Adding a remote replication distributor fails"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

SQL Server 2025 (17.x) includes changes to

encryption

that introduce a breaking change to

Transactional

,

Snapshot

,

Peer-to-peer

, and

Merge

replication.

When configuring a distributor for replication, the

sp_adddistributor

stored procedure fails

when:

The publisher is a SQL Server 2025 (17.x) instance.

The distributor is remote.

The distributor isn't configured with a trusted certificate.

You might see the following error when running

on the publisher instance:

error-text

A remote distributor uses a linked server for communication between the publisher and

distributor. The secure default introduced in SQL Server 2025 (17.x) of the OLEDB 19 provider

requires that

.

To resolve this issue, configure the distributor SQL Server instance to use a

public commercial

certificate

or a certificate from an

internal certificate authority

.

Alternatively, you can choose the less secure option to override the secure default of the

OLEDB 19 provider and set

so the distributor trusts the self-

signed certificate. To override the default, use the

parameter

when calling the

sp_adddistributor

stored procedure:

Secure defaults pertain to the underlying OLEDB provider 19, which enhances security. The

option to override the default is less secure than configuring your instance to use a

trusted certificate. After overriding the default, you have the option to configure SQL

Server to use a certificate, and then use the

stored

procedure to set the

property back to the secure

default.

### sp_changedistributor_property

`sp_adddistributor`

```sql
TrustServerCertificate=False
```

```sql
TrustServerCertificate=True
```

`trust_distributor_certificate`

```sql
trust_distributor_certificate=no
```

```sql
OLE DB provider "MSOLEDBSQL19" for linked server "repl_distributor" returned message
"Client unable to establish connection".
Msg -2146893019, Level 16, State 1, Line 21
SSL Provider: The certificate chain was issued by an authority that is not trusted.
EXECUTE sys.sp_adddistributor @trust_distributor_certificate =
'yes'
;
```

---
title: 'Full-Text queries and populations fail after upgrade'
topic: 'io-fundamentals'
description: 'SQL Server 2025 (17.x) includes changes to'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

SQL Server 2025 (17.x) includes changes to

encryption

that introduce a breaking change to

log

shipping

. You might encounter these issues when you upgrade.

Log shipping monitoring can break if the monitor is a remote SQL Server 2025 (17.x) instance

when other SQL Server instances in the log shipping topology use a previous version.

For information about how to connect securely to SQL Server 2025 (17.x) instances, see

TDS

8.0

.

SQL Server 2025 (17.x) removes all legacy word breaker and filter binaries used by

Full-Text

Search

. These components are rebuilt with a modern toolset and offer expanded support for

more languages and document types. For more information, see

Behavior changes in Full-Text

Search

. Existing indexes after upgrade are designated with

as per

sys.fulltext_indexes

. Newly created indexes are version 2 and use the new components, unless

you specify otherwise by using the

FULLTEXT_INDEX_VERSION

database scoped configuration.

Any Full-Text query on a version 1 index fails to find the word breaker binaries on disk

immediately after upgrade:

Output

７

Note

Secure defaults pertain to the underlying OLEDB provider 19, which enhances security. The

option to override the default is less secure than configuring your instance to use a

trusted certificate. After overriding the default, you have the option to configure SQL

Server to use a certificate, and then use the

stored

procedure to set the

property back to the secure

default.

```sql
index_version = 1
```

```sql
trust_distributor_certificate=no
```

```sql
Msg 30010, Level 16, State 2, Line 8
An error has occurred during the full-text query. Common causes include: word-
breaking errors or timeout, FDHOST permissions/ACL issues, service account missing
privileges, malfunctioning IFilters, communication channel issues with FDHost and
sqlservr.exe, etc. If recently performed in-place upgrade to SQL2025, For help
please see https://aka.ms/sqlfulltext.
```

---
title: "LocalDBShareInstance"
topic: "clr-integration"
description: |
  07/14/2025

  Applies to:

  SQL Server

  Shares the specified SQL Server Express LocalDB instance with other users of the computer,

  using the specified shared name.

  C++

  [Input] The SID of the instance
tags:
  - "clr-integration"
  - "localdbshareinstance"
pubDate: 2025-12-01
---

07/14/2025

Applies to:

SQL Server

Shares the specified SQL Server Express LocalDB instance with other users of the computer,

using the specified shared name.

C++

[Input] The SID of the instance owner.

[Input] The private name for the LocalDB instance to share.

[Input] The shared name for the LocalDB instance to share.

[Input] Reserved for future use. Currently should be set to

.

```sql
msoledbsql.h
0
HRESULT
LocalDBShareInstance (
PSID pOwnerSID ,
PCWSTR pInstancePrivateName ,
PCWSTR pInstanceSharedName ,
DWORD dwFlags
);
```

---
title: "CreateVersionedSOSHostObject"
topic: "event-classes"
description: |
  Article

  •

  02/07/2024

  Creates a versioned object for the root hosting interface.

  This article describes a native code API that is used by SQL Server and may also be called by

  other Microsoft produ
tags:
  - "event-classes"
  - "createversionedsoshostobject"
pubDate: 2025-12-01
---

Article

•

02/07/2024

Creates a versioned object for the root hosting interface.

This article describes a native code API that is used by SQL Server and may also be called by

other Microsoft products.

C

interfacIid

[in]

Versioned interface identifier.

clientId

[in]

Unique client identifier.

scClientName

[in]

Hosting client name.

ppHost

Host object returned.

```cmd
CreateVersionedSOSHostObject(
REFIID interfacIid,
const
SOSHOST_CLIENTID clientId,
const
PCWSTR szClientName
);
```

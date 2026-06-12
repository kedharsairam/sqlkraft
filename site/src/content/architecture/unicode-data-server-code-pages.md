---
title: "Unicode data & server code pages"
topic: "clr-integration"
description: "The Extended Stored Procedure API is enabled for Unicode data; however, it isn't enabled for Unicode metadata."
tags: ["clr-integration","unicode-data-server-code-pages"]
pubDate: "2025-12-01"
---

The Extended Stored Procedure API is enabled for Unicode data; however, it isn't enabled for

Unicode metadata. The

Unicode directive doesn't have any effect on the Extended

Stored Procedure API.

All metadata returned by, or provided to the Extended Stored Procedure API by your extended

stored procedure application is assumed to be in the multibyte code page of the server. The

default code page of an Extended Stored Procedure API server application is the ANSI code

page of the computer on which the application is running, which can be obtained by calling

with the field parameter set to.

If your Extended Stored Procedure API application is Unicode-enabled, you must convert your

Unicode metadata column names, error messages, and so on, to multibyte data before passing

this data to the Extended Stored Procedure API.

The following extended stored procedure provides an example of the Unicode conversions

discussed.

Column data is passed as Unicode data to

because the column is described

to be SRVNVARCHAR.

Column name metadata is passed to

as multibyte data.

The extended stored procedure calls

with the field parameter set to

to obtain the multibyte code page of SQL Server.

Error messages are passed to

as multibyte data.

C++

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR Integration instead.

```sql
#define srv_pfield
SRV_SPROC_CODEPAGE srv_describe srv_describe srv_pfield
SRV_SPROC_CODEPAGE srv_sendmsg
```

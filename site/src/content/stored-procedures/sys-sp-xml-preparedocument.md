---
name: "sys.sp_xml_preparedocument"
title: "sp_xml_preparedocument"
category: "general"
description: "Number of characters into the currently executing batch or stored procedure at occurs."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "sp_xml_preparedocument"
---

## Description

Number of characters into the currently executing batch or stored procedure at occurs.

## Syntax

`sp_xml_preparedocument`

## Remarks

Number of characters into the currently

executing batch or stored procedure at

occurs. Can be used together with the

management function to retrieve the

currently executing statement for the

Number of characters into the currently

executing batch or stored procedure at

occurs. Can be used together with the

management function to retrieve the

currently executing statement for the

Timestamp when

was called.

Size of the unparsed XML document in

Size of the unparsed XML namespace

document, in bytes. NULL if there is no

namespace document.

Number of OPENXML calls with this

document handle.

Number of rows returned by all previous

OPENXML calls for this document handle.

Milliseconds since the last OPENXML call. If

OPENXML has not been called, returns

milliseconds since the

The lifetime of

used to retrieve the SQL text that executed a call to

outlives the cached plan used to execute the query. If the query text

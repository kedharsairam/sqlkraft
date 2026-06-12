---
name: "sys.sp_xml_removedocument"
title: "sp_xml_removedocument"
category: "general"
description: "Removes the internal representation of the XML document specified by the document handle and invalidates the document handle. A parsed document is stored in the internal cache of SQL Server. The MSXML parser ) uses one-eighth the total memory available for SQL Server. To avoid running The handle to the newly created document."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_xml_removedocument"
---

## Description

Removes the internal representation of the XML document specified by the document handle and invalidates the document handle. A parsed document is stored in the internal cache of SQL Server. The MSXML parser ) uses one-eighth the total memory available for SQL Server. To avoid running The handle to the newly created document. A handle that isn't valid returns an error.

## Syntax

`sp_xml_removedocument`

## Permissions

## Examples

### Example 1

```sql
EXECUTE sp_xml_removedocument @hdoc;
```

### Example 2

```sql
EXEC sp_xml_removedocument @idoc;
```

---
name: "sys.sp_xml_removedocument"
title: "sp_xml_removedocument"
category: "general"
description: "SQL database in Microsoft Fabric Removes the internal representation of the XML document specified by the document handle and invalidates the document handle. A parsed document is stored in the internal cache of SQL Server. The MSXML parser ) uses one-eighth the total memory available for SQL Server. To avoid running Transact-SQL syntax conventions The handle to the newly created document."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_xml_removedocument"
---

## Description

SQL database in Microsoft Fabric Removes the internal representation of the XML document specified by the document handle and invalidates the document handle. A parsed document is stored in the internal cache of SQL Server. The MSXML parser ) uses one-eighth the total memory available for SQL Server. To avoid running Transact-SQL syntax conventions The handle to the newly created document. A handle that isn't valid returns an error.

## Syntax

`sp_xml_removedocument`

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Removes the internal representation of the XML document specified by the document handle and invalidates the document handle. A parsed document is stored in the internal cache of SQL Server. The MSXML parser ( ) uses one-eighth the total memory available for SQL Server. To avoid running out of memory, run to free up the memory. Transact-SQL syntax conventions syntaxsql The handle to the newly created document. A handle that isn't valid returns an error. hdoc is an . (success) or (failure). ） Important Arguments for extended stored procedures must be entered in the specific order as described in the section. If the parameters are entered out of order, an error message occurs.

## Examples

### Example 1

```sql
EXECUTE sp_xml_removedocument @hdoc;
```

### Example 2

```sql
EXEC sp_xml_removedocument @idoc;
```

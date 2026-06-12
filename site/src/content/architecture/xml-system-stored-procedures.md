---
title: "XML System Stored Procedures"
topic: "xml-data"
description: "provides the following system stored procedures that are used together with OPENX"
tags: ["xml-data","xml-system-stored-procedures"]
pubDate: 2025-12-01
---

provides the following system stored procedures that are used together with

OPENXML:

sp_xml_preparedocument (Transact-SQL)

sp_xml_removedocument (Transact-SQL)

To write queries by using OPENXML, you must first create an internal representation of the

XML document by calling. The stored procedure returns a handle to

the internal representation of the XML document. This handle is then passed to OPENXML.

OPENXML provides rowset views of the document based on XPaths. Specifically, this is one row

pattern and one or more column patterns.

The internal representation of an XML document can be removed from memory by calling the

system stored procedure.

OPENXML (Transact-SQL)

OPENXML (SQL Server)

７

Note

The document handle that is returned by

is valid for the duration

of the session.

```sql
sp_xml_preparedocument sp_xml_removedocument sp_xml_preparedocument
```

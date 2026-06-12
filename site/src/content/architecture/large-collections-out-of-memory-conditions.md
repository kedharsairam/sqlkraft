---
title: "Large collections & out-of-memory conditions"
topic: "xml-data"
description: ""
tags: ["xml-data","large-collections-out-of-memory-conditions"]
pubDate: 2025-12-01
---

During a call to the built-in XML_SCHEMA_NAMESPACE() function on a large XML schema

collection, or when you try to drop large XML schema collections, an out-of-memory condition

may occur. The following are solutions you can use to handle this:

When the system load is light, use the DROP_XML_SCHEMA_COLLECTION command. If

this fails, put the database in single-user mode by using the ALTER DATABASE statement

and trying DROP XML SCHEMA COLLECTION again. If the XML schema collection exists in

,

, or

, a server restart is required for single-user mode.

When you call the XML_SCHEMA_NAMESPACE, you can try to retrieve a single XML

schema namespace, you can try the call when the system load is lighter, or you can try

the call in single-user mode.

Requirements and Limitations for XML Schema Collections on the Server

```sql
master model tempdb
```

---
title: "The <xsd:redefine> Element"
topic: "xml-data"
description: "The W3C XSD element provides support for redefining schema components."
tags: ["xml-data","the-xsdredefine-element"]
pubDate: 2025-12-01
---

The W3C XSD

element provides support for redefining schema components. However,

support for this directive is potentially costly to performance and also requires that SQL Server

revalidate all instances of the

data type associated with the redefined schema. Therefore,

doesn't support this element. XML schemas that include the

element are rejected by the server.

To update a schema or its components, you can do the following instead:

1. Create a new XML Schema collection with the modified schema components.

2. Retype all

data types (XML DT) that use the XML Schema collection to be redefined to

use the new XML Schema collection instead. To do this, use the ALTER COLUMN option of

the ALTER TABLE command for retyping columns, or change the XML Schema collection

constraints on variables or parameters.

3. Drop the old version of the XML Schema collection.

Requirements and Limitations for XML Schema Collections on the Server

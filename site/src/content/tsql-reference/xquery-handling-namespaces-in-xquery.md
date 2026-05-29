---
name: "xquery-handling-namespaces-in-xquery"
title: "XQuery - Handling Namespaces in XQuery"
category: "xquery"
description: "XQuery Language Reference: Handling Namespaces in XQuery"
syntax: |
  SELECT Instructions.query('
  declare namespace
  AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
  works/ProductModelManuInstructions";
  /AWMI:root/AWMI:Location[1]/AWMI:step
  ') as x
  FROM Production.ProductModel
  WHERE ProductModelID=7
  <AWMI:step xmlns:AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
  works/ProductModelManuInstructions">Insert <AWMI:material>aluminum sheet MS-
  2341</AWMI:material> into the <AWMI:tool>T-85A framing tool</AWMI:tool>.
  </AWMI:step>
  ...
tags:
  - "xquery"
  - "handling-namespaces-in-xquery"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

This topic provides samples for handling namespaces in queries.

The following query retrieves the manufacturing steps of a specific product model.

This is the partial result:

Note that the

keyword is used to define a new namespace prefix, "AWMI:". This

prefix then must be used in the query for all elements that fall within the scope of that

namespace.

In the previous query, a new namespace prefix was defined. That prefix then had to be used in

the query to select the intended XML structures. Alternatively, you can declare a namespace as

the default namespace, as shown in the following modified query:

```sql
SELECT Instructions.query('
declare namespace
AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
/AWMI:root/AWMI:Location[1]/AWMI:step
') as x
FROM Production.ProductModel
WHERE ProductModelID=7
<AWMI:step xmlns:AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions">Insert <AWMI:material>aluminum sheet MS-
2341</AWMI:material> into the <AWMI:tool>T-85A framing tool</AWMI:tool>.
</AWMI:step>
...
```
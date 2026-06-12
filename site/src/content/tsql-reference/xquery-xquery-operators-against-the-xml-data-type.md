---
name: "xquery-xquery-operators-against-the-xml-data-type"
title: "XQuery - XQuery Operators Against the xml Data Type"
category: "xquery"
description: "XQuery Language Reference: XQuery Operators Against the xml Data Type"
syntax: |
  WITH
    XMLNAMESPACES
    (
    'https://schemas.microsoft.com/sqlserver/2004/07/adventure-works/ContactInfo'
    AS
    ACI,
    'https://schemas.microsoft.com/sqlserver/2004/07/adventure-works/ContactTypes'
    AS
    ACT)
    SELECT
    ContactID
    FROM
    Person.Contact
    WHERE
    AdditionalContactInfo.value(
    '
    //ACI:AdditionalContactInfo//ACT:telephoneNumber/ACT:number =
    ("111-111-1111", "222-2222")'
    ,
    'bit'
    )=
    cast
    (1
    as
    bit
    )
tags: ["xquery","xquery-operators-against-the-xml-data-type"]
pubDate: "2025-12-01"
---

XQuery supports the following operators:

Numeric operators (+, -, \*, div, mod)

Operators for value comparison (eq, ne, lt, gt, le, ge)

Operators for general comparison ( =, !=, <, >, <=, >= )

For more information about these operators, see

Comparison Expressions (XQuery)

The query illustrates the use of general operators that apply to sequences, and also to compare

sequences. The query retrieves a sequence of telephone numbers for each customer from the

column of the

table. This sequence is then compared with the

sequence of two telephone numbers ("111-111-1111", "222-2222").

The query uses the

comparison operator. Each node in the sequence on the right side of the

operator is compared with each node in the sequence on the left side. If the nodes match,

the node comparison is. It is then converted to an int and compared with 1, and the

query returns the customer ID.

```sql
WITH
XMLNAMESPACES (
'https://schemas.microsoft.com/sqlserver/2004/07/adventure-works/ContactInfo'
AS
ACI,
'https://schemas.microsoft.com/sqlserver/2004/07/adventure-works/ContactTypes'
AS
ACT)
SELECT
ContactID
FROM
Person.Contact
WHERE
AdditionalContactInfo.value(
'
//ACI:AdditionalContactInfo//ACT:telephoneNumber/ACT:number =
("111-111-1111", "222-2222")'
,
'bit'
)=
cast (1 as bit
)
```

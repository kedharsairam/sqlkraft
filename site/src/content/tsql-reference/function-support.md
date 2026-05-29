---
name: "Function support"
title: "Function support"
category: "statements"
description: "data type must be a JSON object or a JSON array. Scalars, booleans, and"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

SQL

Input to the

data type must be a JSON object or a JSON array. Scalars, booleans, and

values are not supported. The JSON data type conforms to IETF RFC 4627 which allows only a

JSON object or array. The

data type and all JSON functions only work with IETF RFC 4627

compliant JSON documents.

The

ISJSON

function can be used to validate a string that contains JSON document conforms

to IETF RFC 8259. An IETF RFC 8259 conformant JSON document contains only a JSON scalar

value at top level.

For example:

SQL

### json

### json

### json

### json

### json

### json

### char

### nchar

### varchar

### nvarchar

### xml

### char

### nchar

### varchar

### nvarchar

### json

### json

### varchar(max)

### varbinary(max)

### nvarchar(max)

### xml

### varchar(max)

### json

### xml

### json

### json

### json

### json

### varchar

### nvarchar

### json

```sql
NULL
```

```sql
DROP
TABLE
IF
EXISTS
JsonTable;
CREATE
TABLE
JsonTable
(
id
INT
PRIMARY
KEY
,
d
JSON
);
INSERT
INTO
JsonTable (
id
, d)
VALUES
(1,
'{"a":1, "b":"abc", "c":true}'
);
UPDATE
JsonTable
SET
d.modify(
'$.a'
, 14859)
WHERE
id
= 1;
UPDATE
JsonTable
SET
d.modify(
'$.b'
,
'def'
)
WHERE
id
= 1;
```

```sql
DECLARE
@
true
JSON
=
'true'
;
-- invalid
DECLARE
@
false
JSON
=
'false'
;
-- invalid
DECLARE
@
number
JSON
=
'1234.56'
;
-- invalid
DECLARE
@
string
JSON
=
'"contoso"'
;
-- invalid
DECLARE
@
null
JSON
=
'null'
-- invalid
DECLARE
@
null
JSON
=
NULL
-- valid
DECLARE
@
object
JSON
=
'{}'
-- valid
DECLARE
@
array
JSON
=
'[]'
-- valid
```

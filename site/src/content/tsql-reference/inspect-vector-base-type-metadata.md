---
name: 'Inspect vector base type metadata'
title: 'Inspect vector base type metadata'
category: 'predicates'
description: 'The following query confirms actual base type and dimensions of a'
tags: ["tsql", "predicates"]
pubDate: 2026-05-29
---

The following query confirms actual base type and dimensions of a

column:

SQL

Output columns:

: Number of dimensions defined for the vector.

: Internal numeric code for the base type:

=

=

: Human-readable description of the base type.

### varchar

### nvarchar

### json

### vector

### vector

```sql
vector_dimensions
```

```sql
vector_base_type
```

```sql
0
```

```sql
float32
1
```

```sql
float16
vector_base_type_desc
```

```sql
CREATE
VECTOR
INDEX
vec_idx
ON
Articles(embedding)
WITH
(
metric =
'cosine'
,
type
=
'diskANN'
);
-- Step 5: Perform a Vector Similarity Search
DECLARE
@qv
AS
VECTOR(5, float16) =
'[0.3, 0.3, 0.3, 0.3, 0.3]'
;
SELECT
t.id,
t.title,
t.content,
s.distance
FROM
VECTOR_SEARCH(
table
= Articles
AS
t,
column
= embedding,
similar_to = @qv,
metric =
'cosine'
,
top_n = 3
)
AS
s
ORDER
BY
s.distance, t.title;
```

```sql
--Inspect Vector Base type Metadata in sys.columns
SELECT
name
AS
column_name,
system_type_id,
user_type_id,
vector_dimensions,
vector_base_type,
vector_base_type_desc
FROM
sys.columns
WHERE
object_id = OBJECT_ID(
'dbo.Articles'
);
```

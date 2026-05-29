---
name: "Expected behaviors"
title: "Expected behaviors"
category: "statements"
description: "The following sample demonstrates the INNER JOIN with filtering on multiple tables. Use when"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

The following sample demonstrates the INNER JOIN with filtering on multiple tables. Use when

embeddings are stored in a separate table from the main entity data.

SQL

: The alias

from

is

available in the WHERE clause for iterative filtering with latest version indexes

If you attempt to use the

parameter in

when querying a table with a

latest version vector index, SQL Server returns the following error:

### To resolve this error:

### Incorrect (produces error with latest version index):

### Correct (works with latest version index):

#### Aspect

#### Earlier version

#### Latest version

#### Predicate

#### application

## Iterative filtering behavior

1. Remove the

parameter from the

function

2. Use

## syntax instead

SQL

SQL

The latest version introduces significant improvements over earlier vector index versions:

Relational predicates were applied after

vector search returned a fixed number

of nearest neighbors (post-filtering

only)

Relational predicates are applied during the

vector search process (iterative filtering)

ﾉ

Expand table

#### Aspect

#### Earlier version

#### Latest version

#### Result

#### completeness

#### TOP (N) tuning

#### Query

#### optimization

### ORDER BY must be present

### Only distance column allowed

### Ascending order only

### Valid ORDER BY:

## ORDER BY clause requirements

Queries could return fewer rows—or no

rows—if the initial nearest neighbors

didn't satisfy filters, even when

qualifying rows existed

Queries return the expected number of rows

when qualifying data exists, without manual

tuning or query rewrites

Users often had to guess or oversample

TOP (N) values to compensate for post-

filtering

No need to guess TOP (N) values. The engine

searches until enough qualifying rows are

found or the search space is exhausted

Not applicable

SQL Server automatically selects the most

efficient execution strategy, including

switching between vector index seeks and

kNN scans when appropriate

For a practical example of iterative filtering, see

Example C: Vector search with iterative filtering

.

When using

, the ORDER BY clause has specific requirements:

: Queries without an ORDER BY clause fail with error .

: The ORDER BY clause must reference only the distance

column from the VECTOR_SEARCH result set. Including additional columns fails with error.

To sort by multiple columns, use the subquery pattern described in

Multiple ORDER BY

columns

.

: The distance column must be ordered in ascending order (ASC).

Descending order (DESC) is not supported.

SQL

✓

### Invalid ORDER BY patterns:

## Behavior without a vector index

## Query behavior without TOP WITH APPROXIMATE

SQL

can execute queries even when no vector index exists on the target column.

Without an index, the query performs a full table scan (k-nearest neighbor (kNN) search) to

calculate distances for all rows.

✗

✗

✗

### No TOP, no ORDER BY, or ORDER BY non-distance

### TOP (no APPROXIMATE) with ORDER BY distance

### Example - Full scan with distance column:

### Example - kNN search (exact nearest neighbors):

## TOP WITH APPROXIMATE without VECTOR_SEARCH

When using

without

, the query behavior

depends on the presence of

and

clauses:

: Full table scan (brute-force search)

that calculates and returns distances for all rows

: Executes as a kNN (k-nearest

neighbors) search, which is an exact nearest neighbor search

SQL

SQL

Using

without a

function in the query results

in an error. The

clause requires a

function to be present.

### Incorrect - This query fails:

### Correct - Use VECTOR_SEARCH:

### Example workflow:

## TRUNCATE TABLE restrictions

SQL

SQL

Tables with vector indexes cannot be truncated using

. To remove all data from

a vector-indexed table:

1. Drop the vector index

2. Truncate the table

3. Repopulate the table with at least 100 rows

4. Recreate the vector index

SQL

### Syntax:

### Example:

## Table hints for vector search

You can use table hints with the

function to control query execution behavior.

The

table hint forces the query optimizer to use only the approximate nearest

neighbor (ANN) index, even when the optimizer might otherwise choose a different execution

strategy.

SQL

The following example forces the use of the approximate nearest neighbor index for the vector

search query:

SQL

```sql
e
```

```sql
TABLE = wikipedia_articles_embeddings AS e
```

```sql
TOP_N
```

```sql
VECTOR_SEARCH
```

```sql
-- Assuming a schema with separate tables for articles and embeddings
DECLARE
@qv VECTOR(1536) = AI_GENERATE_EMBEDDINGS(N
'artificial intelligence and
machine learning'
USE
MODEL
Ada2Embeddings);
SELECT
TOP (10)
WITH
APPROXIMATE
a.id,
a.title,
a.category,
vs.distance
FROM
wikipedia_articles a
INNER
JOIN
VECTOR_SEARCH(
TABLE
= wikipedia_articles_embeddings
AS
e,
COLUMN
= content_vector,
SIMILAR_TO = @qv,
METRIC =
'cosine'
)
AS
vs
ON
a.id = e.article_id
WHERE
e.approved = 1
-- Iterative filter on embedding
table
AND
a.category
IN
(
'Technology'
,
'Science'
)
-- Filter on main table
AND
a.views > 50000
ORDER
BY
vs.distance;
```

```sql
Msg 42274, Level 16, State 1
Vector search with version 3 index does not support explicit TOP_N parameter.
```

```sql
TOP_N
```

```sql
VECTOR_SEARCH
```

```sql
SELECT TOP (N) WITH APPROXIMATE
```

```sql
SELECT
TOP (10)
t.id,
r.distance
FROM
VECTOR_SEARCH(
TABLE
= dbo.wikipedia_articles
AS
t,
COLUMN
= title_vector,
SIMILAR_TO = @qv,
METRIC =
'cosine'
,
TOP_N = 10
-- This parameter causes the error with latest version indexes
)
AS
r;
SELECT
TOP (10)
WITH
APPROXIMATE
-- Specify TOP and WITH APPROXIMATE here
t.id,
r.distance
FROM
VECTOR_SEARCH(
TABLE
= dbo.wikipedia_articles
AS
t,
COLUMN
= title_vector,
SIMILAR_TO = @qv,
METRIC =
'cosine'
-- No TOP_N parameter
)
AS
r
ORDER
BY
r.distance;
```

```sql
SELECT TOP (N) WITH APPROXIMATE
```

```sql
SELECT
TOP (10)
WITH
APPROXIMATE
t.id,
t.title,
r.distance
FROM
VECTOR_SEARCH(
TABLE
= products,
COLUMN
= embedding,
SIMILAR_TO = @query_vector,
METRIC =
'cosine'
)
AS
r
INNER
JOIN
products t
ON
t.id = r.id
ORDER
BY
r.distance;
--
```

```sql
Valid
```

```sql
VECTOR_SEARCH
```

```sql
-- Missing ORDER BY
SELECT
TOP (10)
WITH
APPROXIMATE
r.distance
FROM
VECTOR_SEARCH(
TABLE
= products,
COLUMN
= embedding,
SIMILAR_TO = @query_vector,
METRIC =
'cosine'
)
AS
r;
--
```

```sql
Error Msg 42248: APPROXIMATE cannot be used in a query without ORDER BY
-- Multiple columns in ORDER BY
SELECT
TOP (10)
WITH
APPROXIMATE
t.title,
r.distance
FROM
VECTOR_SEARCH(
TABLE
= products,
COLUMN
= embedding,
SIMILAR_TO = @query_vector,
METRIC =
'cosine'
)
AS
r
INNER
JOIN
products t
ON
t.id = r.id
ORDER
BY
r.distance, t.title;
--
```

```sql
Error Msg 42271: TOP WITH APPROXIMATE and VECTOR_SEARCH requires ORDER BY
-- on distance column ascending, and no other columns
-- Descending order
SELECT
TOP (10)
WITH
APPROXIMATE
r.distance
FROM
VECTOR_SEARCH(
TABLE
= products,
COLUMN
= embedding,
SIMILAR_TO = @query_vector,
METRIC =
'cosine'
)
AS
r
ORDER
BY
r.distance
DESC
;
--
```

```sql
Error Msg 42271: TOP WITH APPROXIMATE and VECTOR_SEARCH requires ORDER BY
-- on distance column ascending, and no other columns
```

```sql
VECTOR_SEARCH
```

```sql
SELECT TOP (N) WITH APPROXIMATE
```

```sql
TOP
```

```sql
ORDER BY
```

```sql
SELECT TOP (N) WITH APPROXIMATE
```

```sql
VECTOR_SEARCH
```

```sql
WITH APPROXIMATE
```

```sql
VECTOR_SEARCH
```

```sql
-- Returns all rows with calculated distances
SELECT
t.id,
t.title,
r.distance
FROM
VECTOR_SEARCH(
TABLE
= dbo.wikipedia_articles
AS
t,
COLUMN
= title_vector,
SIMILAR_TO = @qv,
METRIC =
'cosine'
)
AS
r
ORDER
BY
t.id;
-- Not ordering by distance
-- Returns exact top 10 nearest neighbors using kNN
SELECT
TOP (10)
t.id,
t.title,
r.distance
FROM
VECTOR_SEARCH(
TABLE
= dbo.wikipedia_articles
AS
t,
COLUMN
= title_vector,
SIMILAR_TO = @qv,
METRIC =
'cosine'
)
AS
r
ORDER
BY
r.distance;
-- No WITH APPROXIMATE = exact kNN
```

```sql
TRUNCATE TABLE
```

```sql
-- Error: WITH APPROXIMATE requires VECTOR_SEARCH
SELECT
TOP (10)
WITH
APPROXIMATE
id
,
title,
VECTOR_DISTANCE(
'cosine'
, title_vector, @qv)
AS
distance
FROM
dbo.wikipedia_articles
WHERE
title_vector
IS
NOT
NULL
ORDER
BY
VECTOR_DISTANCE(
'cosine'
, title_vector, @qv);
-- Correct: WITH APPROXIMATE with VECTOR_SEARCH
SELECT
TOP (10)
WITH
APPROXIMATE
t.id,
t.title,
r.distance
FROM
VECTOR_SEARCH(
TABLE
= dbo.wikipedia_articles
AS
t,
COLUMN
= title_vector,
SIMILAR_TO = @qv,
METRIC =
'cosine'
)
AS
r
ORDER
BY
r.distance;
```

```sql
-- Step 1: Drop the vector index
DROP
INDEX
idx_vector
ON
wikipedia_articles;
-- Step 2: Truncate the table
```

```sql
VECTOR_SEARCH
```

```sql
FORCE_ANN_ONLY
```

```sql
TRUNCATE
TABLE
wikipedia_articles;
-- Step 3: Repopulate with data (at least 100 rows)
-- ... insert operations ...
-- Step 4: Recreate the vector index
CREATE
VECTOR
INDEX
idx_vector
ON
wikipedia_articles(title_vector)
WITH
(METRIC =
'cosine'
);
```

```sql
FROM VECTOR_SEARCH(
TABLE      = table_name,
COLUMN     = column_name,
SIMILAR_TO = vector_value,
METRIC     = 'metric_name'
) AS alias
WITH
(FORCE_ANN_ONLY)
DECLARE
@qembedding VECTOR(1536) = AI_GENERATE_EMBEDDINGS(N
'artificial
intelligence'
USE
MODEL
Ada2Embeddings);
SELECT
TOP 50
WITH
APPROXIMATE
t.id,
t.title,
r.distance
FROM
VECTOR_SEARCH(
TABLE
= dbo.wikipedia_articles
AS
t,
COLUMN
= title_vector,
SIMILAR_TO = @qembedding,
METRIC     =
'cosine'
```

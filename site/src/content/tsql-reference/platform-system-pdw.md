---
name: "Platform System (PDW)"
title: "Platform System (PDW)"
category: "statements"
description: "SET ROWCOUNT stops processing after the specified number of rows. In the following"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

SET ROWCOUNT stops processing after the specified number of rows. In the following

example, note that more than 20 rows meet the criteria of. However,

after applying SET ROWCOUNT, you can see that not all rows were returned.

To return all rows, set ROWCOUNT to 0.

SET Statements (Transact-SQL)

See Also

```sql
AccountType = 'Assets'
```

```sql
-- Uses AdventureWorks
SET
ROWCOUNT 5;
SELECT
*
FROM
[dbo].[DimAccount]
WHERE
AccountType =
'Assets'
;
-- Uses AdventureWorks
SET
ROWCOUNT 0;
SELECT
*
FROM
[dbo].[DimAccount]
WHERE
AccountType =
'Assets'
;
```

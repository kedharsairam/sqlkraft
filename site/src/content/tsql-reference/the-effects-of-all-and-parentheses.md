---
name: "the effects of ALL and parentheses"
title: "The effects of ALL and parentheses"
category: "operators"
description: ""
tags: ["tsql","operators"]
pubDate: "2026-05-29"
---

The following examples use

to combine the results of three tables that all have the same

five rows of data. The first example uses

to show the duplicated records, and returns

all 15 rows. The second example uses

without

to eliminate the duplicate rows from

the combined results of the three

statements, and returns five rows.

The third example uses

with the first

and parentheses enclose the second

that isn't using. The second

is processed first because it's in parentheses, and

## returns five rows because the

option isn't used and the duplicates are removed. These five

rows are combined with the results of the first

by using the

keywords. This

example doesn't remove the duplicates between the two sets of five rows. The final result has

10 rows.

CREATE TRIGGER (Transact-SQL)

CREATE VIEW (Transact-SQL)

DELETE (Transact-SQL)

EXECUTE (Transact-SQL)

Expressions (Transact-SQL)

INSERT (Transact-SQL)

LIKE (Transact-SQL)

Set Operators - UNION (Transact-SQL)

Set Operators - EXCEPT and INTERSECT (Transact-SQL)

UPDATE (Transact-SQL)

WHERE (Transact-SQL)

PathName (Transact-SQL)

SELECT - INTO clause (Transact-SQL)

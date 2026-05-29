---
name: 'sys.sp_helparticle'
title: 'sp_helparticle'
category: 'general'
description: 'Displays information about an article. This stored procedure is executed at the Publisher on the publication database. For Oracle Publishers, this stored procedure is executed at the Distributor Transact-SQL syntax conventions The name of an article in the publication. isn''t supplied, information on all articles for the specified publication is returned. Specifies whether the filter clause should '
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helparticle
  [ @publication = ]
  N
  'publication'
  [ , [ @article = ]
  N
  'article'
  ]
  [ , [ @returnfilter = ] returnfilter ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @found = ] found
  OUTPUT
  ]
  [ ; ]
---

## Description

Displays information about an article. This stored procedure is executed at the Publisher on the publication database. For Oracle Publishers, this stored procedure is executed at the Distributor Transact-SQL syntax conventions The name of an article in the publication. isn't supplied, information on all articles for the specified publication is returned. Specifies whether the filter clause should be returned.

## Syntax

```sql
sp_helparticle
[ @publication = ]
N
'publication'
[ , [ @article = ]
N
'article'
]
[ , [ @returnfilter = ] returnfilter ]
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @found = ] found
OUTPUT
]
[ ; ]
```

## Examples

### Example 1

```sql
sp_helparticle
```

### Example 2

```sql
DECLARE
@publication
AS
sysname;
SET
@publication = N
'AdvWorksProductTran'
;
USE
[AdventureWorks2022]
EXEC sp_helparticle
@publication = @publication;
GO
```

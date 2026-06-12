---
name: "sys.sp_fulltext_service"
title: "sp_fulltext_service"
category: "general"
description: "Changes the server properties of full-text search for SQL Server. The property to be changed or reset. , with no default. For a list of properties, their descriptions, and the values that can be set, see the table under the This argument returns the following properties: deprecation status, if applicable."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_fulltext_service
      [ [ @action = ]
      N
      'action'
      ]
      [ , [ @value = ] value ]
      [ ; ]
---

## Description

Changes the server properties of full-text search for SQL Server. The property to be changed or reset. , with no default. For a list of properties, their descriptions, and the values that can be set, see the table under the This argument returns the following properties: deprecation status, if applicable.

## Syntax

```sql
sp_fulltext_service
[ [ @action = ]
N
'action'
]
[ , [ @value = ] value ]
[ ; ]
```

## Arguments

Returns information related to the properties of the Full-Text Engine. These properties can be

set and retrieved by using

Is an expression containing the name of the full-text service-level property. The table lists the

properties and provides descriptions of the information returned.

Returns 0. Supported for backward compatibility only.

Returns 0. Supported for backward compatibility only.

The full-text component is installed with the current instance of SQL Server.

0 = Full-text is not installed.

1 = Full-text is installed.

The following properties will be removed in a future release of Microsoft SQL Server:. Avoid using these properties in new

development work, and plan to modify applications that currently use any of them.

Expand table

Note that to set signature verification back to its default value, 1, you can use the following

FULLTEXTCATALOGPROPERTY (Transact-SQL)

Metadata Functions (Transact-SQL)

sp_fulltext_service (Transact-SQL)

## Permissions

To update the list of languages registered with full-text search, use sp_fulltext_service with the option. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. sp_fulltext_load_thesaurus_file (Transact-SQL) sp_fulltext_service (Transact-SQL) Configure and manage word breakers and stemmers for search (SQL Server) Configure and Manage Thesaurus Files for Full-Text Search Configure and Manage Stopwords and Stoplists for Full-Text Search Upgrade Full-Text Search

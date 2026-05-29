---
name: 'sys.selective_xml_index_paths'
title: 'sys.selective_xml_index_paths (Transact-'
category: 'indexes'
description: '1 = maximum length is inferred.'
tags: ["catalog-view", "indexes"]
pubDate: 2026-05-29
---

## Description
1 = maximum length is inferred.

0 = node() hint not present.

1 = node() optimization hint applied.

ID of the system type of the column.

ID of the user type of the column.

Max Length (in bytes) of the type.

-1 = Column data type is varchar(max),

nvarchar(max), varbinary(max), or xml.

Maximum precision of the type if it is numeric-based.

Otherwise 0.

Maximum scale of the type if it is numeric-based.

Otherwise, 0.

Name of the collation of the type if it is character-

based. Otherwise, NULL.

0 = SINGLETON hint not present.

1 = SINGLETON optimization hint applied.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Catalog Views (Transact-SQL)

XML Schemas (XML Type System) Catalog Views (Transact-SQL)

See Also

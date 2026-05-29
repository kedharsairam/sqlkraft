---
name: 'sys.numbered_procedure_parameters'
title: 'sys.numbered_procedure_parameters'
category: 'objects'
description: '-1 = Column data type is varchar(max), nvarchar(max), or'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
-1 = Column data type is varchar(max), nvarchar(max), or

varbinary(max).

Precision of the parameter if numeric-based; otherwise, 0.

Scale of the parameter if numeric-based; otherwise, 0.

1 = Parameter is output or return; otherwise, 0

1 = Parameter is a cursor-reference parameter.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

７

Note

XML and CLR parameters are not supported for numbered procedures.

See Also

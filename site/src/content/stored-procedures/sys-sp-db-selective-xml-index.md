---
name: 'sys.sp_db_selective_xml_index'
title: 'sp_db_selective_xml_index'
category: 'general'
description: 'Enables and disables selective XML index (SXI) functionality on a SQL Server database. If called without any parameters, the stored procedure returns if SXI is enabled on a particular Transact-SQL syntax conventions The name of the database on which to to enable or disable selective XML index. , the current database is assumed. Determines whether to enable or disable the index. , and can be one of'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_db_selective_xml_index
  [ [ @dbname = ]
  N
  'dbname'
  ]
  [ , [ @selective_xml_index = ]
  'selective_xml_index'
  ]
  [ ; ]
---

## Description

Enables and disables selective XML index (SXI) functionality on a SQL Server database. If called without any parameters, the stored procedure returns if SXI is enabled on a particular Transact-SQL syntax conventions The name of the database on which to to enable or disable selective XML index. , the current database is assumed. Determines whether to enable or disable the index. , and can be one of the following values:

## Syntax

```sql
sp_db_selective_xml_index
[ [ @dbname = ]
N
'dbname'
]
[ , [ @selective_xml_index = ]
'selective_xml_index'
]
[ ; ]
```

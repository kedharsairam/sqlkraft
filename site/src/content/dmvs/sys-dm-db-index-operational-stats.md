---
name: "sys.dm_db_index_operational_stats"
title: "sys.dm_db_index_operational_stats"
category: "index"
description: "Returns the lower level data access, locking, and latching statistics for each partition of a table . Valid inputs are the ID number of a database, NULL, 0, or DEFAULT. The default is 0. NULL, 0, and DEFAULT are equivalent values in this Specify NULL to return information for all databases in the instance of SQL Server."
tags: ["index", "dmv"]
pubDate: 2026-05-29
syntax: |
  sys.dm_db_index_operational_stats (
  { database_id |
  NULL
  | 0 |
  DEFAULT
  }
  , { object_id |
  NULL
  | 0 |
  DEFAULT
  }
  , { index_id | 0 |
  NULL
  | -1 |
  DEFAULT
  }
  , { partition_number |
  NULL
  | 0 |
  DEFAULT
  }
  )
---

## Description

Returns the lower level data access, locking, and latching statistics for each partition of a table. Valid inputs are the ID number of a database, NULL, 0, or DEFAULT. The default is 0. NULL, 0, and DEFAULT are equivalent values in this Specify NULL to return information for all databases in the instance of SQL Server.

## Syntax

```sql
sys.dm_db_index_operational_stats (
{ database_id |
NULL
| 0 |
DEFAULT
}
, { object_id |
NULL
| 0 |
DEFAULT
}
, { index_id | 0 |
NULL
| -1 |
DEFAULT
}
, { partition_number |
NULL
| 0 |
DEFAULT
}
)
```

## Arguments

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Returns the lower level data access, locking, and latching statistics for each partition of a table

or index in a database.

database_id

| NULL | 0 | DEFAULT

ID of the database.

database_id. Valid inputs are the ID number of a database,

NULL, 0, or DEFAULT. The default is 0. NULL, 0, and DEFAULT are equivalent values in this

Specify NULL to return information for all databases in the instance of SQL Server. If you

specify NULL for

database_id

, you must also specify NULL for

partition_number

The built-in function

can be specified.

| NULL | 0 | DEFAULT

Object ID of the table or view the index is on.

Valid inputs are the ID number of a table and view, NULL, 0, or DEFAULT. The default is 0. NULL,

0, and DEFAULT are equivalent values in this context.

## Permissions

The values for each numeric column are set to zero whenever the metadata for the heap or B- tree is brought into the metadata cache. Statistics are accumulated until the cache object is removed from the metadata cache. An active heap or B-tree commonly has its metadata in the cache, and the cumulative counts reflects the activity since the Database Engine instance was last started. The metadata for a less active heap or B-tree might move in and out of the cache as it is used, particularly if the Database Engine instance is under memory pressure. As a result, index operational statistics might sometimes not be reflected in. This is not common. Statistics are removed from the cache and are no longer reported by this function if a table or index is dropped, or if a partition is truncated. Other DDL operations against the index might cause the value of the statistics to be reset to zero. You can use the Transact-SQL functions DB_ID and OBJECT_ID to specify a value for the database_id and object_id parameters. However, passing values that are not valid to these functions may cause unintended results. Always make sure that a valid ID is returned when you use or. For more information, see Return information for a specified table. Requires the following permissions: permission on the specified object within the database or permission to return information about all objects within the specified database, when a value for is not specified. or permission to return information about all databases, when a value for is not specified. Granting or allows all objects in the database to be returned, regardless of any permissions denied on specific objects. Denying or disallows all objects in the database to be returned, regardless of any permissions granted on specific objects. For more information, see Dynamic Management Views and Functions (Transact-SQL).

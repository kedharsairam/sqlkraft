---
name: "ASSEMBLYPROPERTY"
title: "ASSEMBLYPROPERTY"
category: "statements"
description: "Returns information about assembly properties."
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---
## Syntax

```sql
ASSEMBLYPROPERTY ( 'assembly_name' , 'property_name' )
```

## Return Type

sql_variant

## Property Descriptions

| Property | Return Type | Description |
|----------|-------------|-------------|
| CultureInfo | nvarchar | Name of the culture for the assembly. |
| PublicKey | varbinary | Public key of the assembly. |
| MvID | int | Assembly version ID. |
| VersionMajor | int | Major version number of the assembly. |
| VersionMinor | int | Minor version number of the assembly. |
| VersionBuild | int | Build version number of the assembly. |
| VersionRevision | int | Revision version number of the assembly. |

## Remarks

Returns information about assembly properties.

## Example

```sql
SELECT ASSEMBLYPROPERTY('database_name', 'CultureInfo') AS CultureInfo;
```

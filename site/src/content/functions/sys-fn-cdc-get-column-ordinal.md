---
name: 'sys.fn_cdc_get_column_ordinal'
title: 'sys.fn_cdc_get_column_ordinal'
category: 'change-data-capture'
description: 'Returns the column ordinal of the specified column as it appears in the associated with the specified capture instance. Transact-SQL syntax conventions Is the name of the capture instance in which the specified column is identified as a captured This function is used to identify the ordinal position of a captured column within the change data capture update mask. It is principally used in conjunct'
tags: ["change-data-capture", "function"]
pubDate: 2026-05-29
syntax: 'sys.fn_cdc_get_column_ordinal ( ''capture_instance'',''column_name'')'
---

## Description

Returns the column ordinal of the specified column as it appears in the associated with the specified capture instance. Transact-SQL syntax conventions Is the name of the capture instance in which the specified column is identified as a captured This function is used to identify the ordinal position of a captured column within the change data capture update mask. It is principally used in conjunction with the function

## Syntax

```sql
sys.fn_cdc_get_column_ordinal ( 'capture_instance','column_name')
```

## Permissions

SQL) Article • 08/10/2023 Applies to: SQL Server Returns the column ordinal of the specified column as it appears in the change table associated with the specified capture instance. Transact-SQL syntax conventions capture_instance Is the name of the capture instance in which the specified column is identified as a captured column. capture_instance is . column_name Is the column to report on. column_name is . This function is used to identify the ordinal position of a captured column within the change data capture update mask. It is principally used in conjunction with the function sys.fn_cdc_is_bit_set to extract information from the update mask when querying for change data.

---
name: "sys.fn_cdc_has_column_changed"
title: "sys.fn_cdc_has_column_changed"
category: "change-data-capture"
description: "Identifies whether the specified update mask indicates that the specified column has been updated in the associated change row. capture_instance Is the name of the capture instance. capture_instance Is the captured column of the specified capture instance to report on. Is the mask identifying updated columns in any associated change row."
tags: ["change-data-capture","function"]
pubDate: "2026-05-29"
syntax: "sys.fn_cdc_has_column_changed ( 'capture_instance','column_name' , update_mask )"
---

## Description

Identifies whether the specified update mask indicates that the specified column has been updated in the associated change row. capture_instance Is the name of the capture instance. capture_instance Is the captured column of the specified capture instance to report on. Is the mask identifying updated columns in any associated change row. You can use this function to extract information from an update mask returned in a query for change data.

## Syntax

```sql
sys.fn_cdc_has_column_changed ( 'capture_instance','column_name' , update_mask )
```

## Remarks

Identifies whether the specified update mask indicates that the specified column has been

updated in the associated change row.

capture_instance

Is the name of the capture instance.

capture_instance

column_name

Is the captured column of the specified capture instance to report on.

column_name

update_mask

Is the mask identifying updated columns in any associated change row.

update_mask

You can use this function to extract information from an update mask returned in a query for

change data. It is most useful in post-processing the update mask when you need to know

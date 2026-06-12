---
name: "Change the seed value"
title: "Change the seed value"
category: "statements"
description: "value."
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

increment

value. If a transaction inserts a row and is later rolled back, the next

row inserted uses

- the

current increment

value as if the row

had been deleted. If the table isn't empty, setting the identity value to a

number less than the maximum value in the identity column can result in one

of the following conditions:

- If a PRIMARY KEY or UNIQUE constraint exists on the identity column, error

message 2627 will be generated on later insert operations into the table

because the generated identity value will conflict with existing values.

- If a PRIMARY KEY or UNIQUE constraint doesn't exist, later insert operations

will result in duplicate identity values.

The following table lists conditions when

doesn't automatically reset the

current identity value, and provides methods for resetting the value.

The current identity value

is larger than the

maximum value in the

table.

Execute

to determine the current

maximum value in the column. Next, specify that value as the

new_reseed_value

in a

command.

or

Execute

with

set to a low value, and then run

to correct the value.

All rows are deleted from

the table.

Execute

with

set to the new starting value.

The seed value is the value inserted into an identity column for the first row loaded into the

table. All subsequent rows contain the current identity value plus the increment value where

current identity value is the last identity value generated for the table or view.

Expand table

### sysadmin

### db_owner

### db_ddladmin

### db_owner

`new_reseed_value`

```sql
DBCC CHECKIDENT
```

```sql
DBCC CHECKIDENT (<table_name>, NORESEED)
```

```sql
DBCC CHECKIDENT (<table_name>, RESEED,
<new_reseed_value>)
```

```sql
DBCC CHECKIDENT (<table_name>, RESEED,<new_reseed_value>)
```

`new_reseed_value`

```sql
DBCC CHECKIDENT (<table_name>, RESEED)
```

```sql
DBCC CHECKIDENT (<table_name>, RESEED, <new_reseed_value>)
```

`new_reseed_value`

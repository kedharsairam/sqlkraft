---
name: "sys.sp_bindrule"
title: "sp_bindrule"
category: "general"
description: "condition_expression Is the condition or conditions that define the rule. A rule can be any expression valid in a WHERE clause and can include elements such as arithmetic operators, relational operators, and predicates (for example, IN, LIKE, BETWEEN). A rule cannot reference columns or other database objects. Built-in functions that do not reference database objects can be included. User-defined "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_bindrule
  [ @rulename = ]
  N
  'rulename'
  , [ @objname = ]
  N
  'objname'
  [ , [ @futureonly = ]
  'futureonly'
  ]
  [ ; ]
---

## Description

condition_expression Is the condition or conditions that define the rule. A rule can be any expression valid in a WHERE clause and can include elements such as arithmetic operators, relational operators, and predicates (for example, IN, LIKE, BETWEEN). A rule cannot reference columns or other database objects. Built-in functions that do not reference database objects can be included. User-defined functions cannot be used. condition_expression includes one variable. The at sign ( ) precedes each local variable. The expression refers to the value entered with the UPDATE or INSERT statement. Any name or symbol can be used to represent the value when creating the rule, but the first character must be the at sign ( CREATE RULE cannot be combined with other Transact-SQL statements in a single batch. Rules Deprecated feature

## Syntax

```sql
sp_bindrule
[ @rulename = ]
N
'rulename'
, [ @objname = ]
N
'objname'
[ , [ @futureonly = ]
'futureonly'
]
[ ; ]
```

## Remarks

condition_expression

Is the condition or conditions that define the rule. A rule can be any expression valid in a

WHERE clause and can include elements such as arithmetic operators, relational operators, and

predicates (for example, IN, LIKE, BETWEEN). A rule cannot reference columns or other

database objects. Built-in functions that do not reference database objects can be included.

User-defined functions cannot be used.

condition_expression

includes one variable. The at sign (

) precedes each local variable. The

expression refers to the value entered with the UPDATE or INSERT statement. Any name or

symbol can be used to represent the value when creating the rule, but the first character must

be the at sign (

CREATE RULE cannot be combined with other Transact-SQL statements in a single batch. Rules

do not apply to data already existing in the database at the time the rules are created, and

rules cannot be bound to system data types.

A rule can be created only in the current database. After you create a rule, execute

to bind the rule to a column or to alias data type. A rule must be compatible with the column

data type. For example, "@value LIKE A%" cannot be used as a rule for a numeric column. A

rule cannot be bound to a

, CLR user-defined type, or

column. A rule cannot be bound to a computed

Enclose character and date constants with single quotation marks (') and precede binary

constants with 0x. If the rule is not compatible with the column to which it is bound, the SQL

Server Database Engine returns an error message when a value is inserted, but not when the

rule is bound.

A rule bound to an alias data type is activated only when you try to insert a value into, or to

update, a database column of the alias data type. Because rules do not test variables, do not

assign a value to an alias data type variable that would be rejected by a rule that is bound to a

column of the same data type.

Avoid creating rules on expressions that use alias data types. Although rules can be

created on expressions that use alias data types, after binding the rules to columns or alias

data types, the expressions fail to compile when referenced.

Deprecated feature

Replacement

Feature name

CREATE_DROP_RULE

Use MARS or distributed transactions.

Use MARS or distributed transactions.

DBCC DBREINDEX

DBCC DBREINDEX

DBCC INDEXDEFRAG

DBCC INDEXDEFRAG

DBCC SHOWCONTIG

DBCC SHOWCONTIG

DBCC PINTABLE

DBCC UNPINTABLE

Has no effect.

DBCC [UN]PINTABLE

Level0type = 'type' and Level0type = 'USER' to add extended properties to

level-1 or level-2 type objects.

Use Level0type = 'USER' only to add an

extended property directly to a user or role.

Use Level0type = '

' to add an extended

property to level-1 types such as

VIEW, or level-2 types such as COLUMN or

TRIGGER. For more information, see

sp_addextendedproperty

EXTPROP_LEVEL0

EXTPROP_LEVEL0USER

programming

srv_convert

srv_describe

srv_getbindtoken

srv_got_attention

srv_message_handler

srv_paramdata

srv_paraminfo

srv_paramlen

srv_parammaxlen

srv_paramname

srv_paramnumber

srv_paramset

Use CLR Integration instead.

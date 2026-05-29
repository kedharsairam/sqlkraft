---
title: sys.dm_sql_referencing_entities
name: sys.dm_sql_referencing_entities
category: execution
description:
pubDate: 2026-05-29
---

Transact-SQL database-level DDL trigger

Yes

No

Transact-SQL server-level DDL trigger

Yes

No

Extended stored procedures

No

Yes

Queue

No

Yes

Synonym

No

Yes

Type (alias and CLR user-defined type)

No

Yes

XML schema collection

No

Yes

Partition function

No

Yes

- A table is tracked as a referencing entity only when it references a Transact-SQL module,

user-defined type, or XML schema collection in the definition of a computed column, CHECK

constraint, or DEFAULT constraint.

\*\* Numbered stored procedures with an integer value greater than 1 are not tracked as either a

referencing or referenced entity.

Requires CONTROL permission on the referenced object. When the referenced entity is a

partition function, CONTROL permission on the database is required.

Requires SELECT permission on sys.dm_sql_referencing_entities. By default, SELECT

permission is granted to public.

Requires no permissions on the referenced object. Partial results can be returned if the

user has VIEW DEFINITION on only some of the referencing entities.

Requires VIEW DEFINITION on the object when the referencing entity is an object.

Requires VIEW DEFINITION on the database when the referencing entity is a database-

level DDL trigger.

---
name: "Countersignatures"
title: "Countersignatures"
category: "statements"
description: "When you execute a signed module, the signatures are temporarily added to the SQL token,"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

When you execute a signed module, the signatures are temporarily added to the SQL token,

but the signatures are lost if the module executes another module, or if the module terminates

execution. A

countersignature

is a special form of signature. By itself, a countersignature

doesn't grant any permissions. However, it allows signatures made by the same certificate or

asymmetric key to be kept for the duration of the call made to the countersigned object.

For example, assume that user

calls procedure

, which calls procedure

, which selects from table

. Alice has

permission on

, but

doesn't have

## permissions on

or

permission on

, and no

ownership chaining is involved in this entire chain. Alice can't access table

, either directly, or

by using

and

. Since we want Alice to always use

for

access, we don't want to grant her permission to execute

. How can we

accomplish this scenario?

If we sign

, such that

can access

, then Alice can invoke

directly and she doesn't have to call

.

We could deny

permission on

to Alice, but then Alice can't call

through

.

Signing

wouldn't work by itself, because the signature is lost in the call to

.

However, by countersigning

with the same certificate used to sign

,

the signature is kept across the call chain and is allowed access to

. If Alice attempts to call

directly, she can't access

, because the countersignature doesn't grant any

rights.

Example C

shows the Transact-SQL for this example.

When you recreate a procedure for signature, all the statements in the original batch must

match the recreated batch. If any portion of the batch differs, even in spaces or comments,

the resultant signature is different.

`Alice`

`ProcForAlice`

`ProcSelectT1`

`T1`

`EXECUTE`

`ProcForAlice`

`EXECUTE`

`ProcSelectT1`

`SELECT`

`T1`

`T1`

`ProcForAlice`

`ProcSelectT1`

`ProcForAlice`

`ProcSelectT1`

`ProcSelectT1`

`ProcSelectT1`

`T1`

`ProcSelectT1`

`ProcForAlice`

`EXECUTE`

`ProcSelectT1`

`ProcSelectT1`

`ProcForAlice`

`ProcForAlice`

`ProcSelectT1`

`ProcSelectT1`

`ProcForAlice`

`T1`

`ProcSelectT1`

`T1`

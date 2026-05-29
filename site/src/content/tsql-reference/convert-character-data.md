---
name: 'Convert character data'
title: 'Convert character data'
category: 'statements'
description: 'For information about converting character data, see'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

For information about converting character data, see

char and varchar

. For more information

about converting between data types, see

CAST and CONVERT

.

ALTER TABLE (Transact-SQL)

CAST and CONVERT (Transact-SQL)

COLLATE (Transact-SQL)

CREATE TABLE (Transact-SQL)

Data types (Transact-SQL)

DECLARE @local_variable (Transact-SQL)

LIKE (Transact-SQL)

SET ANSI_PADDING (Transact-SQL)

SET @local_variable (Transact-SQL)

Collation and Unicode Support

Single-Byte and Multibyte Character Sets

Last updated on 11/18/2025

Each non-null

or

column requires 24 bytes of additional fixed

allocation, which counts against the 8,060-byte row limit during a sort operation. These

additional bytes can create an implicit limit to the number of non-null

or

columns in a table. No special error is provided when the table is created

(beyond the usual warning that the maximum row size exceeds the allowed maximum of

8,060 bytes) or at the time of data insertion. This large row size can cause errors (such as

error 512) that users might not anticipate during some normal operations. Two examples

of operations are a clustered index key update, or sorts of the full column set.

Related content

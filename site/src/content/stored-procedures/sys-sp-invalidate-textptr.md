---
name: "sys.sp_invalidate_textptr"
title: "sp_invalidate_textptr"
category: "general"
description: "Invalidates the specified in-row text pointer, or all in-row text pointers, in the transaction."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "sp_invalidate_textptr"
---

## Description

Invalidates the specified in-row text pointer, or all in-row text pointers, in the transaction.

## Syntax

`sp_invalidate_textptr`

## Remarks

Invalidates the specified in-row text pointer, or all in-row text pointers, in the transaction.

can be used only on in-row text pointers. These pointers are from

tables that have the

option enabled.

The in-row text pointer that to be invalidated.

@TextPtrValue

, with a default of

invalidates all in-row text pointers in the transaction.

(success) or

allows for a maximum of 1,024 active valid in-row text pointers per transaction per

database. However, a transaction spanning more than one database can have 1,024 in-row text

pointers in each database.

can be used to invalidate in-row text

pointers and, therefore, free space for more in-row text pointers.

For more information about the text in row option, see

sp_tableoption

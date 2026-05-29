---
name: "Regular expressions functions (Transact-"
title: "Regular expressions functions (Transact-"
category: "statements"
description: "SQL Server 2025 (17.x)"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

#### Function

### 2025

### Always-up-to-date

### update policy

SQL)

Applies to:

SQL Server 2025 (17.x)

Azure SQL Database

Azure SQL Managed

Instance

SQL database in Microsoft Fabric

Use the functions described in this article to match complex patterns and manipulate data in

SQL Server with regular expressions.

## Description

REGEXP_LIKE

## Returns a Boolean value that indicates whether the text input matches the

regex pattern.

REGEXP_REPLACE

## Returns a modified source string replaced by a replacement string, where

occurrence of the regex pattern found.

REGEXP_SUBSTR

Extracts parts of a string based on a regular expression pattern.

## Returns Nth occurrence of a substring that matches the regex pattern.

REGEXP_INSTR

## Returns the starting or ending position of the matched substring, depending

on the option supplied.

REGEXP_COUNT

## Returns a count of the number of times that regex pattern occurs in a string.

REGEXP_MATCHES

## Returns a table of captured substring(s) that match a regular expression

pattern to a string. If no match is found, the function returns no row.

REGEXP_SPLIT_TO_TABLE

## Returns a table of strings split, delimited by the regex pattern. If there's no

match to the pattern, the function returns the string.

Regular expressions

７

Note

Regular expressions are available in Azure SQL Managed Instance with the

SQL Server

or

.

ﾉ

Expand table

Related content

Last updated on 11/18/2025

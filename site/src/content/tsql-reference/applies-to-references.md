---
name: '"Applies to" references'
title: '"Applies to" references'
category: "statements"
description: "Most code examples in the Transact-SQL reference were tested on servers that are running a"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Most code examples in the Transact-SQL reference were tested on servers that are running a

case-sensitive sort order. The test servers were typically running the ANSI/ISO 1252 code page.

Many code examples prefix Unicode character string constants with the letter

. Without the

prefix, the string is converted to the default code page of the database. This default code page

might not recognize certain characters.

The Transact-SQL reference articles encompass multiple versions of SQL Server, starting with

SQL Server 2008 (10.0.x), as well as Azure SQL Database, Azure SQL Managed Instance, Azure

Synapse Analytics, and Analytics Platform System (PDW).

A section near the top of each article indicates which products support the article's subject. If a

product is omitted, then the feature described by the article isn't available in that product.

The general subject of the article might be used in a product, but all of the arguments aren't

supported in some cases. For example, contained database users were introduced in SQL

Server 2012 (11.x). Use the

statement in any SQL Server product; however the

## syntax can't be used with older versions. Extra

sections are inserted

into the appropriate argument descriptions in the body of the article.

Transact-SQL reference (Database Engine)

Reserved Keywords (Transact-SQL)

Last updated on 11/18/2025

Related content

```sql
ANSI_WARNINGS
CONCAT_NULL_YIELDS_NULL
QUOTED_IDENTIFIER
```

```sql
N
```

```sql
N
```

```sql
CREATE USER
```

```sql
WITH PASSWORD
```

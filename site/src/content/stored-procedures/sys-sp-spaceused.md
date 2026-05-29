---
name: 'sys.sp_spaceused'
title: 'sp_spaceused'
category: 'general'
description: 'Analytics Platform System (PDW) system stored procedure displays either: the number of rows, disk space reserved, and disk space used by a table, indexed view, or Service Broker queue in the current database the disk space reserved and used by the whole database Transact-SQL syntax conventions For Azure Synapse Analytics and Analytics Platform System (PDW), upon the ordinal position of parameters.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_spaceused (@objname= N''Table1'');'
---

## Description

Analytics Platform System (PDW) system stored procedure displays either: the number of rows, disk space reserved, and disk space used by a table, indexed view, or Service Broker queue in the current database the disk space reserved and used by the whole database Transact-SQL syntax conventions For Azure Synapse Analytics and Analytics Platform System (PDW), upon the ordinal position of parameters. The qualified or nonqualified name of the table, indexed view, or queue for which space usage

## Syntax

```sql
sp_spaceused (@objname= N'Table1');
```

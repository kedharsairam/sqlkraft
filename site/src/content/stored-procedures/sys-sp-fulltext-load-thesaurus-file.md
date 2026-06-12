---
name: "sys.sp_fulltext_load_thesaurus_file"
title: "sp_fulltext_load_thesaurus_file"
category: "general"
description: "Causes the server instance to parse and load the data from the thesaurus file that corresponds to the language whose LCID is specified. This stored procedure is useful after updating a causes recompilation of full-text queries that use the thesaurus of the specified LCID. Integer mapping the locale identifier (LCID) of the language for which you want to load the , w"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "sp_fulltext_load_thesaurus_file"
---

## Description

Causes the server instance to parse and load the data from the thesaurus file that corresponds to the language whose LCID is specified. This stored procedure is useful after updating a causes recompilation of full-text queries that use the thesaurus of the specified LCID. Integer mapping the locale identifier (LCID) of the language for which you want to load the , with no default.

## Syntax

`sp_fulltext_load_thesaurus_file`

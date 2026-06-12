---
name: "sys.numbered_procedure_parameters"
title: "sys.numbered_procedure_parameters"
category: "compatibility"
description: "Contains one row for each parameter of a numbered procedure. When you create a numbered stored procedure, the base procedure is number 1. All subsequent procedures have numbers 2, contains the parameter definitions for all subsequent procedures, numbered 2 and greater. This view does not show parameters for the base stored procedure (number = 1). The base stored procedure is similar to a nonnumber"
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
syntax: |
  sys.numbered_procedures
      sys.numbered_procedure_parameters
---

## Description

Contains one row for each parameter of a numbered procedure. When you create a numbered stored procedure, the base procedure is number 1. All subsequent procedures have numbers 2, contains the parameter definitions for all subsequent procedures, numbered 2 and greater. This view does not show parameters for the base stored procedure (number = 1). The base stored procedure is similar to a nonnumbered

## Syntax

```sql
sys.numbered_procedures sys.numbered_procedure_parameters
```

---
name: "sys.fn_validate_plan_guide"
title: "sys.fn_validate_plan_guide"
category: "date-time"
description: "Verifies the validity of the specified plan guide. The returns the first error message that is encountered when the plan guide is applied to its query. An empty rowset is returned when the plan guide is valid. Plan guides can become invalid after changes are made to the physical design of the database. For example, if a plan guide specifies a particular index and that index is subsequently dropped"
tags: ["date-time", "function"]
pubDate: 2026-05-29
syntax: "sys.fn_validate_plan_guide"
---

## Description

Verifies the validity of the specified plan guide. The returns the first error message that is encountered when the plan guide is applied to its query. An empty rowset is returned when the plan guide is valid. Plan guides can become invalid after changes are made to the physical design of the database.

## Syntax

`sys.fn_validate_plan_guide`

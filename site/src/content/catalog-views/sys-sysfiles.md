---
name: "sys.sysfiles"
title: "sys.sysfiles"
category: "databases-files"
description: "Contains one row for each file in a database. File identification number unique for each database. File group identification number. Size of the file, in 8-KB pages. Maximum file size, in 8-KB pages. -1 = File will grow until the disk is full. 268435456 = Log file will grow to a maximum size of 2 TB. Note: Databases that are upgraded with an unlimited log file size will report -1 for the maximum s"
tags: ["databases-files","catalog-view"]
pubDate: "2026-05-29"
---

## Description

Contains one row for each file in a database. File identification number unique for each database. File group identification number. Size of the file, in 8-KB pages. Maximum file size, in 8-KB pages. -1 = File will grow until the disk is full. 268435456 = Log file will grow to a maximum size of 2 TB. Note: Databases that are upgraded with an unlimited log file size will report -1 for the maximum size of the log file.

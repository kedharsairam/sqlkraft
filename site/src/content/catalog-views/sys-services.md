---
name: 'sys.services'
title: 'sys.services'
category: 'objects'
description: 'This catalog view contains a row for each service in the database.'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server

This catalog view contains a row for each service in the database.


## Description
Case-sensitive name of service, unique within the database. Not

NULLABLE.

Identifier of the service. Not NULLABLE.

Identifier for the database principal that owns this service. NULLABLE.

Object id for the queue that this service uses. Not NULLABLE.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

ﾉ

Expand table

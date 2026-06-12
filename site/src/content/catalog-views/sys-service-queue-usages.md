---
name: "sys.service_queue_usages"
title: "sys.service_queue_usages"
category: "compatibility"
description: "This catalog view returns a row for each reference between service and service queue. A service can only be associated with one queue. A queue can be associated with multiple services."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

This catalog view returns a row for each reference between service and service queue. A service can only be associated with one queue. A queue can be associated with multiple services.

## Permissions

Article • 02/28/2023 A service can only be associated with one queue. A queue can be associated with multiple services. Description Identifier of the service. Unique within the database. Not NULLABLE. Identifier of the service queue used by the service. Not NULLABLE. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. sys.services (Transact-SQL) ﾉ Expand table See Also

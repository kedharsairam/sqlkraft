---
name: "sys.sp_deletepeerrequesthistory"
title: "sp_deletepeerrequesthistory"
category: "general"
description: "Deletes history related to a publication status request, which includes the request history ) as well as the response history ( executed on the publication database at a Publisher participating in a Peer-to-Peer replication topology. For more information, see Peer-to-Peer - Transactional Replication Name of the publication for which the status request was made. Spec"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_deletepeerrequesthistory
  [ @publication = ]
  N
  'publication'
  [ , [ @request_id = ] request_id ]
  [ , [ @cutoff_date = ] cutoff_date ]
  [ ; ]
---

## Description

Deletes history related to a publication status request, which includes the request history ) as well as the response history ( executed on the publication database at a Publisher participating in a Peer-to-Peer replication topology. For more information, see Peer-to-Peer - Transactional Replication Name of the publication for which the status request was made. Specifies an individual status request so that all responses to this request will be deleted.

## Syntax

```sql
sp_deletepeerrequesthistory
[ @publication = ]
N
'publication'
[ , [ @request_id = ] request_id ]
[ , [ @cutoff_date = ] cutoff_date ]
[ ; ]
```

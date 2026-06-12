---
name: "sys.sp_redirect_publisher"
title: "sp_redirect_publisher"
category: "general"
description: "Specifies a redirected publisher for an existing publisher/database pair. If the publisher database belongs to an Always On availability group (AG), the redirected publisher is the AG listener name associated with the AG."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_redirect_publisher
  [ @original_publisher = ]
  N
  'original_publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  [ , [ @redirected_publisher = ]
  N
  'redirected_publisher'
  ]
  [ ; ]
---

## Description

Specifies a redirected publisher for an existing publisher/database pair. If the publisher database belongs to an Always On availability group (AG), the redirected publisher is the AG listener name associated with the AG.

## Syntax

```sql
sp_redirect_publisher
[ @original_publisher = ]
N
'original_publisher'
, [ @publisher_db = ]
N
'publisher_db'
[ , [ @redirected_publisher = ]
N
'redirected_publisher'
]
[ ; ]
```

## Permissions

The target of redirection when was called for the original publisher/published database pair. @redirected_publisher is an OUTPUT parameter of type , with no default. (success) or (failure). None. If no entry exists for the publisher and the publishing database, returns null for the output parameter @redirected_publisher. Otherwise, the associated redirected publisher is returned, both on success and failure. If the validation succeeds, returns a success indication. If the validation fails, appropriate errors are raised. makes a best effort to raise all issues and not just the first encountered. fails with the following error when validating secondary replica hosts that don't allow read access, or require read intent to be specified. Msg 21899, Level 11, State 1, Procedure , Line 109 The query at the redirected publisher 'MyReplicaHostName' to determine whether there were sysserver entries for the subscribers of the original publisher 'MyOriginalPublisher' failed with error '976', error message 'Error 976, Level 14, State 1, Message: The target database, 'MyPublishedDB', is participating in an availability group and is currently not accessible for queries. Either data movement is suspended or the availability replica isn't enabled for read access. To allow read-only access to this and other databases in the availability group, enable read access to one or more secondary availability replicas in the group. For more information, see the ALTER AVAILABILITY GROUP statement in SQL Server Books Online.

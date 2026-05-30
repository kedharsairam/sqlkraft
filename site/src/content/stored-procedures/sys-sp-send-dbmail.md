---
name: "sys.sp_send_dbmail"
title: "sp_send_dbmail"
category: "general"
description: "Sends an e-mail message to the specified recipients. The message might include a query result set, file attachments, or both. When mail is successfully placed in the Database Mail queue, of the message. This stored procedure is in the Transact-SQL syntax conventions"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_send_dbmail [ [ @profile_name = ]
  'profile_name'
  ]
  [ , [ @recipients = ]
  'recipients [ ; ...n ]'
  ]
  [ , [ @copy_recipients = ]
  'copy_recipient [ ; ...n ]'
  ]
  [ , [ @blind_copy_recipients = ]
  'blind_copy_recipient [ ; ...n ]'
  ]
  [ , [ @from_address = ]
  'from_address'
  ]
  [ , [ @reply_to = ]
  'reply_to'
  ]
  [ , [ @subject = ]
  N
  'subject'
  ]
  [ , [ @body = ]
  N
  'body'
  ]
  [ , [ @body_format = ]
  'body_format'
  ]
  [ , [ @importance = ]
  'importance'
  ]
  [ , [ @sensitivity = ]
  'sensitivity'
  ]
  [ , [ @file_attachments = ]
  N
  'attachment [ ; ...n ]'
  ]
  [ , [ @query = ]
  N
  'query'
  ]
  [ , [ @execute_query_database = ]
  'execute_query_database'
  ]
  [ , [ @attach_query_result_as_file = ] attach_query_result_as_file ]
  [ , [ @query_attachment_filename = ]
  N
  'query_attachment_filename'
  ]
  [ , [ @query_result_header = ] query_result_header ]
  [ , [ @query_result_width = ] query_result_width ]
  [ , [ @query_result_separator = ]
  'query_result_separator'
  ]
  [ , [ @exclude_query_output = ] exclude_query_output ]
  [ , [ @append_query_error = ] append_query_error ]
  [ , [ @query_no_truncate = ] query_no_truncate ]
  [ , [ @query_result_no_padding = ] @query_result_no_padding ]
  [ , [ @mailitem_id = ] mailitem_id ] [
  OUTPUT
  ]
  [ ; ]
---

## Description

Sends an e-mail message to the specified recipients. The message might include a query result set, file attachments, or both. When mail is successfully placed in the Database Mail queue, of the message. This stored procedure is in the Transact-SQL syntax conventions

## Syntax

```sql
sp_send_dbmail [ [ @profile_name = ]
'profile_name'
]
[ , [ @recipients = ]
'recipients [ ; ...n ]'
]
[ , [ @copy_recipients = ]
'copy_recipient [ ; ...n ]'
]
[ , [ @blind_copy_recipients = ]
'blind_copy_recipient [ ; ...n ]'
]
[ , [ @from_address = ]
'from_address'
]
[ , [ @reply_to = ]
'reply_to'
]
[ , [ @subject = ]
N
'subject'
]
[ , [ @body = ]
N
'body'
]
[ , [ @body_format = ]
'body_format'
]
[ , [ @importance = ]
'importance'
]
[ , [ @sensitivity = ]
'sensitivity'
]
[ , [ @file_attachments = ]
N
'attachment [ ; ...n ]'
]
[ , [ @query = ]
N
'query'
]
[ , [ @execute_query_database = ]
'execute_query_database'
]
[ , [ @attach_query_result_as_file = ] attach_query_result_as_file ]
[ , [ @query_attachment_filename = ]
N
'query_attachment_filename'
]
[ , [ @query_result_header = ] query_result_header ]
[ , [ @query_result_width = ] query_result_width ]
[ , [ @query_result_separator = ]
'query_result_separator'
]
[ , [ @exclude_query_output = ] exclude_query_output ]
[ , [ @append_query_error = ] append_query_error ]
[ , [ @query_no_truncate = ] query_no_truncate ]
[ , [ @query_result_no_padding = ] @query_result_no_padding ]
[ , [ @mailitem_id = ] mailitem_id ] [
OUTPUT
]
[ ; ]
```

## Permissions

for messages related to that . When an error is returned from , the e-mail is not submitted to the Database Mail system and the error is not displayed in this view. When individual account delivery attempts fail, Database Mail holds the error messages during retry attempts until the mail item delivery either succeeds or fails. In case of ultimate success, all of the accumulated errors get logged as separate warnings including the . This can cause warnings to appear, even though the e-mail was sent. In case of ultimate delivery failure, all previous warnings get logged as one error message without an , since all accounts have failed. You must be a member of the fixed server role or the database role to access this view. Members of who are not members of the role, can only see the events for e-mails that they submit. sysmail_faileditems (Transact-SQL) Database Mail External Program See Also

## Examples

### Example 1

`msdb`

### Example 2

`sp_send_dbmail`

### Example 3

`sp_send_dbmail`

### Example 4

`sysmail_delete_profile_sp`

### Example 5

`msdb`

### Example 6

`msdb`

### Example 7

`EXECUTE`

### Example 8

```sql
AdventureWorks Administrator
```

### Example 9

```sql
EXECUTE msdb.dbo.sysmail_delete_profile_sp @profile_name =
'AdventureWorks
Administrator'
;
```

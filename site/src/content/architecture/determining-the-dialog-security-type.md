---
title: "Determining the Dialog Security Type"
topic: "service-broker"
description: "09/11/2025 The type of dialog security that's used for a conversation depends on the options in the statement, the settings on the remote service"
tags: ["service-broker","determining-the-dialog-security-type"]
pubDate: "2025-12-01"
---

The type of dialog security that's used for a conversation depends on the options in the

statement, the settings on the remote service binding for the service, and

whether the owner of the initiating service owns a certificate. For each new dialog, SQL Server

looks up the remote service binding for the target service in the

catalog view.

The following table lists the type of dialog security for each valid combination. If a remote

service binding exists, the dialog uses encryption regardless of the settings on the

statement.

Service owner has a

certificate

Dialog fails

Anonymous security

Full security

Service owner has a

certificate

No dialog

security

Anonymous security

Full security

Service owner

doesn't have a

certificate

Dialog fails

Anonymous security

Dialog fails

Service owner

doesn't have a

certificate

No dialog

security

Anonymous security

Dialog fails

doesn't have the information required to provide the requested security.

Service Broker ends the conversation and puts an error message on the queue for the

initiating service.

doesn't provide dialog security for the dialog. Operations on behalf of the

initiating service run as

in the target database. Messages aren't encrypted for this

ﾉ

Expand table

```sql
BEGIN
DIALOG CONVERSATION sys.remote_service_bindings
BEGIN
DIALOG CONVERSATION
ANONYMOUS = ON
ANONYMOUS = OFF
ENCRYPTION =
ON
ENCRYPTION =
OFF
ENCRYPTION =
ON
ENCRYPTION =
OFF
```

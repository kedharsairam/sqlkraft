---
title: "Certificates for Dialog Security"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  When a conversation begins, Service Broker uses remote service bindings to locate the

  certificate to use for the conversation. This to
tags:
  - "service-broker"
  - "certificates-for-dialog-security"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

When a conversation begins, Service Broker uses remote service bindings to locate the

certificate to use for the conversation. This topic describes how Service Broker determines the

certificate to use for a conversation.

Service Broker first locates a remote service binding for the conversation, then selects a

certificate owned by the user specified in the binding.

To find a binding, Service Broker checks the database for a binding that specifies the target

service name for the conversation.

To select a certificate, Service Broker finds the certificate with the latest expiration date that's

owned by the user specified in the remote service binding. Service Broker doesn't consider

certificates that aren't yet valid, that have expired, or that aren't marked as available for begin

dialog. For more information on certificates, see

CREATE CERTIFICATE

.

If no remote service binding exists or the user for the remote service binding doesn't own a

valid certificate that's available for begin dialog, Service Broker can't encrypt messages for the

conversation. If there's no binding and the database contains a Broker Configuration Service,

Service Broker requests a binding through that service. If there's no Broker Configuration

Service in the database or the Broker Configuration Service doesn't provide a remote service

binding, the conversation is delayed if encryption is

, or continues without encryption if

encryption is

. For more information, see

Determine the dialog security type

.

Service Broker dialog security uses certificates for remote authorization. When a dialog uses

dialog security, the first message sent by each participant in the conversation contains header

information encrypted with the private key of the sending user, and header information

encrypted with the public key of the receiving user. The content of the message is encrypted

with a session key. The session key itself is encrypted, and can only be recovered using the

private key for the receiving user.

If the message recipient can successfully decrypt the message, this means that the recipient

possesses the corresponding keys, and this confirms the identity of each participant in the

```sql
ON
OFF
```

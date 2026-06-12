---
title: "Managing Security (Service Broker)"
topic: "service-broker"
description: |
  09/11/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Service Broker provides a flexible security framework for helping you secure your applications.

  This topic explains considerations for
tags:
  - "service-broker"
  - "managing-security-service-broker"
pubDate: 2025-12-01
---

09/11/2025

SQL Server

Azure SQL Managed Instance

Service Broker provides a flexible security framework for helping you secure your applications.

This topic explains considerations for managing Service Broker security.

Each application has unique security requirements. Part of managing security is to carefully

plan the requirements for your application. Transport security, dialog security, and the security

infrastructure built into SQL Server work together to help you secure your application.

All applications use the security infrastructure built into SQL Server. Each operation in SQL

Server occurs in a specific security context. In most cases, you create SQL Server database

principals specifically for the application. This helps you to ensure that each step in the

application runs in a security context with only the privileges necessary for that step. For

example, the principal that you specify for internal activation needs execute permissions on the

stored procedure that Service Broker activates. The stored procedure itself might impersonate

a user that has

permission for the queue and

permission for a particular table.

You design your application so that, at each stage, the security context for the application

doesn't have permission to perform unexpected operations.

Applications that send messages between SQL Server instances can use transport security,

dialog security, or both. Transport security and dialog security provide distinctly different

protections.

Service Broker dialog security provides end-to-end encryption and authorization for

conversations between specific services. Therefore, dialog security helps protect data against

inspection or modification in transit. Applications that transmit confidential or sensitive data, or

that transmit messages over untrusted networks, should use dialog security. Dialog security

can help a participant in the conversation identify the other participant in the conversation.

Because dialog security applies to specific services, you must configure dialog security for each

service that uses dialog security. However, an instance might use dialog security for some

conversations and allow other conversations to be transmitted unencrypted. For example,

conversations to a service that updates customer information might use dialog security,

whereas conversations that simply look up part number information might not require dialog

security.

```sql
RECEIVE
UPDATE
```

---
title: "Security Overview (Service Broker)"
topic: "service-broker"
description: |
  08/29/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Service Broker helps you write highly scalable database applications that are also secure and

  reliable. Service Broker security allows
tags:
  - "service-broker"
  - "security-overview-service-broker"
pubDate: 2025-12-01
---

08/29/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Service Broker helps you write highly scalable database applications that are also secure and

reliable. Service Broker security allows services hosted by different SQL Server instances to

communicate securely, even where the instances are on different computers that have no other

trust relationship or where the source and destination computers aren't connected to the same

network at the same time.

Service Broker security relies on certificates. The general approach is to use certificates to

establish the credentials of a remote database, and then to map operations from the remote

database to a local user. The permissions for the local user apply to any operation on behalf of

the remote service. The certificate is shared between databases. No other information for the

user is shared.

Service Broker provides two distinct types of security - dialog security and transport security.

Understanding these two types of security, and how they work together, helps you to design,

deploy, and administer Service Broker applications.

- Encrypts messages in an individual dialog conversation and verifies the

identities of participants in the dialog. Dialog security also provides remote authorization

and message integrity checking. Dialog security establishes authenticated and encrypted

communication between two services.

- Prevents unauthorized databases from sending Service Broker

messages to databases in the local instance. Transport security establishes an

authenticated network connection between two databases.

The dialog protocol and the adjacent broker protocol are designed around passing messages

between databases, rather than executing commands on a remote database. This style of

communication allows Service Broker to provide services without requiring databases to share

SQL Server logins or Windows security credentials.

For more information on certificates, see

CREATE CERTIFICATE

.

７

Note

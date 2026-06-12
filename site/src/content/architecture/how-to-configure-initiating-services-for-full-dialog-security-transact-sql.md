---
title: "How to: Configure Initiating Services for Full Dialog Security (Transact-SQL)"
topic: "service-broker"
description: ""
tags: ["service-broker","how-to-configure-initiating-services-for-full-dialog-security-transact-sql"]
pubDate: 2025-12-01
---

uses dialog security for any conversation to a service for which a remote service

binding exists in the database that hosts the initiating service. If the database that hosts the

target service contains a user that corresponds to the user that created the dialog, and the

remote service binding doesn't specify anonymous security, then the dialog uses full security.

To make sure that an initiating service uses dialog security, you create a remote service binding

for the service. For SQL Server to use full security, the remote service binding must not specify

anonymous security, and the target database must be configured to use full security for this

service.

1. Obtain a certificate for the owner of the target service in the remote database from a

trusted source. Typically, this step involves sending the certificate using encrypted email,

or transferring the certificate on physical media such as a USB drive.

The certificate must be encrypted with the database master key (DMK). For more

information, see

CREATE MASTER KEY.

2. Create a user without a login for the remote service.

3. Install the certificate for the remote service user. The user created in the previous step

owns the certificate.

4. Create a remote service binding that specifies the remote service user and the service.

5. Create a user without a sign in to own the local service.

6. Create a certificate for the local service. The user created in the previous step owns the

certificate.

７

Note

Only install certificates from trusted sources.

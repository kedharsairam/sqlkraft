---
title: "Service Accounts"
topic: "high-availability"
description: |
  Article
  
  •
  
  02/01/2024
  
  Applies to:
  
  SQL Server
  
  When using Windows Authentication, if the server instances use different accounts, specify the
  
  service accounts for SQL Server. These service accounts
tags:
  - "high-availability"
  - "service-accounts"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

When using Windows Authentication, if the server instances use different accounts, specify the

service accounts for SQL Server. These service accounts must all be domain accounts (in the

same or trusted domains).

If all the server instances use the same domain account or use certificate-based authentication,

leave the fields blank. Simply click

, and the wizard automatically configures the accounts

based on the account of the current wizard.

Establish a Database Mirroring Session Using Windows Authentication (SQL Server

Management Studio)

Start the Configuring Database Mirroring Security Wizard (SQL Server Management

Studio)

Specify the service account of the principal server instance. Enter the domain name in upper

case:

DOMAINNAME

\

username

Specify the service account of the mirror server instance. Enter the domain name in upper case:

DOMAINNAME

\

username

Specify the service account of the witness server instance. Enter the domain name in upper

）

Important

If the database mirroring endpoints of the server instances are configured to use

certificates, you must leave the service account fields empty.
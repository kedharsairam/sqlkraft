---
name: 'sys.partition_schemes'
title: 'sys.partition_schemes'
category: 'partitions'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "partitions"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Managed Instance

Contains one row for each message sent by Database Mail. Use

when you

want to see which messages were successfully sent.

To see all messages processed by Database Mail, use

sysmail_allitems (Transact-SQL)

. To see

only messages with the failed status, use

sysmail_faileditems (Transact-SQL)

. To see only unsent

or retrying messages, use

sysmail_unsentitems (Transact-SQL)

. To see e-mail attachments, use

sysmail_mailattachments (Transact-SQL)

.


## Description
Identifier of the mail item in the mail queue.

The identifier of the profile used to send the message.

The e-mail addresses of the message recipients.

The e-mail addresses of those who receive copies of the

message.

The e-mail addresses of those who receive copies of the

message but whose names do not appear in the message

header.

The subject line of the message.

The body of the message.

The body format of the message. The possible values are

and

.

The

parameter of the message.

The

parameter of the message.

A semicolon-delimited list of file names attached to the e-

mail message.

The type of mail attachment.

The query executed by the mail program.

The database context within which the mail program

executed the query.

ﾉ

Expand table

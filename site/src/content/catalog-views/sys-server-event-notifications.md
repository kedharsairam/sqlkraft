---
name: 'sys.server_event_notifications'
title: 'sys.server_event_notifications (Transact-'
category: 'objects'
description: 'Returns a row for each server-level event notification object.'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

SQL)

09/24/2025

Applies to:

SQL Server


## Returns a row for each server-level event notification object.

## Description
Server event notification name. Is unique across all server-level

event notifications.

Object identification number. Is unique within the

database.

Class of parent. Is always 100 = Server.


## Description of class of parent. Is always
.

Is always 0.

Date created.

Date object was last modified by using an

statement.

Name of the target service to which the notification is sent.

The service broker where the named target service is defined.

SID of the login executing the statement that creates the event

notification.

if

is not specified in the event

notification definition.

ID of the server principal that owns this.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

visibility configuration

.

ﾉ

Expand table

Related content

Object catalog views (Transact-SQL)

System catalog views (Transact-SQL)

```sql
name
```

```sql
object_id
```

```sql
master
```

```sql
parent_class
```

```sql
parent_class_desc
```

```sql
SERVER
```

```sql
parent_id
```

```sql
create_date
```

```sql
modify_date
```

```sql
ALTER
```

```sql
service_name
```

```sql
broker_instance
```

```sql
creator_sid
```

```sql
NULL
```

```sql
WITH FAN_IN
```

```sql
principal_id
```

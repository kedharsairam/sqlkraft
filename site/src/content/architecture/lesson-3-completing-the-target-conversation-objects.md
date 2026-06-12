---
title: "Lesson 3: Completing the Target Conversation Objects"
topic: "service-broker"
description: ""
tags: ["service-broker","lesson-3-completing-the-target-conversation-objects"]
pubDate: "2025-12-01"
---

In this lesson, you learn to create the linked server and routes from the target instance of the

Database Engine to the initiator instance. Run these steps from a copy of Management Studio

that is running on the same computer as the target instance.

Copy and paste the following code into a Query Editor window. Change the

clause to reference the folder to which you copied the

file from

step 4 in Lesson 2. Then, run the code to create an initiator user and pull in the initiator

certificate.

Copy and paste the following code into a Query Editor window. Change the string

to the name of the computer that is running your initiator instance.

Then, run the code to create routes to the target service and initiator service, and a

remote service binding that associates the

with the initiator service route.

The following

statements assume that there are no duplicate service names

in the target instance. If multiple databases on the target instance contain services that

```sql
FROM FILE
CREATE ROUTE
USE
InstTargetDB;
GO
CREATE
USER
InitiatorUser
WITHOUT
LOGIN;
CREATE
CERTIFICATE InstInitiatorCertificate
AUTHORIZATION InitiatorUser
FROM
FILE
=
N
'C:\storedcerts\$ampleSSBCerts\InstInitiatorCertificate.cer'
;
GO
```

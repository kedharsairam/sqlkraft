---
title: "Troubleshooting Tools (Service Broker)"
topic: "service-broker"
description: "08/29/2025 Service Broker provides several tools to diagnose configuration and conversation problems. Service Broker is a component of the Databa"
tags: ["service-broker","troubleshooting-tools-service-broker"]
pubDate: 2025-12-01
---

Service Broker provides several tools to diagnose configuration and conversation problems.

Service Broker is a component of the Database Engine. Therefore, many of the Database

Engine tools can also be used to diagnose Service Broker problems.

The

utility analyzes the configuration of Service Broker services and running

conversations for errors. Use

to do the following:

Confirm that there are no configuration errors in a newly configured Service Broker

application.

Confirm that there are no configuration errors after you change the configuration of an

existing Service Broker application.

Confirm that there are no configuration errors after a Service Broker database is detached

and then reattached to a new instance of the Database Engine.

Determine what errors are preventing messages from being successfully transmitted

between services.

For more information about how to use the utility, see

ssbdiagnose utility.

Service Broker messages that aren't successfully transmitted to the receiving queue are held in

the Service Broker transmission queue in the sending database. You can use the

system view in each database to see the messages in the queue. For

any messages that are in the queue because of a transmission error, the

column contains the error message.

Not all messages in the transmission queue are caused by errors:

Some messages in the queue could be in the process of being sent. Examples include

waiting for a disconnected receiver to be reconnected or a network send to be

acknowledged.

```sql
sys.transmission_queue transmission_status
```

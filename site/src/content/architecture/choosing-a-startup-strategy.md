---
title: "Choosing a Startup Strategy"
topic: "service-broker"
description: "08/29/2025 This article describes options for Service Broker activation. Service Broker supports asynchronous, queued messaging. Because conversa"
tags: ["service-broker","choosing-a-startup-strategy"]
pubDate: 2025-12-01
---

This article describes options for Service Broker activation.

Service Broker supports asynchronous, queued messaging. Because conversations can last for

days, months, or years, many applications use activation to scale dynamically. This section

describes some common strategies for starting an application that uses Service Broker.

The strategies for starting an application fall into four broad categories:

Internal activation

Event-based activation

Scheduled task

Startup task

Each activation strategy has different advantages. An application can combine these strategies.

For example, an application can use internal activation with a small number of queue readers

most of the time, but at certain times of the day, it can start more queue readers.

With Service Broker internal activation, a Service Broker queue monitor directly activates a

stored procedure when it's necessary. This is often the most straightforward approach. By using

direct activation of a stored procedure, you don't have to write additional code in the

application to manage activation. However, internal activation requires that the application be

written as a SQL Server stored procedure. When using internal activation, you write the

application to exit when there are no more messages to process.

Some applications run in response to a specific event. For example, you can run an application

when the CPU usage on the computer falls below a certain level, or you can run a logging

application when a new table is created.

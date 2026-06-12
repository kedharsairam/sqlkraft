---
title: "Handling Poison Messages"
topic: "service-broker"
description: ""
tags: ["service-broker","handling-poison-messages"]
pubDate: 2025-12-01
---

This article describes one way that an application that uses Service Broker can detect a poison

message and remove the message from the queue without relying on automatic poison

message detection.

Service Broker provides automatic poison message detection. Automatic poison message

detection sets the queue status to

if a transaction that receives messages from the queue

rolls back five times. This feature provides a safeguard against catastrophic failures that an

application can't detect programmatically. However, an application shouldn't rely on this

feature for normal processing. Because automatic poison message detection stops the queue,

this feature effectively halts all processing for the application until the poison message is

removed. Instead, an application should attempt to detect and remove poison messages as

part of the application logic.

The strategy outlined in this section assumes that a message should be removed if it fails a

certain number of times. For many applications, this assumption is valid. However, before using

this strategy in your application, consider the following questions:

Is a failure count reliable for your application? Depending on your application, it might be

normal for messages to fail from time to time. For example, in an order-entry application,

the service that processes an order might take less processing time than the service that

adds a new customer record. In this case, it might be normal that an order for a new

customer can't be processed immediately. The application needs to account for the delay

when deciding whether a message is a poison message or not. The service might need to

allow several failures before removing the message.

Can your application quickly and reliably check the content of a message to detect that it

can never succeed? If so, this is a better strategy than counting the number of times that

the program failed to process the message. For example, an expense report that doesn't

contain an employee name or an employee ID number can't be processed. In this case,

the program might be more efficient if it immediately responds to a message that can't

be processed with an error, rather than attempting to process the message. Consider

other validation as well. For example, if the ID number is present, but falls outside the

range of assigned numbers (for example, a negative number), the application can end the

conversation immediately.

Should you remove a message after any failure? If the application handles a high volume

of messages where each message has a limited useful life, it might be most efficient to

`OFF`

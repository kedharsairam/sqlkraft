---
title: "Planning for Service Broker Development"
topic: "service-broker"
description: |
  09/03/2025
          
            Review the following as you design a Service Broker application:
          
            The metrics concerning the type and volume of input and output expected from your
          
            application.
          
            The requirements for your
tags: ["service-broker","planning-for-service-broker-development"]
pubDate: 2025-12-01
---

Review the following as you design a Service Broker application:

The metrics concerning the type and volume of input and output expected from your

application.

The requirements for your proposed application.

If you understand these factors, you can develop a system that meets business goals.

Consider the following questions as you plan your application:

The answer to this question helps you plan the message types your application uses, the

structure of your application, and the storage and processing needs of your application.

For example, your application could use Service Broker to deal with spikes in message arrival

rates by storing the messages in queues until resources are available to process them. In this

case, the message types your application uses should closely match the input and output of

the existing application. You can estimate storage and processing needs for your application,

depending on the existing workload.

In contrast, if you design a new application, carefully consider which operations can benefit the

most from Service Broker. Using Service Broker often trades off predictable processing times in

the best case in return for reliability when a conventional application would fail completely.

For example, an online order entry application might not have to completely process the order

and provide final confirmation at the time the order is submitted. Instead, the application

might submit the order to a service that processes the order and provides final confirmation

through e-mail. By using this design, the order application can continue to accept orders even

if networking problems prevent the application from confirming the order. When the

networking problems are resolved, the application processes the orders. In this case, the

storage and processing needs for the application depend on the number of orders expected,

the size of each order message, and the time each order requires to be processed.

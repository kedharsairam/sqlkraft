---
title: "Completing a Conversation Between Instances"
topic: "service-broker"
description: "08/29/2025 This tutorial is intended for users who are new to Service Broker, but are familiar with database concepts and Transact-SQL statements"
tags: ["service-broker","completing-a-conversation-between-instances"]
pubDate: 2025-12-01
---

This tutorial is intended for users who are new to Service Broker, but are familiar with database

concepts and Transact-SQL statements. It helps new users get started by showing them how to

build and run a simple conversation between two databases on separate instances of the

Database Engine.

This tutorial builds on the tasks that you learned in

Complete a conversation between

databases. In this tutorial, you learn how to configure a conversation so that it runs between

two instances of the Database Engine.

The steps that you follow in this tutorial are the same as those you followed in the Complete a

Conversation Between Databases tutorial, with these exceptions:

The two databases are on separate instances of the Database Engine.

You can learn how to create Service Broker endpoints and routes to establish network

connections between two instances.

The previous tutorials didn't transmit messages on the network. Therefore, they used

Database Engine permissions to help protect against unauthorized access to messages. In

Lesson 3, you learn how to create certificates and remote service bindings to encrypt

messages on the network.

In this tutorial, the instance of the Database Engine that contains the initiator database is

referred to as the

initiator instance. The instance that contains the target database is referred to

as the

target instance.

This tutorial is divided into six lessons:

Description

Lesson 1: Creating the

Target Database

In this lesson, you create the target database and all the objects that don't

have dependencies on the initiator database. This includes the endpoint,

ﾉ

Expand table

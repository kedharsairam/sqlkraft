---
title: "Symptoms and causes of spinlock contention"
topic: "locking"
description: ""
tags: ["locking","architecture"]
pubDate: 2026-05-29
---

This article provides in-depth information on how to identify and resolve issues related to

spinlock contention in SQL Server applications on high-concurrency systems.

In the past, commodity Windows Server computers have utilized only one or two

microprocessor/CPU chips, and CPUs have been designed with only a single processor or

"core". Increases in computer processing capacity have been achieved by using faster CPUs,

made possible largely through advancements in transistor density. Following "Moore's Law",

transistor density or the number of transistors that can be placed on an integrated circuit have

consistently doubled every two years since the development of the first general purpose single

chip CPU in 1971. In recent years, the traditional approach of increasing computer processing

capacity with faster CPUs has been augmented by building computers with multiple CPUs. As

of this writing, the Intel Nehalem CPU architecture accommodates up to eight cores per CPU,

which when used in an eight socket system can then be doubled to 128 logical processors by

using simultaneous multithreading (SMT) technology. On Intel CPUs, SMT is called

Hyper-

Threading. As the number of logical processors on x86 compatible computers increases,

concurrency-related issues increase as logical processors compete for resources. This guide

describes how to identify and resolve particular resource contention issues observed when

running SQL Server applications on high concurrency systems with some workloads.

In this section, we analyze the lessons learned by the SQLCAT team from diagnosing and

resolving spinlock contention issues. Spinlock contention is one type of concurrency issue

observed in real customer workloads on high scale systems.

７

Note

The recommendations and best practices documented here are based on real-world

experience during the development and deployment of real world OLTP systems. It was

originally published by the Microsoft SQL Server Customer Advisory Team (SQLCAT) team.

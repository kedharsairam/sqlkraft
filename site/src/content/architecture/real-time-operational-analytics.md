---
title: "Real-time operational analytics"
topic: "filestream"
description: "2016 (13.x) introduces real-time operational analytics, the ability to run both a"
tags: ["filestream","real-time-operational-analytics"]
pubDate: "2025-12-01"
---

2016 (13.x) introduces real-time operational analytics, the ability to run both

analytics and OLTP workloads on the same database tables at the same time. Besides running

analytics in real time, you can also eliminate the need for ETL and a data warehouse.

Traditionally, businesses have had separate systems for operational (that is, OLTP) and analytics

workloads. For such systems, Extract, Transform, and Load (ETL) jobs regularly move the data

from the operational store to an analytics store. The analytics data is usually stored in a data

warehouse or data mart dedicated to running analytics queries. While this solution has been

the standard, it has these three key challenges:

Implementing ETL can require considerable coding especially to load only

the modified rows. It can be complex to identify which rows have been modified.

Implementing ETL requires the cost of purchasing additional hardware and software

licenses.

Implementing ETL adds a time delay for running the analytics. For example,

if the ETL job runs at the end of each business day, the analytics queries will run on data

that is at least a day old. For many businesses this delay is unacceptable because the

business depends on analyzing data in real time. For example, fraud-detection requires

real-time analytics on operational data.

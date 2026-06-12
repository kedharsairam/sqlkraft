---
title: "Mechanical hard drives"
topic: "query-processing"
description: "Other drive implementations, such as IDE, ATA, and SATA:"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

Other drive implementations, such as IDE, ATA, and SATA:

Are typically designed for light to medium-duty use.

Are typically targeted at single-user applications.

Non-SCSI, desktop-based controllers require more main processor (CPU) bandwidth and are

frequently limited by a single active command. For example, when a non-SCSI drive is adjusting a

bad block, the drive requires that the host commands wait. The ATA bus presents another

example: the ATA bus supports two devices, but only a single command can be active. This

limitation leaves one drive idle while the other drive services the pending command. RAID

systems built on desktop technologies can all experience these symptoms and be greatly affected

by the slowest responder. Unless these systems use advanced designs, their performance isn't as

efficient as the performance of SCSI-based systems.

A desktop-based drive or array can be a low-cost solution for some situations. For example, if

you set up a read-only database for reporting, you don't encounter many of the performance

factors of an OLTP database when drive caching is disabled.

Storage device sizes continue to increase. Low-cost, high-capacity drives can be appealing. But

when you configure the drive for SQL Server and your business response time needs, carefully

consider the following issues:

Access path design

The requirement to disable the on-disk cache

Mechanical drives use spinning magnetic platters for storing data. They're available in several

capacities and form factors, such as IDE, SATA, SCSI, and Serial Attached SCSI (SAS). Some SATA

drives include failure prediction constructs. SCSI drives are designed for heavier duty cycles and

decreased failure rates.

write to, remote block-level storage across IP networks. Since iSCSI depends on networks,

you can experience delays or bottlenecks. Ensure the server's caching performance is

optimal, and latency is minimized. For more information, see.

## Bit corruption

## Flying writes

## Shorn writes

## Metadata corruption

## Unresponsive device

## Unserializability

## Recommendation

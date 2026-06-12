---
title: "Page and extent architecture guide"
topic: "query-processing"
description: ""
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

This guide describes the structure of pages and extents, and the organization of pages and

extents within data files.

A

page

is a fundamental unit of data storage in the Database Engine. The disk space allocated

to a data file (.mdf or.ndf) in a database is logically divided into pages numbered contiguously

from 0 to

n. Disk I/O operations against data files are performed at the page level. That is, the

Database Engine reads or writes whole data pages.

An

extent

is a collection of eight physically contiguous pages, used to manage pages efficiently.

Every page belongs to an extent.

Transaction log files (.ldf) don't contain pages. They contain a series of log records which don't

have a fixed size.

In a regular book, all content is written on pages. Similar to a book, the Database Engine writes

all data rows on pages. The size of every page is the same: 8 KiB. In a book, most pages contain

the data, or the main content of the book. Some pages contain metadata describing the

content, for example, the table of contents and the index.

Similarly, most pages in the database contain actual rows of data. These are called

data pages.

Text/LOB

pages also contain data, but are used only by large object (LOB) data types.

Index

pages

contain index structures that help find data efficiently. Finally, a variety of

system pages

store the metadata describing the organization and properties of the data.

The following table describes page types.

Data

Data rows with all data. Data in columns using the LOB data types can also be

partially stored on data pages.

Text/LOB

Data in columns using the LOB data types, such as

,

,

,

,

,

,

, and.

ﾉ

Expand table

Data in variable length columns when the data row exceeds 8 KiB, for columns

using data types such as

,

,

, and

sql_variant.

Index

Btree index structures.

Global Allocation Map

(GAM)

Shared Global

Allocation Map (SGAM)

Information about allocated and unallocated extents.

Page Free Space (PFS)

Information about page allocation and free space available on pages.

Index Allocation Map

(IAM)

Information about the extents used by a heap or index in an allocation unit.

Bulk Changed Map

(BCM)

Information about the extents modified by bulk operations since the last

transaction log backup.

Differential Changed

Map (DCM)

Information about the extents that have changed since the last full database

backup.

Each page begins with a 96-byte header that is used to store system information about the

page. This information includes the page number, the page type, and can include other

metadata such as the object ID and the index ID of the object and index that own the page.

A structure called the

slot array

is stored at the end of the page. Each 2-byte element in the

slot array corresponds to a row stored on the page. A slot array element stores the byte offset

of the row relative to the start of the page. The Database Engine uses these offsets to locate

rows on a page.

When the Database Engine adds a row to an empty page, it stores the row immediately after

the header. The slot array element for the first row is stored at the very end of the page. As

more rows are added, they are stored one after another from the beginning to the end of the

page, while the slot array grows from the end to the beginning of the page, as shown on the

following diagram.

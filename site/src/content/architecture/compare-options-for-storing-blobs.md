---
title: "Compare Options for Storing Blobs"
topic: "filestream"
description: "Discusses and compares the options that are available for storing files and documents in SQL Server. A large percentage of enterprise data is unstruc"
tags: ["filestream","compare-options-for-storing-blobs"]
pubDate: 2025-12-01
---

Discusses and compares the options that are available for storing files and documents in SQL

Server.

A large percentage of enterprise data is unstructured in nature, and is typically stored as files

and documents in file systems. Most of this data is produced, managed, and consumed by

applications that access the files through Windows APIs. Enterprises typically keep this data in

the file system, while storing the related metadata for the files in a relational database.

Integrating unstructured data into the relational database provides the following benefits:

Integrated storage and data management capabilities such as backup.

Integrated services such as full-text search and semantic search over data and metadata.

Ease of administration and policy management over the unstructured data.

Generally it has been inconvenient to store unstructured data in a relational database. It has

been impractical to rewrite established applications (such as Microsoft Word or Adobe Reader)

to interact through relational database APIs. These applications expect the data to be

accessible through Windows APIs. The applications have the following expectations:

Windows applications are not aware of database transactions and do not require them.

Windows applications require compatibility with file system APIs for file and directory

data.

Many years ago, SQL Server did not offer any variety of ways to store unstructured data in a

relational database. But nowadays it does offer ways to store unstructured data.

already has the FILESTREAM feature. The FILESTREAM feature provides efficient

storage, management, and streaming of unstructured data stored as files on the file system.

However, a FILESTREAM solution requires custom programming, and does not satisfy the

requirement for full Windows application compatibility described above.

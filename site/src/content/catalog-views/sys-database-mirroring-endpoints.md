---
name: 'sys.database_mirroring_endpoints'
title: 'sys.database_mirroring_endpoints'
category: 'objects'
description: 'The visibility of the metadata in catalog views is limited to securables that a user either owns,'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

SQL Server 2022 (16.x) and later versions require VIEW SERVER SECURITY STATE permission on

the server.

Specify the Endpoint URL When Adding or Modifying an Availability Replica (SQL Server)

sys.availability_replicas (Transact-SQL)

sys.database_mirroring (Transact-SQL)

sys.database_mirroring_witnesses (Transact-SQL)

The Database Mirroring Endpoint (SQL Server)

Querying the SQL Server System Catalog FAQ

Last updated on 03/03/2026

７

Note

The RC4 algorithm is only supported for backward compatibility. New material can only be

encrypted using RC4 or RC4_128 when the database is in compatibility level 90 or 100.

(Not recommended.) Use a newer algorithm such as one of the AES algorithms instead. In

SQL Server 2012 (11.x) and higher, material encrypted using RC4 or RC4_128 can be

decrypted in any compatibility level.

Related content

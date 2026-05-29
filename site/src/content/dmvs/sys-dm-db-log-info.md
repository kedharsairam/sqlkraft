---
name: 'sys.dm_db_log_info'
title: 'sys.dm_db_log_info'
category: 'log'
description: 'SQL Server 2016 (13.x) SP2 and later versions SQL database in Microsoft Fabric information of the transaction log. Note all transaction log files are combined in the table output. Each row in the output represents a VLF in the transaction log and provides information relevant to that VLF in the log. . Valid inputs are the ID number of a database, NULL, or DEFAULT. The default is NULL. NULL and DEF'
tags: ["log", "dmv"]
pubDate: 2026-05-29
syntax: 'sys.dm_db_log_info ( database_id )'
---

## Description

SQL Server 2016 (13.x) SP2 and later versions SQL database in Microsoft Fabric information of the transaction log. Note all transaction log files are combined in the table output. Each row in the output represents a VLF in the transaction log and provides information relevant to that VLF in the log. . Valid inputs are the ID number of a database, NULL, or DEFAULT. The default is NULL. NULL and DEFAULT are equivalent values in the context

## Syntax

```sql
sys.dm_db_log_info ( database_id )
```

## Permissions

vlf_begin_offset Offset location of the virtual log file (VLF) from the beginning of the transaction log file. vlf_size_mb virtual log file (VLF) size in MB, rounded to two decimal places. vlf_sequence_number virtual log file (VLF) sequence number in the created order. Used to uniquely identify VLFs in log file. vlf_active Indicates whether virtual log file (VLF) is in use or not. 0 - VLF isn't in use. 1 - VLF is active. vlf_status Status of the virtual log file (VLF) . Possible values include 0 - VLF is inactive 1 - VLF is initialized but unused 2 - VLF is active. vlf_parity Parity of virtual log file (VLF) . Used internally to determine the end of log within a VLF. vlf_first_lsn Log sequence number (LSN) of the first log record in the virtual log file (VLF) . vlf_create_lsn Log sequence number (LSN) of the log record that created the virtual log file (VLF) . vlf_encryptor_thumbprint SQL Server 2019 (15.x) and later Shows the thumbprint of the encryptor of the VLF if the VLF is encrypted using Transparent Data Encryption , otherwise . The dynamic management function replaces the statement. The formula for how many VLFs are created based on a growth event is detailed in the SQL Server Transaction Log Architecture and Management Guide . This formula changed slightly starting in SQL Server 2022 (16.x). Requires the permission in the database.

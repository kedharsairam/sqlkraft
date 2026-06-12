---
name: "To Add TDE Enabled Databases to Always on AG"
title: "To Add TDE Enabled Databases to Always on AG"
description: "Create Master Key in all Replicas"
category: high-availability
tags: ["database", "high-availability"]
pubDate: 2025-03-15
---

```sql
--Create Master Key in all Replicas
USE master;
Go
CREATE MASTER KEY ENCRYPTION BY PASSWORD = '[password]';
GO

--Create Database Encryption Certificate
USE master;
GO
CREATE CERTIFICATE Certificatename WITH SUBJECT='Certificatesubject';
GO

--Backup Database Encryption Certificate
USE master;
GO
BACKUP CERTIFICATE [Certificatename]
TO FILE = 'path\filename.cer'
WITH PRIVATE KEY (file='path\filename_key.pvk',
ENCRYPTION BY PASSWORD='[password]');

--Create Database Encryption Key in User Database
USE userdatabasename
GO
CREATE DATABASE ENCRYPTION KEY WITH ALGORITHM = AES_256
ENCRYPTION BY SERVER CERTIFICATE Certificatename;

--Turn ON Encryption for User Database
ALTER DATABASE Databasename SET ENCRYPTION ON

--Backup User Database (Make sure to take Both Full and Log Backups) backup database databasename to disk = N'path\filename.bak'
backup log databasename to disk = N'path\filename.trn'

--Restore Database Encryption Certificate in all Replicas
USE master;
GO
Create CERTIFICATE [Certificatename]
From FILE = 'path\filename.cer'
WITH PRIVATE KEY (file='path\filename_key.pvk',
DECRYPTION BY PASSWORD='[password]');

--Restore User Database with NORECOVERY in all Replicas
USE [master]
RESTORE DATABASE [databasename]
FROM DISK = N'path\filename.bak'
WITH FILE = 1,
MOVE N'logicalfilename' TO N'path\filename.mdf',
MOVE N'logicalfinename_log' TO N'path\filename_log.ldf',
NOUNLOAD, STATS = 5
GO

--Create Availability Group on Primary Replica
USE master;
GO
CREATE AVAILABILITY GROUP [TDE] WITH (DB_FAILOVER = ON) FOR REPLICA ON
'instancename1' WITH (ENDPOINT_URL = 'TCP://instancename.domainname.com:5022', AVAILABILITY_MODE = SYNCHRONOUS_COMMIT, FAILOVER_MODE = AUTOMATIC),
'instancename2' WITH (ENDPOINT_URL = 'TCP://instancename.domainname.com:5022', AVAILABILITY_MODE = SYNCHRONOUS_COMMIT, FAILOVER_MODE = AUTOMATIC);

--Join all the Secondary Replicas in Availability Group

--Add TDE Enabled User Database to Availability Group in Primary Replica
USE master
GO
ALTER AVAILABILITY GROUP TDE ADD DATABASE [Databasename]

--Add TDE Enabled User Dataabse to Availability Group in all Scondary Replicas
Use Master
Go
ALTER DATABASE Databasename SET HADR AVAILABILITY GROUP = TDE;
```

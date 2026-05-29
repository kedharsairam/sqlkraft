---
name: 'Oracle'
title: 'Oracle'
category: 'operators'
description: 'SQL) CONNECTION_OPTIONS'
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

SQL) CONNECTION_OPTIONS

08/21/2025

Applies to:

SQL Server 2016 (13.x) and later

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

This article provides additional detail for

depending on the provider. The

CREATE

EXTERNAL DATA SOURCE

argument can vary depending on the external data provider.

The

argument for

CREATE EXTERNAL DATA SOURCE

was first introduced in SQL Server

2019 (15.x). This document applies to SQL Server 2019 (15.x) for Windows and Linux, as well as SQL Server 2019

Big Data Clusters.

The

is the keyword and the value for a specific connection option.

To use multiple connection options, separate them by a semi-colon.

Possible key value pairs are specific to the driver.

The remainder of this article contains vendor-specific connection options.

You can only specify the key-value pairs that have an entry in

DSN and Connection String Keywords and

Attributes

under the

column. For example, the

keyword isn't supported, because that is an attribute set using

SQLSetConnectAttr

, not in the connection

string.

You can only specify the key-value pairs that have an entry in the Oracle wire protocol table as follows:

Attribute (Short Name)

Default

AccountingInfo (AI)

None

Action (ACT)

None

AlternateServers (ASRV)

None

AllowedOpenSSLVersions (AOV)

latest

SQL Server external data source

７

Note

PolyBase supports only the Microsoft ODBC Driver version 17 and 18. For more information, see

.

ﾉ

Expand table

Attribute (Short Name)

Default

ApplicationName (AN)

None

ApplicationUsingThreads (AUT)

1 (Enabled)

ArraySize (AS)

60000

AuthenticationMethod (AM)

1 (Encrypt Password)

BatchFailureReturnsError (BFRE)

0 (Disabled)

BindParamsAsUnicode (BPAU)

0 (Disabled)

BulkBinaryThreshold (BBT)

32

BulkCharacterThreshold (BCT)

-1

BulkLoadBatchSize (BLBS)

1024

BulkLoadFieldDelimiter (BLFD)

None

BulkLoadOptions (BLO)

0

BulkLoadRecordDelimiter (BLRD)

None

CachedCursorLimit (CCL)

32

CachedDescriptionLimit (CDL)

0

CatalogIncludesSynonyms (CIS)

1 (Enabled)

CatalogOptions (CO)

0 (Disabled)

ClientHostName (CHN)

None

ClientID (CID)

None

ClientUser (CU)

None

ConnectionReset (CR)

0 (Disabled)

ConnectionRetryCount (CRC)

0

ConnectionRetryDelay (CRD)

3

CredentialsWalletEntry (CWE)

None

CredentialsWalletPassword (CWPWD)

None

CredentialsWalletPath (CWPATH)

None

CryptoProtocolVersion (CPV)

TLSv1.2, TLSv1.1, TLSv1

CryptoLibName (CLN)

Empty string

DataIntegrityLevel (DIL)

1 (Accepted)

DataIntegrityTypes (DIT)

MD5, SHA1, SHA256, SHA384, SHA512

DataSourceName (DSN)

None

Attribute (Short Name)

Default

DefaultLongDataBuffLen (DLDBL)

1024

DescribeAtPrepare (DAP)

0 (Disabled)


## Description (n/a)
None

EditionName (EN)

None

EnableBulkLoad (EBL)

0 (Disabled)

EnableDescribeParam (EDP)

0 (Disabled)

EnableNcharSupport (ENS) (deprecated.)

None

EnableScrollableCursors (ESC)

1 (Enabled)

EnableServerResultCache (ESRC)

0 (Disabled)

EnableStaticCursorsForLongData (ESCLD)

0 (Disabled)

EnableTimestampwithTimezone (ETWT)

(deprecated)

None

EncryptionLevel (EL)

1 (Accepted)

EncryptionMethod (EM)

0 (No Encryption)

EncryptionTypes (ET)

No encryption methods are specified. The driver sends a list of all of the

encryption methods to the Oracle server.

FailoverGranularity (FG)

0 (Non-Atomic)

FailoverMode (FM)

0 (Connection)

FailoverPreconnect (FP)

0 (Disabled)

FetchTSWTZasTimestamp (FTSWTZAT)

0 (Disabled)

GSSClient (GSSC)

native

HostName (HOST)

None

HostNameInCertificate (HNIC)

None

IANAAppCodePage (IACP) (UNIX and Linux

only)

4 (ISO 8559-1 Latin-1)

ImpersonateUser (IU)

None

InitializationString (IS)

None

KeepAlive (KA)

0 (Disabled)

KeyPassword (KP)

None

Keystore (KS)

None

KeystorePassword (KSP)

None

LDAPDistinguishedName (LDAPDN)

None

Attribute (Short Name)

Default

LoadBalanceTimeout (LBT)

0

LoadBalancing (LB)

0 (Disabled)

LOBPrefetchSize (LPS)

4000

LocalTimezoneOffset (LTZO)

"" (Empty String)

LockTimeout (LTO)

-1

LoginTimeout (LT)

15

LogonID (UID)

None

MaxPoolSize (MXPS)

100

MinPoolSize (MNPS)

0

Module (MOD)

None

Password (PWD)

None

Pooling (POOL)

0 (Disabled)

PortNumber (PORT)

None

PRNGSeedFile (PSF) (UNIX and Linux only)

/dev/random

PRNGSeedSource (PSS) (UNIX and Linux

only)

0 (File)

ProcedureRetResults (PRR)

0 (Disabled)

ProgramID (PID)

None

ProxyHost (PXHN)

Empty string

ProxyMode (PXM)

0 (NONE)

ProxyPassword (PXPW)

Empty string

ProxyPort (PXPT)

0

ProxyUser (PXU)

Empty string

QueryTimeout (QT)

0

ReportCodepageConversionErrors (RCCE)

0 (Ignore Errors)

ReportRecycleBin (RRB)

0 (Disabled)

SDUSize (SDU)

16384

ServerName (SRVR)

None

ServerType (ST)

0 (Server Default)

ServiceName (SN)

None. If no value is specified for either the SID, Service Name, or TNSNames

option, the driver attempts to connect to the ORCL SID by default.

```sql
CONNECTION_OPTIONS
```

```sql
CONNECTION_OPTIONS
```

```sql
CONNECTION_OPTIONS
```

```sql
key_value_pair
```

```sql
SQL_ATTR_TXN_ISOLATION
```

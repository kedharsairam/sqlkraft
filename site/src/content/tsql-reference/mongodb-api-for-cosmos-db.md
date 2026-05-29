---
name: 'MongoDB API for Cosmos DB'
title: 'MongoDB API for Cosmos DB'
category: 'statements'
description: 'Attribute (Short Name)'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Attribute (Short Name)

Default

SID (SID)

None. If no value is specified for either the SID, Service Name, or TNSNames

option, the driver attempts to connect to the ORCL SID by default.

SSLLibName (SLN)

Empty string

SupportBinaryXML (SBX)

0 (Disabled)

TimestampEscapeMapping (TEM)

0 (Oracle Version Specific)

TNSNamesFile (TNF)

None. If no value is specified for either the SID, Service Name, or TNSNames

option, the driver attempts to connect to the ORCL SID by default.

Truststore (TS)

None

TruststorePassword (TSP)

None

UseCurrentSchema (UCS)

1 (Enabled)

UseDefaultEncryptionOptions

1 (Enabled)

ValidateServerCertificate (VSC)

1 (Enabled)

WireProtocolMode (WPM)

2

You can only specify the key-value pairs that have an entry in the connector configuration options provided in

the

Teradata Connector Configuration Options

.

You can only specify the key-value pairs that have an entry in the following driver configuration options.

Key name

Default

Required


## Description
255

No

The maximum number of characters that can be contained in

columns. The maximum value that you can set for this option is

2147483647.

False

No

This option specifies whether the driver allows active cursors on the

data source server to expire. When

, the data source server will

time out idle cursors after the threshold inactivity period set on the

server. When set to

, the driver prevents the data source server

from timing out idle cursors, and there's a risk that if the driver should

quit or lose the connection to the server unexpectedly, the cursor

remains open on the server indefinitely. You can adjust the threshold

for idle cursor timeouts on the MongoDB server, see

MongoDB Server

Parameters for a Self-Managed Deployment

for details.

100

No

The maximum number of records that the driver can sample to

generate a temporary schema definition. When this option is set to 0,

the driver samples every document in the database.

ﾉ

Expand table

```sql
DefaultStringColumnLength
```

```sql
STRING
```

```sql
noCursorTimeout
```

```sql
FALSE
```

```sql
TRUE
```

```sql
SamplingLimit
```

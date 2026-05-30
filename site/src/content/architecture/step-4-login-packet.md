---
title: "Step 4. Login packet"
topic: "transaction-log"
description: "This packet is encrypted and might show as"
tags: ["transaction-log", "architecture"]
pubDate: 2026-05-29
---

Output

This packet is encrypted and might show as

or

, depending

on your network parser. If all the packets after this step also show as

, the connection is encrypted.

Output

```sql
SSL Application Data
```

```sql
TDS:Data
```

```sql
SSL Application
Data
```

```sql
Frame Time Offset Source IP    Dest IP      Description
----- ----------- ------------ ------------ ----------------------------------
-----------------------------------------------------------------
6132  116.5835288 10.10.10.10  10.10.10.120 TLS:TLS Rec Layer-1 HandShake:
Client Hello. {TLS:328, SSLVersionSelector:327, TDS:326, TCP:325, IP
6133  116.5845058 10.10.10.120 10.10.10.10  TLS:TLS Rec Layer-1 HandShake:
Server Hello. Certificate. Server Hello Done. {TLS:328, SSLVersionSe
6134  116.5864588 10.10.10.10  10.10.10.120 TLS:TLS Rec Layer-1 HandShake:
Client Key Exchange.; TLS Rec Layer-2 Cipher Change Spec; TLS Rec La
6135  116.5923178 10.10.10.120 10.10.10.10  TLS:TLS Rec Layer-1 Cipher Change
Spec; TLS Rec Layer-2 HandShake: Encrypted Handshake Message. {TL
```

```sql
Frame Time Offset Source IP    Dest IP      Description
----- ----------- ------------ ------------ ----------------------------------
-----------------------------------------------------------------
```

---
name: "sys.sp_refresh_parameter_encryption"
title: "sp_refresh_parameter_encryption"
category: "general"
description: "2016 (13.x) and later Updates the Always Encrypted metadata for the parameters of the specified non-schema- bound stored procedure, user-defined function, view, DML trigger, database-level DDL trigger, or server-level DDL trigger in the current database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_refresh_parameter_encryption
  [ @name = ]
  N
  'name'
  [ , [ @namespace = ] {
  OBJECT
  |
  DATABASE
  _
  DDL
  _
  TRIGGER
  |
  SERVER
  _
  DDL
  _
  TRIGGER
  } ]
  [ ; ]
---

## Description

2016 (13.x) and later Updates the Always Encrypted metadata for the parameters of the specified non-schema- bound stored procedure, user-defined function, view, DML trigger, database-level DDL trigger, or server-level DDL trigger in the current database.

## Syntax

```sql
sp_refresh_parameter_encryption
[ @name = ]
N
'name'
[ , [ @namespace = ] {
OBJECT
|
DATABASE
_
DDL
_
TRIGGER
|
SERVER
_
DDL
_
TRIGGER
} ]
[ ; ]
```

## Permissions

The encryption metadata for parameters of a module can become outdated, if: Encryption properties of a column in a table the module references, have been updated. For example, a column was dropped and a new column is added with the same name, but a different encryption type, encryption key, or an encryption algorithm. The module references another module with outdated parameter encryption metadata. When encryption properties of a table are modified, should be run for any modules directly or indirectly referencing the table. This stored procedure can be called on those modules in any order, without requiring the user to first refresh the inner module before moving to its callers. doesn't affect any permissions, extended properties, or options that are associated with the object. To refresh a server-level DDL trigger, execute this stored procedure from the context of any database. Requires permission on the module and permission on any CLR user-defined types and XML schema collections that are referenced by the object. When the specified module is a database-level DDL trigger, requires permission in the current database. When the specified module is a server-level DDL trigger, requires permission. For modules that are defined with the clause, permission is required on the specified principal. Generally, refreshing an object doesn't change its principal, unless the module was defined with and the user name of the principal now resolves to a different user than it did at the time the module was created. ７ Note Any signatures that are associated with the object are dropped when you run.

## Examples

### Example 1

`sp_refresh_parameter_encryption`

### Example 2

```sql
CREATE
TABLE
[Patients]
(
[PatientID]
INT
IDENTITY (1, 1)
NOT
NULL
,
[SSN]
CHAR (11),
[FirstName]
NVARCHAR (50)
NULL
,
[LastName]
NVARCHAR (50)
NOT
NULL
,
[MiddleName]
NVARCHAR (50)
NULL
,
[StreetAddress]
NVARCHAR (50)
NOT
NULL
,
[City]
NVARCHAR (50)
NOT
NULL
,
[ZipCode]
CHAR (5)
NOT
NULL
,
[State]
CHAR (2)
NOT
NULL
,
[BirthDate]
DATE
NOT
NULL
,
CONSTRAINT
[PK_Patients] PRIMARY
KEY
CLUSTERED ([PatientID]
ASC
)
);
GO
CREATE
PROCEDURE
[find_patient]
@SSN
CHAR (11)
AS
BEGIN
SELECT
*
FROM
[Patients]
WHERE
SSN = @SSN;
END
GO
CREATE
COLUMN
MASTER
KEY
[CMK1]
WITH (
KEY_STORE_PROVIDER_NAME = N
'MSSQL_CERTIFICATE_STORE'
,
KEY_PATH = N
'CurrentUser/my/A66BB0F6DD70BDFF02B62D0F87E340288E6F9305'
);
GO
CREATE
COLUMN
ENCRYPTION
KEY
[CEK1]
WITH
VALUES (
COLUMN_MASTER_KEY = [CMK1],
ALGORITHM =
'RSA_OAEP'
,
```

### Example 3

`sp_refresh_parameter_encryption`

### Example 4

```sql
ENCRYPTED_VALUE = 0x
016E000001630075007200720065006E00740075007300650072002F006D0079002F00610036003600
6200620030006600360064006400370030006200640066006600300032006200360032006400300066
003800370065003300340030003200380038006500360066003900330030003500CA0D0CEC74ECADD1
804CF99137B4BD06BBAB15D7EA74E0C249A779C7768A5B659E0125D24FF827F5EA8CA517A8E197ECA1
353BA814C2B0B2E6C8AB36E3AE6A1E972D69C3C573A963ADAB6686CF5D24F95FE43140C4F9AF48FBA7
DF2D053F3B4A1F5693A1F905440F8015BDB43AF8A04BE4E045B89876A0097E5FBC4E6A3B9C3C0D278C
540E46C53938B8C957B689C4DC095821C465C73117CBA95B758232F9E5B2FCC7950B8CA00AFE374DE4
2847E3FBC2FDD277035A2DEF529F4B735C20D980073B4965B4542A34723276A1646998FC6E1C40A3FD
B6ABCA98EE2B447F114D2AC7FF8C7D51657550EC5C2BABFFE8429B851272086DCED94332CF18FA854C
1D545A28B1EF4BE64F8E035175C1650F6FC5C4702ACF99850A4542B3747EAEC0CC726E091B36CE2439
2D801ECAA684DE344FECE05812D12CD72254A014D42D0EABDA41C89FC4F545E88B4B8781E5FAF40D71
99D4842D2BFE904D209728ED4F527CBC169E2904F6E711FF81A8F4C25382A2E778DD2A58552ED031AF
FDA9D9D891D98AD82155F93C58202FC24A77F415D4F8EF22419D62E188AC609330CCBD97CEE1AEF8A1
8B01958833604707FDF03B2B386487CC679D7E352D0B69F9FB002E51BCD814D077E82A09C14E9892C1
F8E0C559CFD5FA841CEF647DAB03C8191DC46B772E94D579D8C80FE93C3827C9F0AE04D5325BC73111
E07EEEDBE67F1E2A73580085
);
GO
ALTER
TABLE
[Patients]
DROP
COLUMN
[SSN];
GO
ALTER
TABLE
[Patients]
ADD
[SSN]
CHAR (11)
COLLATE
Latin1_General_BIN2 ENCRYPTED
WITH (
COLUMN_ENCRYPTION_KEY = [CEK1],
ENCRYPTION_TYPE =
DETERMINISTIC
,
ALGORITHM =
'AEAD_AES_256_CBC_HMAC_SHA_256'
)
NOT
NULL
;
GO
EXECUTE sp_refresh_parameter_encryption [find_patient];
GO
```

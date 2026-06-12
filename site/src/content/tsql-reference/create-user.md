---
name: "CREATE USER"
title: "CREATE USER"
category: "statements"
description: "T-SQL reference for CREATE USER syntax and usage."
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

### Users based on logins in

#### master

### new name for Azure Active Directory (Azure AD)

### Microsoft Entra server principals (logins)

ﾃ

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

Adds a user to the current database. The 13 types of users are listed with a sample of the most

basic syntax:

User based on a login based on a Windows Active Directory account.

User based on a login based on a Windows group.

User based on a login using SQL Server authentication.

User based on a Microsoft Entra login.

７

Note

While Microsoft Entra ID is the

, to

prevent disrupting existing environments, Azure AD still remains in some hardcoded

elements such as UI fields, connection providers, error codes, and cmdlets. In this article,

the two names are interchangeable.

７

Note

are currently in public preview for Azure

SQL Database.

７

Note

Logins, and therefore users based on logins, aren't supported in SQL database in

Microsoft Fabric.

### Users that authenticate at the database

### Users based on Windows principals that connect through Windows group logins

### Users that cannot authenticate

```sql
CREATE USER
[Contoso\Fritz];
```

```sql
CREATE USER [Contoso\Sales];
```

```sql
CREATE USER Mary;
```

```sql
CREATE USER [bob@contoso.com] FROM LOGIN
[bob@contoso.com]
```

---
name: "sys.server_sql_modules"
title: "sys.server_sql_modules"
category: "compatibility"
description: "Contains the set of SQL modules for server-level triggers of type TR. You can join this relation to sys.server_triggers. The tuple (object_id) is the key of the relation. This is a FOREIGN KEY reference back to the server-level trigger where this module is defined. SQL text that defines this module. Module was created with ANSI NULLS set option set to ON. Module was created with QUOTED IDENTIFIER "
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Contains the set of SQL modules for server-level triggers of type TR. You can join this relation to sys.server_triggers. The tuple (object_id) is the key of the relation. This is a FOREIGN KEY reference back to the server-level trigger where this module is defined. SQL text that defines this module. Module was created with ANSI NULLS set option set to ON. Module was created with QUOTED IDENTIFIER set option set

## Permissions

Article • 02/28/2023 Applies to: SQL Server Azure SQL Managed Instance Contains the set of SQL modules for server-level triggers of type TR. You can join this relation to sys.server_triggers. The tuple (object_id) is the key of the relation. Description This is a FOREIGN KEY reference back to the server-level trigger where this module is defined. SQL text that defines this module. NULL = Encrypted. Module was created with ANSI NULLS set option set to ON. Module was created with QUOTED IDENTIFIER set option set to ON. ID of the EXECUTE AS server principal. NULL by default or if EXECUTE AS CALLER ID of the specified principal if EXECUTE AS SELF EXECUTE AS principal-2 = EXECUTE AS OWNER. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Catalog Views (Transact-SQL) ﾉ Expand table See Also

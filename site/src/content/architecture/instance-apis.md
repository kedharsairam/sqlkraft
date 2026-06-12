---
title: "Instance APIs"
topic: "clr-integration"
description: "Express LocalDB instance APIs 07/14/2025 In the traditional, service-based SQL Server world, individual SQL Server instances installed on a single computer are p"
tags: ["clr-integration","instance-apis"]
pubDate: 2025-12-01
---

Express LocalDB instance APIs

In the traditional, service-based SQL Server world, individual SQL Server instances installed on a

single computer are physically separated. Each instance must be installed and removed

separately, has a separate set of binaries, and runs under a separate service process. The SQL

Server instance name is used to specify which SQL Server instance the user wants to connect

to.

The SQL Server Express LocalDB instance API uses a simplified, light instance model. Although

individual LocalDB instances are separated on the disk and in the registry, they use the same

set of shared LocalDB binaries. Moreover, LocalDB doesn't use services. LocalDB instances are

launched on demand through LocalDB instance API calls. In LocalDB, the instance name is used

to specify which of the LocalDB instances the user wants to work with.

A LocalDB instance is always owned by a single user and is visible and accessible only from this

user's context, unless instance sharing is enabled.

Although technically LocalDB instances aren't the same as traditional SQL Server instances,

their intended use is similar. They are called

instances

to emphasize this similarity and to make

them more intuitive to SQL Server users.

LocalDB supports two kinds of instances: automatic instances (AI) and named instances (NI).

The identifier for a LocalDB instance is the instance name.

Automatic LocalDB instances are

public

; they are created and managed automatically for the

user and can be used by any application. One automatic LocalDB instance exists for every

version of LocalDB that is installed on the user's computer.

Automatic LocalDB instances provide seamless instance management. The user doesn't need to

create the instance. This enables users to easily install applications and to migrate to different

computers. If the target computer has the specified version of LocalDB installed, the automatic

LocalDB instance for that version is also available on that computer.

A user doesn't need to create an automatic LocalDB instance. The instance is lazily created the

first time the instance is used, as long as the specified version of LocalDB is available on the

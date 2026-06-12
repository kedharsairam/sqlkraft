---
name: "sys.sp_script_synctran_commands"
title: "sp_script_synctran_commands"
category: "general"
description: "Generates a script that contains the calls to be applied at Subscribers for updatable subscriptions. There's one call for each article in the publication. The generated script also contains the table that is needed to process queued publications. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: "MSsubsciption_articles"
---

## Description

Generates a script that contains the calls to be applied at Subscribers for updatable subscriptions. There's one call for each article in the publication. The generated script also contains the table that is needed to process queued publications. This stored procedure is executed at the Publisher on the publication database.

## Syntax

`MSsubsciption_articles`

## Arguments

Creates triggers at the Subscriber used with all types of updatable subscriptions (immediate,

queued, and immediate updating with queued updating as failover). This stored procedure is

executed at the Subscriber on the subscription database.

procedure should be used instead of

generates a script that contains the

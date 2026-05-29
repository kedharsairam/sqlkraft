---
name: 'sys.conversation_endpoints'
title: 'sys.conversation_endpoints'
category: 'objects'
description: 'receive_sequence_frag'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
receive_sequence_frag

Next message fragment number expected in

message receive sequence. Not NULLABLE.

system_sequence

The sequence number of the last system message

for this dialog. Not NULLABLE.

first_out_of_order_sequence

The sequence number of the first message in the

out of order messages for this dialog. Not

NULLABLE.

last_out_of_order_sequence

The sequence number of the last message in the

out of order messages for this dialog. Not

NULLABLE.

last_out_of_order_frag

Sequence number of the last message in the out of

order fragments for this dialog. Not NULLABLE.

is_system

1 if this is a system dialog. Not NULLABLE.

priority

The conversation priority that is assigned to this

conversation endpoint. Not NULLABLE.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

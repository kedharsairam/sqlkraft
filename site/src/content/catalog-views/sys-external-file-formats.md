---
name: 'sys.external_file_formats'
title: 'sys.external_file_formats'
category: 'external'
description: 'serialization/deserialization'
tags: ["catalog-view", "external"]
pubDate: 2026-05-29
---

## Description
serialization/deserialization

method.

row_terminator

For format_type =

DELIMITEDTEXT, this is the

character string that

terminates each row in the

external Hadoop file.

Always '\n'.

encoding

For format_type =

DELIMITEDTEXT, this is the

encoding method for the

external Hadoop file.

Always 'UTF8'.

data_compression

The data compression

method for the external

data.

For format_type = DELIMITEDTEXT:

-

'org.apache.hadoop.io.compress.DefaultCodec'

- 'org.apache.hadoop.io.compress.GzipCodec'

For format_type = RCFILE:

-

'org.apache.hadoop.io.compress.DefaultCodec'

For format_type = ORC:

-

'org.apache.hadoop.io.compress.DefaultCodec'

-

'org.apache.hadoop.io.compress.SnappyCodec'

For format_type = PARQUET:

- 'org.apache.hadoop.io.compress.GzipCodec'

-

'org.apache.hadoop.io.compress.SnappyCodec'

The visibility of the metadata in catalog views is limited to securables that a user either owns or on

which the user has been granted some permission. For more information, see

Metadata Visibility

Configuration

.

See Also

sys.external_data_sources (Transact-SQL)

sys.external_tables (Transact-SQL)

CREATE EXTERNAL FILE FORMAT (Transact-SQL)

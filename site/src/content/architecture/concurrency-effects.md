---
title: "Concurrency effects"
topic: "query-processing"
description: "protecting all reads with locks. By using row versioning, the chance that a read operation"
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

protecting all reads with locks. By using row versioning, the chance that a read operation

blocks other transactions is greatly reduced.

Locking and row versioning prevent users from reading uncommitted data and prevent multiple

users from attempting to change the same data at the same time. Without locking or row

versioning, queries executed against that data could produce unexpected results by returning

data that hasn't yet been committed in the database.

Applications can choose transaction isolation levels, which define the level of protection for the

transaction from modifications made by other transactions. Table-level hints can be specified for

individual Transact-SQL statements to further tailor the behavior to fit the requirements of the

application.

Users who access a resource at the same time are said to be accessing the resource concurrently.

Concurrent data access requires mechanisms to prevent adverse effects when multiple users try

to modify resources that other users are actively using.

Users modifying data can affect other users who are reading or modifying the same data at the

same time. These users are said to be accessing the data concurrently. If a database has no

concurrency control, users could see the following side effects:

Lost updates occur when two or more transactions select the same row and then update the

row based on the value originally selected. Each transaction is unaware of the other

transactions. The last update overwrites updates made by the other transactions, which

results in lost data.

For example, two editors make an electronic copy of the same document. Each editor

changes the copy independently and then saves the changed copy thereby overwriting the

original document. The editor who saves the changed copy last overwrites the changes

made by the other editor. This problem could be avoided if one editor couldn't access the

file until the other editor had finished and committed the transaction.

## Inconsistent analysis (nonrepeatable read)

## Phantom reads

Uncommitted dependency occurs when a second transaction reads a row that's being

updated by another transaction. The second transaction is reading data that hasn't been

committed yet and might be changed by the transaction updating the row.

For example, an editor is making changes to an electronic document. During the changes, a

second editor takes a copy of the document that includes all the changes made so far, and

distributes the document to the intended audience. The first editor then decides the

changes made so far are wrong and removes the edits and saves the document. The

distributed document contains edits that no longer exist and should be treated as if they

never existed. This problem could be avoided if no one could read the changed document

until the first editor does the final save of modifications and commits the transaction.

Inconsistent analysis occurs when a second transaction accesses the same row several times

and reads different data each time. Inconsistent analysis is similar to uncommitted

dependency in that another transaction is changing the data that a second transaction is

reading. However, in inconsistent analysis, the data read by the second transaction was

committed by the transaction that made the change. Also, inconsistent analysis involves

multiple reads (two or more) of the same row, and each time the information is changed by

another transaction; thus, the term nonrepeatable read.

For example, an editor reads the same document twice, but between each reading the

writer rewrites the document. When the editor reads the document for the second time, it

has changed. The original read wasn't repeatable. This problem could be avoided if the

writer couldn't change the document until the editor has finished reading it for the last

time.

A phantom read is a situation that occurs when two identical queries are executed and the

set of rows returned by the second query is different. The following example shows how this

might occur. Assume the two transactions are executing at the same time. The two

statements in the first transaction might return different results because the

statement in the second transaction changes the data used by both.

## Missing and double reads caused by row updates

`SELECT`

`INSERT`

```sql
--Transaction 1
BEGIN
TRAN;
```

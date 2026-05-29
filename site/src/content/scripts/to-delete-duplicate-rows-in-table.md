---
name: 'To Delete Duplicate Rows in Table'
title: 'To Delete Duplicate Rows in Table'
description: 'method 1 = create and drop a table'
category: database
tags: ["database", "table"]
pubDate: 2025-03-15
---

```sql
--method 1 = create and drop a table
select distinct * from tablename
select distinct * into temptablename from tablename
truncate table tablename
delete from tablename
insert into tablename select * from temptablename
drop table temptablename

--method 2 = auto_id
alter table tablename
add auto_id int identity(1,1)
delete from tablename
where auto_id not in (select min(auto_id) from tablename group by name, id)
alter table tablename
drop column auto_id

--method 3 = CTE-common table expression
with empcte as
(select * , row_number() over(partition by id order by id) as rowno from tablename)
delete from empcte where rowno > 1
```

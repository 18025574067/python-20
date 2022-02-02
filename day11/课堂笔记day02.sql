--查询练习
	--查询所有字段
	--select * from 表名;
	select * from students;


	--查询指定字段
	--select 列1,列2,... from 表名;
	select id,name,age from students;


	--使用 as 给字段起别名
	--select 字段 as 名字 ...from 表名
	select id as "编号", name as "姓名" from students;
	select id "编号", name "姓名" from students;



	--select 表名，字段.... from 表名;
	select students.id, students.name from students;



	--可以通过 as 给表起别名
	--select 别名，字段.... from 表名 as 别名;
	select s.id, s.name from students as s;
	select s.id, s.gender from students as s;

	--失败的:   
	select students.name, students.age from students as s;



	--消除重复行（查性别）
	--distinct 字段



--条件查询
	--比较运算符
		--select .... from 表名 where ......
		-- >
		--查询大于18 岁的信息
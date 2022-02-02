-- sql强化演练（goods 表练习）

	-- 查询类型 cate_name 为 ‘超级本’ 的商品名称 name, 价格 price (where)
	select name, price from goods where cate_name = "超级本";

	-- 显示商品的种类
	-- 1）分组的方式（group by）
	select cate_name from goods group by cate_name;


	-- 2) 去重的方法（distinct）
	select distinct cate_name from goods;


	-- 求所有电脑产品的平均价格 avg, 并且保留两位小数（round）
	select round(avg(price), 2) "平均价格" from goods;


	-- 显示 每种类型 cate_name (由此可知需要分组) 的平均价格
	select cate_name, avg(price) from goods group by cate_name;


	-- 查询 每种类型 的商品中 最贵 max, 最便宜 min, 平均价 avg, 数量 count
	select cate_name, max(price), min(price), avg(price), count(*) from goods group by cate_name; 


	-- 查询所有价格大于 平均价格 的商品，并且按 价格降序 排序 order desc


	-- 1) 查询平均价格 avg(price)
	select avg(price) from goods;
	-- 2) 使用子查询
	select * from goods where price > (select avg(price) from goods) order by price desc;



	-- 查询每种类型中最贵的电脑的所有信息（难）

	-- 1 查找 每种类型 中 最贵的 max_price 价格
	select cate_name, max(price) from goods group by cate_name;

	-- 2 关联查询 inner join 每种类型 中最贵的物品信息
	-- select * from goods;
	-- inner join
	-- (select cate_name, max(price) as max_price from goods group by cate_name) as max_price_goods
	-- on goods,cate_name= max_price_goods.cate_name and goods.price= max_price_goods.max_price;
	select * from goods
	inner join
	(select cate_name,max(price) as max_price from goods group by cate_name) as max_price_goods 
	on goods.cate_name = max_price_goods.cate_name and goods.price = max_price_goods.max_price;


	-- 创建“商品分类”表
	-- 第一步  创建表 （商品种类表 goods_cates）
	create table if not exists goods_cates(
		id int unsigned primary key auto_increment,
		name varchar(40) not null
		);


	-- 第二步  同步 商品分类表 数据 将商品的所有 （种类信息）写入到（商品种类表）中
	-- 按照 分组 的方式查询 goods 表中的所有 种类（cate_name）
	select cate_name from goods group by cate_name;


	-- 通过子查询插入数据到新的分类表中
	insert into goods_brands(name) (select brand_name from goods group by brand_name);


	-- 第三步 同步 商品表 数据 通过 goods_cates 数据表来更新 goods 表
	-- 因为要通过 goods_cates 表 更新 goods 表 所以要把两个表连接起来（goods.cate_name = goods_cates.name）
	select * from goods inner join goods_cates on goods.cate_name = goods_cates.name;

	-- 把 商品表 goods 中的 cate_name 全部替换成 商品分类表中的 商品id(update (...)... set)
	update goods inner join goods_cates on goods.cate_name = goods_cates.name set goods.cate_name = goods_cates.id;


	-- 第四步 修改表结构
	-- 查看表结构(注意 两个表中的 外键类型需要一致)
	desc goods;
	+------------+------------------+------+-----+---------+----------------+
| Field      | Type             | Null | Key | Default | Extra          |
+------------+------------------+------+-----+---------+----------------+
| id         | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name       | varchar(150)     | NO   |     | NULL    |                |
| cate_name  | varchar(40)      | NO   |     | NULL    |                |
| brand_name | varchar(40)      | NO   |     | NULL    |                |
| price      | decimal(10,3)    | NO   |     | 0.000   |                |
| is_show    | bit(1)           | NO   |     | b'1'    |                |
| is_saleft  | bit(1)           | NO   |     | b'0'    |                |
+------------+------------------+------+-----+---------+----------------+
	
	-- 修改表结构（alter table) 字段名字不同 change, 把 cate_name 改为 cate_id int unsignes not null
	alter table goods change cate_name cate_id int unsigned not null;



	-- 创建 商品品牌表 goods_brands
	-- # 第一步 创建 “商品品牌表” 表
	-- 第一种方式 先创建表
	create table if not exists goods_brands(
		id int unsigned primary key auto_increment,
		name varchar(40) not null);

+-------+------------------+------+-----+---------+----------------+
| Field | Type             | Null | Key | Default | Extra          |
+-------+------------------+------+-----+---------+----------------+
| id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(40)      | NO   |     | NULL    |                |
+-------+------------------+------+-----+---------+----------------+


	-- 插入数据 brand_name(分组)
	-- 按照 分组的方式查询 goods表中的所有 种类 （brand_name）
	select brand_name from goods group by brand_name;



	-- (注意) 把查询出来的 结果 写入 goods_brands 表里去 （insert into）只插入name
	-- 第二种方式 创建表的同时插入数据(了解，不建议使用)
	insert into goods_brands(name) (select brand_name from goods group by brand_name);



	-- # 第二步 同步数据 
	-- 通过 goods_brands 数据表来更新 goods数据表 g.brand_name= b.id
	select * goods inner join goods_brands on goods.brand_name = goods_brands.name;
	update goods inner join goods_brands on goods.brand_name = goods_brands.name set goods.brand_name = goods_brands.id;


	-- # 第三步 修改表结构
	-- 通过 alter table 语句修改表结构 brand_id int unsignes not null
	alter table goods change brand_name brand_id int unsignes not null;





-- 外键的使用（了解）
+-----------+------------------+------+-----+---------+----------------+
| Field     | Type             | Null | Key | Default | Extra          |
+-----------+------------------+------+-----+---------+----------------+
| id        | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name      | varchar(150)     | NO   |     | NULL    |                |
| cate_id   | int(10) unsigned | NO   |     | NULL    |                |
| brand_id  | int(10) unsigned | NO   |     | NULL    |                |
| price     | decimal(10,3)    | NO   |     | 0.000   |                |
| is_show   | bit(1)           | NO   |     | b'1'    |                |
| is_saleft | bit(1)           | NO   |     | b'0'    |                |
+-----------+------------------+------+-----+---------+----------------+
	-- 向goods表里插入任意一条数据（name, cate_id, brand_id, price),cate_id的值为12
	insert into goods (name, cate_id, brand_id, price) values('LaserJet Pro P1606dn 黑白激光打印机', 12, 4, '1849')

	-- 查询所有商品的详细信息（通过左连接 将左表未显示数据添加到最终结果）
	select * from goods left join goods_cates on goods.cate_id = goods_cates.id;


	-- 约束 数据的插入使用外键 foreign key
	-- 添加外键：alter table 表名 add foreign key (外键字段) references 表名(主键id)
	alter table goods add foreign key(cate_id) references goods_cates(id);

	-- ERROR 1452 (23088): Cannot add or update a child row: a foreign key constraint fails
	-- ('jing_dong', '#sql=372_26', CONSTRAINT'goods_ibfk_1' FOREIGN KEY ('cate_id') REFERENCES 'goods_cates'('id'))
	-- 错误的原因是：数据库已经存在一条 不符合规则的数据了，需要先删除数据再重新添加外键
	-- 删除数据 cate_id = 12
	delete from goods where cate_id = 12;
	show create table goods


	-- 给 goods 表的brands_id 添加和 goods_brands 的 id 做外键关联
	alter table goods add foreign key(brand_id) references goods_brands(id);



	-- 创建表的同时设置外键（注意 goods_cates 和 goods_brands 两个表必须事先存在）
	-- 创建goods_test表，字段为（id, name, cates_id, brands_id）
	-- 其中 cate_id 外键关联 goods_cates 的id字段
	-- 其中 brand_id 外键关联 goods_brands 的id字段
	create table goods_test(
		id int primary key auto_increment,
		name varchar(150) not null,
		cate_id int unsigned not null,
		brand_id int unsigned not null,
		foreign key (cate_id) references goods_cates(id),
		foreign key (brand_id) references goods_brands(id)
		);


	-- 如何取消外键约束
	-- 需要先获取外键约束名称（常见格式为：表名_ibfk_数字，'goods_test_ibfk_1'）,
	-- 该名称系统会自动生成，可以通过查看表创建语句来获取名称
	-- 查看外键名
	show create table goods_test;


	-- 获取名称之后就可以根据名称来删除外键约束
	alter table goods_test drop foreign key goods_test_ibfk_1;





-- 什么是视图
	-- 通俗的讲，视图就是一条SELECT语句执行后返回的结果集
	-- 所以我们在创建视图的时候，主要的工作就落在创建这条SQL查询语句上.

-- 视图的特点
	-- 视图是对若干张基本表的引用，一张 表，查询语句执行的结果
	-- 不存储具体的数据（基本表数据发生了改变，视图也会跟着改变）

-- 视图的最主要的作用
	-- 如果数据库因为需求等原因发生了改变，为了保证查询出来的数据与之前相同
	-- 则需要在多个地方进行修改，维护起来非常麻烦，这个时候使用视图就可解决这个问题

	-- 视图的定义方式
	-- create view 视图名 as select ... ...

	-- 查出产品表中产品名称，分类名称以及对应品牌
	select goods.name gname, goods_cates.name gcname, goods_brands.name gbname from goods join goods_cates on goods.cate_id = goods_cates.id join goods_brands on goods.brand_id = goods_brands.id;

	-- 创建上述结果的视图 (v_goods_info)
	create view v_goods_info as select goods.name gname, goods_cates.name gcname, goods_brands.name gbname from goods join goods_cates on goods.cate_id = goods_cates.id join goods_brands on goods.brand_id = goods_brands.id;


	-- 查看所有表或视图
	show tables;
	select * from v_goods_info;


	-- 当原表产品名称改变后，会影响视图 (视图是虚拟表)
	update goods set name="xxx" where id = 24;
	select * from v_goods_info where gname="xxx";

	-- 删除视图
	-- drop view 视图名;
	drop view v_goods_info;


	-- 注意
		-- 视图只能进行搜索；

-- 视图作用总结
	
	-- 1 提高了重用性，就像一个函数
	-- 2 对数据库重构，却不影响已经编写好的程序运行
	-- 3 提高了安全性能，可以对不同的用户
	-- 4 让数据更加清晰

-- 视图最主要解决的问题
	-- 程序对数据库操作，一旦数据库发生变化，程序需要修改，这时如果使用视图就可以解决这个问题




-- 事物（ACID）
	基本使用：
	1. begin
	2. 操作 insert update delete
	3. 确认修改 commit
	4. 反悔 rollback;

	-- 原子性 一致性
		第一步 打开 终端1 终端2
		第二步 终端1 打开事物 begin
			终端1 update 表名 set 字段="xxx" where ...;
			终端2 select * from 表名; 发现数据改变
		第三步 终端2 select * from 表名;
			发现数据其实并没有改变 其实这个时候对数据的相关操作信息存在缓存中，
			当count之后，这些操作才会一次性的完成
		第四步 终端1 commit 数据数数据真的改变
			终端2 select * from 表名，数据改变了

	-- 隔离性
		第一步 打开 终端1 终端2
		第二步 终端1 打开事物 begin
			终端1 update 表名 set 字段="xxx" where ...;
		第三步 终端2 update 表名 set 字段="yyy" where ...;
			发现 处于阻塞状态
		第四步 终端1 commit
			终端2 阻塞状态解除 数据修改成 yyy

	-- 回滚（rollback）
		第一步 打开 终端1 begin
		第二步 终端1 update 表名 set 字段="xxx" where ...;
		第三步 rollback 数据返回最开始的原始值


	-- 持久性
		-- 一旦事务提交，则其所做的修改会永久保存到数据库

	-- 注意
		-- innodb 能使用事物
		-- 使用python操作数据库的时候 默认开启事物的
		-- 但是python对数据库运行增删改的时候 需要手动commit

		-- 使用终端操作数据库（也就是mysql的客户端）的时候，也是默认开始事物的
		-- 只是在回车确认操作的时候 终端会默认的commit 所以我们不需要commit




-- 创建客户表
create table customer(
	id int unsigned auto_increment primary key not null,
	name varchar(30) not null,
	addr varchar(100),
	tel varchar(11) not null);

-- 创建订单表
create table orders(
	id int unsigned auto_increment primary key not null,
	order_date_time datetime not null,
	customer_id int unsigned,
	foreign key(customer_id) references customer(id)
);

-- 创建订单详情
create table order_detail(
	id int unsigned auto_increment primary key not null,
	order_id int unsigned not null,
	goods_id int unsigned not null,
	quantity tinyint unsigned not null,
	foreign key(order_id) references orders(id),
	foreign key(goods_id) references goods(id)
);
























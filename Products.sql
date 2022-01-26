create database sepsales;

create table products (
prod_id       bigint,
prod_name     varchar(100),
prod_category varchar(100),
unit_price    decimal,
primary key(prod_id));

insert into products (prod_id, prod_name, prod_category, unit_price) values (1,'fan','Home Goods',30.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (2,'table','Home Goods',30.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (3,'chair','Home Goods',50.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (4,'wire','Home Goods',5.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (5,'cloth','Home Goods',5.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (6,'cell phone','Electronics',500.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (7,'laptop','Electronics',1000.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (8,'TV','Electronics',1000.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (9,'washer','Electronics',2000.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (10,'dryer','Electronics',2000.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (11,'apple','Fruits and Vegis',1.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (12,'tomato','Fruits and Vegis',1.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (13,'chilli','Fruits and Vegis',1.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (14,'onion','Fruits and Vegis',1.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (15,'potato','Fruits and Vegis',2.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (16,'kale','Fruits and Vegis',1.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (17,'spinach','Fruits and Vegis',1.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (18,'kiwi','Fruits and Vegis',2.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (19,'bathroom cleaner','Cleaning',3.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (20,'dishwasher','Cleaning',3.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (21,'handsoap','Cleaning',3.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (22,'soap','Cleaning',4.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (23,'paper','Office Supplies',5.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (24,'pens','Office Supplies',1.00);
insert into products (prod_id, prod_name, prod_category, unit_price) values (25,'ink','Office Supplies',1.00);

commit;
select * from products;

create table BillHeader(
bill_id bigint,
store_id bigint,
bill_date datetime,
bill_total decimal,
Primary key(bill_id)
);

create table BillDetail(
billDetail_id varchar(100),
bill_id bigint,
prod_id bigint,
quantity decimal,
line_total decimal,
Primary key(billDetail_id),
foreign key(bill_id) references BillHeader(bill_id),
foreign key(prod_id) references products(prod_id)
);

select * from BillDetail;
select * from BillHeader;

delete from BillDetails where prod_id=6;
delete from BillHeader where bill_id = 20211109191921;

insert into BillHeader values(20211109191921,1,STR_TO_DATE("20110411000000","%Y%m%d%H%i%S"),10077);
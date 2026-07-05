-- use pproject;
/* creating the customers table */
/*
create table if not exists customers (
id int auto_increment primary key,
first_name varchar(50),
last_name varchar(50),
age int,
gender enum('Male', 'Female', 'Other'),
region varchar(100),
country varchar(100),
created_at timestamp default current_timestamp
);
*/

-- select region, country, count(*) from customers
-- group by region, country order by region;


-- insert into customers (first_name, last_name, age, gender, region, country) values('Test6', 'test1', 34, 'Male', 'Asia', 'Turkey');
/*select region, gender, count(*) from customers
group by region, gender order by region asc;
*/

/*
create table if not exists partners (
id int auto_increment primary key,
partner_name varchar(100),
country varchar(100),
region varchar(100),
shipments_count int,
average_delivery_days decimal(4, 1),
cost_per_shipment decimal(8, 2),
status enum('Active', 'Inactive'),
rating decimal(3, 1),
contract_start date,
created_at timestamp default current_timestamp 
);
*/

-- select count(*) from customers;



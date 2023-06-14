select product_name, manufacturer, price from smartphone where product_count>2;

select * from smartphone where manufacturer='Samsung';

select * from smartphone where product_name like "%iPhone%";

select * from smartphone where product_name like "%Samsung%";

select * from smartphone where product_name regexp '[:xdigit:]';

select * from smartphone where product_name like "%8%";
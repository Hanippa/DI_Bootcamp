CREATE TABLE house_expenses(
id serial primary key,
pay_date date,
electricity float,
water float,
paid_by varChar(10)
);

INSERT INTO house_expenses(pay_date,electricity,water,paid_by)
VALUES ('01-01-2023' , 87.52 , 83.2 , 'Valery'),
('01-01-2023' , 13.34 , 23.2 , 'Tricia'),
('01-01-2023' , 653.34 , 433.2 , 'Mable');

SELECT max(water) as max_paid,min(water) as mid_paid ,avg(electricity) FROM public.house_expenses where paid_by != 'mable'
SELECT paid_by , SUM(electricity) + SUM(water),max(water + electricity) from house_expenses group by paid_by
UPDATE house_expenses SET paid_by = 'Mable' WHERE id = 1;
UPDATE house_expenses SET electricity = 0 WHERE paid_by = 'Mable';
SELECT * FROM house_expenses;
DELETE FROM house_expenses WHERE electricity < 50;
DELETE FROM house_expenses WHERE date > '2019-06-06';
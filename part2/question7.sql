/*Gives the total amount each customer has spent (non-present customers are assummed to have spent 0)*/
/*We cannot update this view because - among many reasons - views that do not select
from a single table or view are not automatically updatable.*/
create view perCustomerRevenue as
SELECT c.memberno, c.firstName, c.lastName, o.grandtotal
FROM customers c
JOIN (
    SELECT memberno, SUM(total) AS grandtotal
    FROM orders GROUP BY memberno
) o ON o.memberno = c.memberno;

/*Shows "large" (greater than $200) orders*/
/*We can update this view because it only uses one table so the update commands will map easily
to this table*/
create view largeTransactions as
SELECT *
FROM orders
WHERE total > 200;

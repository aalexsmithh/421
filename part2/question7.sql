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


/* From w3resource.com, the conditions for updating a view are:
1. The view is defined based on one and only one table.

2. The view must include the PRIMARY KEY of the table based upon which the view has been created.

3. The view should not have any field made out of aggregate functions.

4. The view must not have any DISTINCT clause in its definition.

5. The view must not have any GROUP BY or HAVING clause in its definition.

6. The view must not have any SUBQUERIES in its definitions.

7. If the view you want to update is based upon another view, the later should be updatable.

8. Any of the selected output fields (of the view) must not use constants, strings or value expressions.
*/

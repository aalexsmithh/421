/* extend all coupons that have expired in the last 7 days by an additional 7 days from their original start date  */

UPDATE coupons SET enddate = enddate + 7 WHERE enddate BETWEEN current_date - 7 AND current_date;

/* give a $0.50 wage increase to all cashiers */

UPDATE shifts SET wage = wage + .5 WHERE employeeID IN (SELECT employeeID FROM cashiers);

/* give a $5 instant rebate on any order that is more than $200 */

UPDATE orders SET total = total - 5 WHERE total > 200;

/* each delivery drivers receives a 10% tip for gas a day after any given shift */

INSERT INTO shifts 
(SELECT shiftdate+1, employeeid, TRUNC(wage/10), managerid FROM shifts WHERE employeeid IN (SELECT * FROM deliverydrivers));

/*all purchases on the given date*/
SELECT amount
FROM transactions
WHERE amount>0 AND transactionDate='2018-03-01';

/*membership numbers of customers who have bought at least 1 Rice Bran Gluten Free Mini Baguette in a single order*/
SELECT O.memberNo
FROM orders O, ordercontents C
WHERE O.orderNo = C.orderNo AND C.pName='Rice Bran Gluten Free Mini Baguette' AND C.quantity>=1;

/*the licenses of all delivery vehicle used while a certain manager ID 1296 was active*/
SELECT DV.licenseNo
FROM deliveryvehicles DV, shifts S
WHERE S.managerID='1296' AND S.employeeID=DV.currentdriverID;

/*all the addresses that driver ID 1271 has delivered to*/
SELECT c.address
FROM customers C, orders O
WHERE C.memberNo = O.orderNo AND O.driverID='1271';

/*all the names of items customers with first name Emily have bought with a coupon */
SELECT C.pName
FROM (
	SELECT O.orderNo
	FROM orders O, customers C
	WHERE O.memberNo = C.memberNo AND C.firstName='Emily'
	) O, coupons C, couponRedeems CR
WHERE O.orderNo = CR.orderNo AND CR.couponCode = C.couponCode;
COPY items(name, price)
FROM 'csv/items.csv' DELIMITER ',' CSV;

COPY customers(memberNo, firstName, lastName, address, expiry)
FROM 'csv/customers.csv' DELIMITER ',' CSV;

COPY coupons(couponCode, pName, discountPct, startDate, endDate)
FROM 'csv/coupons.csv' DELIMITER ',' CSV;

COPY employees(employeeID, firstName, lastName)
FROM 'csv/employees.csv' DELIMITER ',' CSV;

COPY managers(employeeID)
FROM 'csv/managers.csv' DELIMITER ',' CSV;

COPY cashiers(employeeID)
FROM 'csv/cashiers.csv' DELIMITER ',' CSV;

COPY deliverydrivers(employeeID)
FROM 'csv/deliverydrivers.csv' DELIMITER ',' CSV;

COPY orders(orderNo, memberNo, total, toBeDelivered, driverID)
FROM 'csv/orders.csv' DELIMITER ',' CSV;

COPY ordercontents(orderNo, pName, quantity)
FROM 'csv/ordercontents.csv' DELIMITER ',' CSV;

COPY couponRedeems(couponCode, orderNo)
FROM 'csv/couponRedeems.csv' DELIMITER ',' CSV;

COPY transactions(transactionID, amount, transactionDate, cashierID)
FROM 'csv/transactions.csv' DELIMITER ',' CSV;

COPY shifts(shiftDate, employeeID, wage, managerID)
FROM 'csv/shifts.csv' DELIMITER ',' CSV;

COPY deliveryvehicles(licenseNo, currentdriverID)
FROM 'csv/deliveryvehicles.csv' DELIMITER ',' CSV;
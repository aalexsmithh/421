create table items(name text NOT NULL PRIMARY KEY, price real NOT NULL);

create table customers(memberNo int NOT NULL PRIMARY KEY, firstName text NOT NULL, lastName text NOT NULL, address text NOT NULL, expiry date NOT NULL);

create table coupons(couponCode int NOT NULL PRIMARY KEY, pName text NOT NULL, discountPct int NOT NULL, startDate date NOT NULL, endDate date NOT NULL, FOREIGN KEY(pName) REFERENCES items(name));

create table employees(employeeID int NOT NULL PRIMARY KEY, firstName text NOT NULL, lastName text NOT NULL);

create table managers(employeeID int NOT NULL PRIMARY KEY, FOREIGN KEY(employeeID) REFERENCES employees(employeeID));

create table cashiers(employeeID int NOT NULL PRIMARY KEY, FOREIGN KEY(employeeID) REFERENCES employees(employeeID));

create table deliverydrivers(employeeID int NOT NULL PRIMARY KEY, FOREIGN KEY(employeeID) REFERENCES employees(employeeID));

create table orders(orderNo int NOT NULL PRIMARY KEY, memberNo int NOT NULL, total real NOT NULL, toBeDelivered boolean, driverID int, FOREIGN KEY(memberNo) REFERENCES customers(memberNo), FOREIGN KEY(driverID) REFERENCES deliverydrivers(employeeID));

create table ordercontents(orderNo int NOT NULL, pName text NOT NULL, quantity int NOT NULL, FOREIGN KEY(orderNo) REFERENCES orders(orderNo), FOREIGN KEY(pName) REFERENCES items(name), PRIMARY KEY(orderNo, pName));

create table couponRedeems(couponCode int NOT NULL, orderNo int NOT NULL, FOREIGN KEY(couponCode) REFERENCES coupons(couponCode), FOREIGN KEY(orderNo) REFERENCES orders(orderNo), PRIMARY KEY (couponCode, orderNo));

create table transactions(transactionID int NOT NULL PRIMARY KEY, amount real NOT NULL, transactionDate date NOT NULL, cashierID int, FOREIGN KEY(cashierID) REFERENCES cashiers(employeeID));

create table shifts(shiftDate date NOT NULL, employeeID int NOT NULL, wageID int NOT NULL, managerID int NOT NULL, FOREIGN KEY(employeeID) REFERENCES employees(employeeID), FOREIGN KEY(wageID) REFERENCES transactions(transactionID), FOREIGN KEY(managerID) REFERENCES managers(employeeID), PRIMARY KEY(shiftDate, employeeID));

create table deliveryvehicles(licenseNo char(7) NOT NULL PRIMARY KEY, currentdriverID int NOT NULL, FOREIGN KEY(currentDriverID) REFERENCES deliverydrivers(employeeID));
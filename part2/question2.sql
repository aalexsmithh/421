create table items(name text PRIMARY KEY, price real);

create table customers(memberNo int PRIMARY KEY, firstName text lastName text, address text, expiry date);

create table coupons(couponCode, pName, discountPct int, startDate date, endDate date);

create table orders(orderNo int PRIMARY KEY, total real, toBeDelivered boolean);

create table employees(employeeID int PRIMARY KEY, firstName text, lastName text);

create table transactions(transactionID int PRIMARY KEY, amount real, transactionDate date);

create table shifts(shiftDate date, employeeID int, wage real, hours real);

create table deliveryvehicles(licenseNo char(7) PRIMARY KEY);
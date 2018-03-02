create table coupons(couponCode int NOT NULL PRIMARY KEY,
	pName text NOT NULL,
	discountPct int NOT NULL CHECK (discountPct % 5 = 0),
	startDate date NOT NULL,
	endDate date NOT NULL,
	FOREIGN KEY(pName) REFERENCES items(name));

-- All discounts must be a multiple of 5. No 42% off, only 45%

create table ordercontents(
	orderNo int NOT NULL,
 	pName text NOT NULL,
 	quantity int NOT NULL CHECK (quantity > 0),
 	FOREIGN KEY(orderNo) REFERENCES orders(orderNo),
 	FOREIGN KEY(pName) REFERENCES items(name),
 	PRIMARY KEY(orderNo,pName)
 	);

-- You must add at least one of an item to an order

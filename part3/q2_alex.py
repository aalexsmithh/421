import psycopg2

def add_order():
	'''
	orderNo int
	memberNo int
	total real
	toBeDelivered boolean,
	driverID int,
	FOREIGN KEY(memberNo) REFERENCES customers(memberNo),
	FOREIGN KEY(driverID) REFERENCES deliverydrivers(employeeID)
	);
	'''

	# get latest order no from db?
	

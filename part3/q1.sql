/*counts all records in all table
run from psql prompt*/
create or replace function total_count() returns int as $$
begin
	return 
	(select count(*) from items)
	+
	(select count(*) from customers)
	+
	(select count(*) from coupons)
	+
	(select count(*) from employees)
	+
	(select count(*) from managers)
	+
	(select count(*) from cashiers)
	+
	(select count(*) from deliverydrivers)
	+
	(select count(*) from orders)
	+
	(select count(*) from ordercontents)
	+
	(select count(*) from couponRedeems)
	+
	(select count(*) from transactions)
	+
	(select count(*) from shifts)
	+
	(select count(*) from deliveryvehicles);
end;
$$ language plpgsql;
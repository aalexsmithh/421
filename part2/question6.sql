/* delete all expired coupons from the coupon table*/

DELETE FROM coupons WHERE enddate < current_date;

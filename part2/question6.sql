/* delete all expired coupons from the coupon table*/

DELETE FROM couponredeems where couponcode IN (SELECT couponcode FROM coupons WHERE enddate < current_date);
DELETE FROM coupons WHERE enddate < current_date;

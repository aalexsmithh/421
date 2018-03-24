/* This index would be used to create a flyer containing all of the feature items that are currently on sale. 
Say for example, all the items that have more than 40% off*/

CREATE INDEX flyer ON coupons (pName, discountpct);

/* This index would be used to calculate how much profit the store made on a given date. It could also be used 
to calculate profit for a given time of year (range of dates) */

CREATE INDEX profit ON transactions (transactiondate);

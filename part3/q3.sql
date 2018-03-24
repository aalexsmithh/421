/* This index would be used to create a flyer containing all of the feature items that are currently on sale. 
Say for example, all the items that have more than 40% off*/

CREATE index flyer ON coupons (pName, discountpct);

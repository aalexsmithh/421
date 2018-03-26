/* This trigger will be used to track all the membership renewals of customers. Each time a customer renews their membership, an entry
will be made in the renewals table */

CREATE TABLE renewals (
memberNo int NOT NULL, 
renewdate date NOT NULL, 
FOREIGN KEY (memberNo) REFERENCES customers(memberNo), 
PRIMARY KEY (memberNo, renewdate)
);

CREATE OR REPLACE FUNCTION renewals() 
RETURNS trigger AS $trig$ 
BEGIN 
INSERT INTO renewals VALUES (NEW.memberNo, current_date); 
RETURN NEW; 
END; 
$trig$ language plpgsql;

CREATE TRIGGER renew 
BEFORE UPDATE 
ON customers 
FOR EACH ROW EXECUTE PROCEDURE renewals();

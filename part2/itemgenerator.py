import numpy as np

def generateitems(items):
	for item in items:
		price = np.random.normal(10, 8, 1)
		if price < 0:
			price = price - 2 * price

		price = np.around(price, 2)[0]

		print 'insert into items values ("%s", %s);' % (item, price)

items = ["Riceland American Jazmine Rice","Caress Velvet Bliss Ultra Silkening Beauty Bar - 6 Ct","Earth's Best Organic Fruit Yogurt Smoothie Mixed Berry","Boar's Head Sliced White American Cheese - 120 Ct","Back To Nature Gluten Free White Cheddar Rice Thin Crackers","Sally Hansen Nail Color Magnetic 903 Silver Elements","Twinings Of London Classics Lady Grey Tea - 20 Ct","Lea & Perrins Marinade In-a-bag Cracked Peppercorn","Van De Kamp's Fillets Beer Battered - 10 Ct","Ahold Cocoa Almonds","Honest Tea Peach White Tea","Mueller Sport Care Basic Support Level Medium Elastic Knee Support","Garnier Nutritioniste Moisture Rescue Fresh Cleansing Foam","Pamprin Maximum Strength Multi-symptom Menstrual Pain Relief","Suave Naturals Moisturizing Body Wash Creamy Tropical Coconut","Burt's Bees Daily Moisturizing Cream Sensitive","Ducal Refried Red Beans","Scotch Removable Clear Mounting Squares - 35 Ct","Careone Family Comb Set - 8 Ct","Plums Black","Doctor's Best Best Curcumin C3 Complex 1000mg Tablets - 120 Ct","Betty Crocker Twin Pack Real Potatoes Scalloped 2 Pouches For 2 Meals - 2 Pk","Reese Mandarin Oranges Segments In Light Syrup","Smart Living Charcoal Lighter Fluid","Hood Latte Iced Coffee Drink Vanilla Latte","Triaminic Syrup Night Time Cold & Cough Grape 4oz","Morton Kosher Salt Coarse","Guava","Heinz Tomato Ketchup - 2 Ct","Petmate Booda Bones Steak, Bacon & Chicken Flavors - 9 Ct","Zhena's Gypsy Tea Herbal Red Tea Sachets Fire Light Chai - 22 Ct","Barefoot Pinot Grigio  187","Tomy The First Years Gumdrop Orthodontic Pacifiers 6m+ - 2ct","Halls Menthol Cough Suppresant/oral Anesthetic Drops Honey-lemon - 30 Ct","Nature's Way Forskohlii - 60 Ct","Rice Bran Gluten Free Dinner Rolls Plain","Nakano Seasoned Rice Vinegar Original","Sundown Naturals Essential Electrolytes Tropical Punch, Watermelon And Fruit Punch Gummies - 60 Ct","Munchies Sandwich Crackers Cheddar Cheese On Golden Toast Crackers - 8 Pk","Amy's Light & Lean Spaghetti Italiano","P.f. Chang's Home Menu Meal For Two Beef With Broccoli","Mom's Best Naturals Cereal Toasted Cinnamon Squares","Ferrara Vanilla Syrup","Elmer's Board Mate Dual Tip Glue Pen","Kellogg's Disney Pixar Cars 2 Cereal","Pizza Sauce","Bear Naked Fit Almond Crisp 100% Natural Energy Cereal","Dove Men + Care Antiperspirant Deodorant Cool Silver","Easy-off Oven Cleaner Lemon Scent","Choice Organic Teas Black Tea Classic Black - 16 Ct","Careone Lubricating Jelly","Sacla Italia Sun Dried Pesto Sauce","Huggies Natural Care Wipes - 3 Pk","Serpis Green Olives Stuffed With Spicy Chorizo","Ripken Power Shred Beef Jerky Teriyaki","Arnold Bread Jewish Rye Everything","Traditional Medicinals Herbal Tea Bags Just For Kids Organic Nighty Night - 18 Ct","Perry's Ice Cream Panda Paws","Black Swan Shiraz Merlot 1.5","Maty's All Natural Kids 1+ Caramel Banana Taste Cough Syrup","Kraft Anything Dressing Honey Mustard","Eight O'clock Coffee Dark Italian Roast Ground","Ahold  Honey Mustard","Enzymatic Therapy  Acidophilus Pearls Active Cultures Dietary Supplement - 30 Ct","Ahold Complete Buttermilk Pancake & Waffle Mix","Salsa Habanero","Say-it Sandwich & Snack Bags- 60 Pk","Hillshire Farm Deli Select Smoked Ham With Water Added Ultra Thin","Nestle Coffee-mate Fat Free Hazelnut Flavor Coffee Creamer","Careone Cotton Swabs","1-day Vaginal Antifungal Prefilled Applicator 1-dose Treatment","Preparation H Hemorrhoidal Ointment","Roth Kase Mini Cheeseboard Kit Havarti, Gruyere & Pepper Jack - 3 Ct","Firm Grip Disposable Nitrile Gloves - 10 Gloves","Downy Ultra Infusions Orchid Allure Fabric Softener - 48 Loads","Hostess Mini Muffins Chocolate Chip - 20 Ct","Gerber Graduates For Toddlers Lil' Meals Pasta Shells & Cheese","Powerbar Protein Plus High Protein Bar Vanilla Yogurt","Every Man Jack Shave Cream","Ahold Premium Paper Towels Giant Rolls - 8 Ct","Piacci Parmesan Nuggets","Organix Smoothing Shea Butter Conditioner","Dr. Scholl's For Her Rub Relief Strips","Guida's Whole Milk","Hime Wasabi Powdered Sushi","Boneless Pork Shoulder Roast","Boneless Pork Shoulder Roast","Ahold Simply Enjoy Gourmet Spread Smoky Fig & Roasted Garlic","Cuisinart Citrus Juicer Pulp Control","Velveeta Cheese","Lotrimin Ultra Antifungal Athlete's Foot Cream","Pasta Lensi Gigli #253","Cherrybrook Kitchen D.w. Sugar Cookie Mix","Herb Pharm Black Elderberry Herbal Glycerite Extract","Gold Bond Medicated Cornstarch Plus Baby Powder","General Mills Sweet 'n Salty Honey Nut Chex Mix","Udi's Soft N' Chewy Granola Bars Chocolate Chip - 5 Ct","Smoked Pork Hocks - 4 Ct","Kelapo Extra Virgin Coconut Oil Baking Sticks","Margaret Holmes Peanut Patch Green Boiled Peanuts Hot & Spicy","Kraft Velveeta Shells & Cheese 2% Milk","Sylvania Daylight 75 Watt Indoor Light Bulb","Sushi Chef Wakame Soup Mix Traditional Japanese Style","Campbell's Homestyle Soup Italian-style Wedding","Sapore Sensuale Cake Toasted Almond","Goody Ouchless No Metal Elastics - 29 Ct","Ahold Cooked Shrimp Large Tail-on","Smart Living 10.5in X 8in", "3 Subject Notebook College Ruled","Playtex Plastic Tampons Gentle Glide 360 Multi-pack Regular/super Fresh Scent - 18 Ct","Hershey's Caramel Syrup","Windex Original Glass & Surface Wipes - 28 Pk","Olay Total Effects 7-in-1 Tone Correcting Eye Treatment 0.5 Fl Oz","Alberto Vo5 Normal Balancing Shampoo","Milani Total Lash Cover Mascara 105 Black","Sylvia's Restaurant Specially-seasoned Field Peas With Snaps","Nabisco Wheat Thins Snacks","Careone Whitening Toothbrush Soft","Vaseline Spray & Go Moisturizer Total Moisture","Nature Made Fish Oil 1200mg Omega-3 360mg Liquid Softgels Lemon Flavor - 60 Ct","Belluci Extra Virgin Olive Oil 100% Italian","Ruffles Sour Cream & Onion Potato Chips","Turkey Hill Premium Ice Cream Party Cake","Tums Freshers Antacid Spearmint - 2 Pk","Manishchewitz Gluten Free Wide Egg Noodles","Gillette Fusion Proglide Cartridges - 8 Ct","Bakery Pistachio Muffin - 4 Ct","Frigo Cheese Heads 100% Natural str Cheese Light - 12 Ct","Similac Advance Infant Formula With Iron Milk-based/ready To Feed - 6 Ct","Rice A Roni Chicken Flavor Lower Sodium Rice","Oberweis Dairy Raspberry Lemonade","Companion Dog Biscuits Senior","Coco Lite Multigrain Pop Cakes Whole Wheat","Nestle The Original Coffee Mate","Sweetleaf Natural Stevia Sweetener Packets - 70 Ct","Pamela's Chocolate Cake Mix","Designer Gift Bag Glitterwrap","Ahold 5 Cheese Pizza Ready To Bake","Rice Bran Gluten Free Mini Baguette","Cracker Jack Popcorn Butter Toffee","Swingline Standard Desk Stapler Bonus Pack!","Pork Chops Bone-in Center Cut","Pork Chops Bone-in Center Cut","Snack Pack Tapioca Pudding - 4 Pk","Pure Power Easy Grip Scrub Brush","Cocktail Rx Frozen Cocktails Blue Hawaiian","Anagram Foil Balloon 18in Happy Birthday Smiles","Shelton's Turkey Burgers - 3 Ct","Buckler Non-alcoholic Malt Beverage - 6 Ct","Cento All Purpose Crushed Tomatoes","Careone Vitamin B12 500mcg Tablets - 100 Ct","Earth Balance Natural Peanut Butter And Flaxseed Creamy","Looza Mango Juice Drink","Campbell's Go Soup Coconut Curry With Chicken & Shitake Mushrooms","Sweet Baby Ray's Barbecue Sauce","Renuzit Gel Air Freshener Original","Uncle Ben's Roasted Garlic Ready Whole Grain Rice Medley","Howe Gummi Sour Brites","Nabisco Ritz Bits Cheese Cracker Sandwiches","Alessi Balsamic Reduction Traditional Balsamic","Allegra Allergy 12 Hour Relief Tablets - 12 Ct","Reynolds Staybrite Baking Cups Flowers - 36 Ct","Mccormick Grill Mates Brown Sugar Bourbon Marinade","Ahold Cocoa Magic Cereal","Cocktail Rx Frozen Cocktail Cosmopolitan","Earth Balance Natural Buttery Spread Soy Free","T.g.i Friday's Poppers Cream Cheese Stuffed Jalapenos","Instant Krazy Glue - 4 Ct","Pepperidge Farm Puff Pastry Turnovers Apple - 4 Ct","Campbell's Soup On The Go Chicken & Star Shaped Pasta Soup","Hi-c Boppin' Strawberry Fruit Juice Boxes- 10 Pk","Werther's Original Sugar Free Hard Candies","Cesar Canine Cuisine Filet Mignon Flavor","Freshpet Chilly Wags Natural Vanilla Flavor Frozen Treats For Dogs - 4 Ct","Boston Market Spaghetti With Meatballs","Osem Soup & Seasoning Mix Consomme","Smart Living Assorted Binder Clips - 10 Ct","Golden Krust Jamaican Style Spicy Beef Patties - 2 Ct","Eden Organic Shelled & Dry Roasted Pistachios","Mccormick Grill Mates Mesquite Marinade","Urban Accents Fisherman's Wharf Seafood Seasoning","Tastykake Cream Filled Koffee Kake Cupcakes Family Pack - 12 Ct","Kikkoman Soy Sauce","International Delight Coffee Creamer Irish Cream","Ahold Honey Ham - Water Added","Ahold Fitness Grape Creatine","Premier Protein Crisp Crunchy Protein Bar Peanut Butter Caramel - 6 Ct","Whitmor Stacking Shelf White Grid Medium","Fruit Gushers Fruit Flavored Snacks Value Pack - 12 Ct","Suave Naturals Everlasting Sunshine Shampoo","Hot Pockets Sandwiches Cheeseburgers - 4 Ct","Turkey Hill Premium Ice Cream Getrude Hawk Chocolates Box Of Chocolates","Currant Affair Black Currant Cranberry Juice","Spectrum Essentials Prenatal Dha Softgels - 60 Ct","Lundberg Risotto Butternut Squash","Twin Dragon Cookies Almond Chinese Style","Gerber Multigrain Cereal","Pure Protein Soft Baked Protein Bar Double Double Chocolate Vanilla Crunch","Burt's Bees Green Tea & Lemongrass Hand Soap","Rice Select Royal Blend Whole Grain","Weight Watchers Smart Ones Smart Delights Strawberry Shortcake - 4 Ct"]

def generatecustomers():
	lastnames = ["Smith","Murphy","Lam","Martin","Roy","Tremblay","Lee","Gagnon","Wilson","Diaz","Mora","Rodriguez","Gonzalez","Hernandez","Morales","Williams","Brown","Jones","Miller","Davis","Ortiz","Jenkins","Gutierrez","Perry","Butler"]
	firstnames = ["Liam","Jackson","Logan","Lucas","Noah","Ethan","Jack","William","Jacob","James","Thomas","Felix","Nathan","Samuel","Alexis","Emma","Olivia","Sophia","Zoe","Emily","Avery","Isabella","Charlotte","Lily","Ava","Lea","Alice","Florence","Zoe","Chloe","Beatrice","Rosalie"]
	
	streets = ["De Lorimier Avenue","Drummond Street","Guy Street","Honore Beaugrand Street","Lacordaire Boulevard","Langelier Boulevard","Louis-Hippolyte-Lafontaine Boulevard","MacKay Street","Mansfield Street","McGill College Avenue","McGill Street","Metcalfe Street","Montcalm Street","Mountain Street","Panet Street","Papineau Avenue","Park Avenue","Peel Street","Pie-IX Boulevard","Plessis Street","Saint Andre Street","Saint Denis Street","Saint Hubert Street","Saint Laurent Boulevard","Saint Michel Boulevard","Saint Timothee Street","Saint Urbain Street","Sanguinet Street","Stanley Street"]
	i = 1001

	for j in range(50):
		ln = np.random.choice(lastnames)
		fn1,fn2 = np.random.choice(firstnames, size=(2), replace=False)

		address = str(np.random.randint(10,1000)) + " " + np.random.choice(streets) + ", Montreal"
		expiry = np.datetime64("2018-03-01") + np.random.choice(np.arange(0, 450))
		expiry = str(expiry)[:10]

		memberno1 = str(i)
		i += 1
		memberno2 = str(i)
		i += 1

		print 'insert into customers values (%s, "%s", "%s", "%s", %s);' % (memberno1, fn1, ln, address, expiry)
		print 'insert into customers values (%s, "%s", "%s", "%s", %s);' % (memberno2, fn2, ln, address, expiry)

def generateorders():
	for i in range(150):
		total = np.random.normal(75, 50, 1)
		if total < 0:
			total = total - 2 * total

		total = str(np.around(total, 2)[0])

		tbd = str(np.random.choice([True,False]))

		print 'insert into orders values (%s, %s, %s)' % (str(i), total, tbd)

def generateemployees():
	lastnames = ["Smith","Murphy","Lam","Martin","Roy","Tremblay","Lee","Gagnon","Wilson","Diaz","Mora","Rodriguez","Gonzalez","Hernandez","Morales","Williams","Brown","Jones","Miller","Davis","Ortiz","Jenkins","Gutierrez","Perry","Butler"]
	firstnames = ["Liam","Jackson","Logan","Lucas","Noah","Ethan","Jack","William","Jacob","James","Thomas","Felix","Nathan","Samuel","Alexis","Emma","Olivia","Sophia","Zoe","Emily","Avery","Isabella","Charlotte","Lily","Ava","Lea","Alice","Florence","Zoe","Chloe","Beatrice","Rosalie"]
	
	for i in range(50):
		employeeno = str(1247 + i)
		fn = np.random.choice(firstnames)
		ln = np.random.choice(lastnames)

		print 'insert into employees values (%s, "%s", "%s")' % (employeeno, fn, ln)

def generatedeliveryvehicle():
	license = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","1","2","3","4","5","6","7","8","9"," "]
		
	for i in range(25):
		l = np.random.choice(license, size=(7), replace=False)
		out = ""
		for letter in l:
			out += letter
		
		print 'insert into deliveryvehicles values ("%s")' % (out)

generateemployees()


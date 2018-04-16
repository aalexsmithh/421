--How many movies were released in each year?

--load the data from HDFS and define the schema
movies = LOAD '/data/movies.csv'
	USING PigStorage(',')
	AS (
		movieid:INT,
		title:CHARARRAY,
		year:INT
	);

moviesperyear = GROUP movies BY year;
yearcount = FOREACH moviesperyear GENERATE group, COUNT(movies) as nummovies;
yearcount = ORDER yearcount BY group;

--store into a file called q1
STORE ordered INTO 'q1';
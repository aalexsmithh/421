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
yearcount = FOREACH moviesperyear GENERATE group, COUNT (movies);
yearcount = ORDER yearcount BY $0;

-- Send the output to the screen.
dump yearcount;

--For each genre, how many movies were produced in the years 2015 and 2016 ?

--load the data from HDFS and define the schema
movies = LOAD '/data/movies.csv'
	USING PigStorage(',')
	AS (
		movieid:INT,
		title:CHARARRAY,
		year:INT
	);

movies2015_2016 = FILTER movies BY (year==2015) OR (year==2016);

genres = LOAD '/data/moviegenres.csv'
	USING PigStorage(',')
	AS (
		movieid:INT,
		genre:CHARARRAY
	);

--Add genre info to movies
movies2015_2016 = JOIN movies2015_2016 BY movieid, genres BY movieid;

moviesByGenreAndYear = GROUP movies2015_2016 BY (genres::genre, movies2015_2016::year);
DESCRIBE moviesByGenreAndYear;

moviesByGenreAndYear = FOREACH moviesByGenreAndYear GENERATE group, COUNT($1);

dump moviesByGenreAndYear;

--Find the title of all 'Comedy' and 'Sci-Fi' movies from 2015

--load the data from HDFS and define the schema
movies = LOAD '/data/movies.csv'
	USING PigStorage(',')
	AS (
		movieid:INT,
		title:CHARARRAY,
		year:INT
	);

movies2015 = FILTER movies BY year == 2015;

genres = LOAD '/data/moviegenres.csv'
	USING PigStorage(',')
	AS (
		movieid:INT,
		genre:CHARARRAY
	);

-- Get all movies that are comedy or scifi
comedy_or_scifi = FILTER genres BY (genre=='Comedy') OR (genre=='Sci-Fi');

-- join comedy or scifi movies on the list of 2015 movies
comedy_or_scifi2015 = JOIN movies2015 BY movieid, comedy_or_scifi BY movieid;

-- project only title
comedy_or_scifi2015 = FOREACH comedy_or_scifi2015 GENERATE movies2015::title;

-- remove duplicates and order
comedy_or_scifi2015 = DISTINCT comedy_or_scifi2015;
comedy_or_scifi2015 = ORDER comedy_or_scifi2015 BY title;


dump comedy_or_scifi2015;

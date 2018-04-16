--Find years in which the number of movies produced were less than the previous year.

--load the data from HDFS and define the schema
movies = LOAD '/data/movies.csv'
	USING PigStorage(',')
	AS (
		movieid:INT,
		title:CHARARRAY,
		year:INT
	);
movies_ = LOAD '/data/movies.csv'
	USING PigStorage(',')
	AS (
		movieid:INT,
		title:CHARARRAY,
		year:INT
	);

movieCountByYear = GROUP movies BY year;
movieCountByYear = FOREACH movieCountByYear GENERATE group, COUNT($1) AS count;

movieCountByYear_ = GROUP movies_ BY year;
movieCountByYear_ = FOREACH movieCountByYear_ GENERATE group, COUNT($1) AS count;

xmoviesCountByYear = CROSS movieCountByYear, movieCountByYear_;

lessThanPreviousYear = FILTER xmoviesCountByYear BY
        (movieCountByYear::group==(movieCountByYear_::group)+1)
    AND (movieCountByYear::count<movieCountByYear_::count);

--output year, movies made that year, movies made the previous year
lessThanPreviousYear = FOREACH lessThanPreviousYear GENERATE $0, $1, $3;

STORE lessThanPreviousYear INTO '~/q4';

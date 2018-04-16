-- Find the 5 Sci-Fi movies from 2015 with the maximum number of user ratings

-- Load the data from HDFS and define the schema
movies = LOAD '/data/movies.csv'
         USING PigStorage(',')
         AS (
                movieid:INT,
                title:CHARARRAY,
                year:INT
         );

genres = LOAD '/data/moviegenres.csv'
         USING PigStorage(',')
         AS (
                movieid:INT,
                genre:CHARARRAY
         );

ratings = LOAD '/data/ratings.csv'
          USING PigStorage(',')
          AS (
                userid:INT,
                movieid:INT,
                rating:DOUBLE,
                timestamp:DATETIME
          );

-- Filter movies to 2015 and genres to scifi
movies2015 = FILTER movies BY year == 2015;
scifi = FILTER genres BY genre == 'Sci-Fi';

-- Join scifi and ratings, group by id
scifiRatings = JOIN scifi BY movieid, ratings BY movieid;
scifiByNumRatings = GROUP scifiRatings BY scifi::movieid;

-- Count ratings, sort and limit to 5 tuples
scifiByNumRatings = FOREACH scifiByNumRatings GENERATE ($0), COUNT ($1);
sorted = ORDER scifiByNumRatings BY $1 DESC;
top5 = LIMIT sorted 5;

-- Join top5 and movies to get titles
top5scifi = JOIN top5 BY $0, movies BY movieid;
top5scifi = FOREACH top5scifi GENERATE ($3), ($1);
top5scifi = ORDER top5scifi by $1 DESC;

DUMP top5scifi;

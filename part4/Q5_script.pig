-- Find the 10 movies with the maximum number of user ratings

-- Load the data from HDFS and define the schema
movies = LOAD '/data/movies.csv'
         USING PigStorage(',')
         AS (   
                movieid:INT,
                title:CHARARRAY,
                year:INT
         );

ratings = LOAD '/data/ratings.csv' 
          USING PigStorage(',') 
          AS ( 
                userid:INT, 
                movieid:INT, 
                rating:DOUBLE, 
                timestamp:DATETIME
          );

-- Join movies and ratings
movieRatings = JOIN movies BY movieid, ratings BY movieid;

-- Group movies by title
moviesByNumRatings = GROUP movieRatings BY movies::title;

-- Count ratings, sort and limit to 10 tuples
moviesByNumRatings = FOREACH moviesByNumRatings GENERATE ($0), COUNT ($1);
sorted = ORDER moviesByNumRatings BY $1 DESC;
top10 = LIMIT sorted 10;

DUMP top10;

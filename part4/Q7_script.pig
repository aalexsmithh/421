--For all the movies released in 2016, output the movieid, title, number of genres
--to which the movie belongs and the number of user ratings it has received.
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
        TIMESTAMP
    );

movies2016 = FILTER movies BY year == 2016;

movies2016genres = JOIN movies2016 BY movieid, genres BY movieid;

movies2016numgenres = GROUP movies2016genres BY movies2016::movieid;

movies2016numgenres = FOREACH movies2016numgenres GENERATE ($0), COUNT($1);

movies2016ratings = JOIN movies2016 BY movieid, ratings BY movieid;

movies2016numratings = GROUP movies2016ratings BY movies2016::movieid;

movies2016numratings = FOREACH movies2016numratings GENERATE ($0), COUNT($1);

movies2016total = JOIN movies2016 BY movieid, movies2016numgenres BY ($0);

movies2016totalfinal = JOIN movies2016total BY movieid, movies2016numratings BY ($0);

final = FOREACH movies2016totalfinal GENERATE $0 AS movieid, $1 AS title, $4 AS numgenres, $6 AS numratings;

store final into 'q7' using PigStorage(',');
explain final;

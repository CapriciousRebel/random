CREATE TABLE movies
(
    MovieID SERIAL PRIMARY KEY,
    Title VARCHAR(255),
    Rating VARCHAR(63)
);

CREATE TABLE owners
(
    OwnerID SERIAL PRIMARY KEY,
    Fname VARCHAR(255),
    Lname VARCHAR(255)
);


CREATE TABLE locations
(
    LocationID SERIAL PRIMARY KEY,
    City VARCHAR(255),
    State VARCHAR(255)
);

CREATE TABLE rewards
(
    RewardID SERIAL PRIMARY KEY,
    CustFName VARCHAR(255),
    CustLName VARCHAR(255),
    Email VARCHAR(255)
);

CREATE TABLE theatres
(
    TheatreID SERIAL PRIMARY KEY,
    TheatreName VARCHAR(255),
    OwnerID INT REFERENCES owners(OwnerID),
    LocationID INT REFERENCES locations(LocationID)
);



CREATE TABLE tickets
(
    MovieID INT REFERENCES movies(MovieID),
    TheatreID INT REFERENCES theatres(TheatreID),
    RewardID INT REFERENCES rewards(RewardID),
    SalesDate DATE,
    TicketsSold INT
);


UPDATE movies                                                        
SET                                                                             
rating = 'R'                                                                    
WHERE                                                                           
rating = 'PG';

UPDATE movies                                                        
SET                                                                             
rating = 'PG'                                                                   
WHERE                                                                           
rating = 'PG-13';


SELECT fname, lname, COUNT(fname)
FROM owners
    INNER JOIN theatres
    ON owners.ownerid = theatres.ownerid
GROUP BY fname,lname
HAVING COUNT(fname) >= 2;



SELECT title
FROM movies
    INNER JOIN tickets
    ON movies.movieid = tickets.movieid
    INNER JOIN theatres
    ON tickets.theatreid = theatres.theatreid
    INNER JOIN owners
    ON theatres.ownerid = owners.ownerid
GROUP BY title, owners.fname,owners.lname
HAVING owners.fname = 'David' AND owners.lname = 'Jackson';


SELECT title, tickets.ticketssold, 0.35*13.5*(tickets.ticketssold)
FROM Movies
    INNER JOIN tickets
    ON movies.movieid = tickets.movieid
GROUP BY title,tickets.ticketssold,rating
HAVING rating = 'PG-13' AND 0.35*13.5*(tickets.ticketssold) >= 200;



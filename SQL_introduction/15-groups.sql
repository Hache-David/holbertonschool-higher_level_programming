-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
USE hbtn_0c_0; SELECT score, COUNT(*) FROM second_table GROUP BY score;

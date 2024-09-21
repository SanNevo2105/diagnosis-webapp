use team059;
DROP TABLE IF EXISTS Drugs_Reviews;

create TABLE Drugs_Reviews(
	uniqueID INT PRIMARY KEY,
    drugName VARCHAR(50), 
    condition_ VARCHAR(255),
    review TEXT,
    rating INT,
    date_ TEXT,
    usefulCount INT);
    

INSERT INTO Drugs_Reviews (uniqueID, drugName, condition_, review, rating, date_, usefulCount)
SELECT uniqueID, LOWER(drugName), condition_, review, rating, date_, usefulCount
FROM Temp_DrugsReview 
WHERE drugName IN (SELECT Drugs.name FROM Drugs);
SELECT * FROM Drugs_Reviews;
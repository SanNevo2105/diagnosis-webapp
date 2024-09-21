CREATE TABLE Temp_Drugs (
    name VARCHAR(100) PRIMARY KEY,
    medical_condition VARCHAR(50),
    side_effects TEXT,
    generic_name VARCHAR(50),
    drug_classes VARCHAR(50),
    brand_names VARCHAR(50),
    activity FLOAT,
    rx_otc VARCHAR(10),
    pregnancy_category VARCHAR(1),
    csa VARCHAR(1),
    alcohol VARCHAR(1),
    related_drugs VARCHAR(20),
    medical_condition_description VARCHAR(255),
    rating FLOAT,
    no_of_reviews INT,
    drug_link VARCHAR(255),
    medical_condition_url VARCHAR(255)
);




CREATE TABLE Temp_SideEffects (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    substitute0 VARCHAR(50),
    substitute1 VARCHAR(50),
    substitute2 VARCHAR(50),
    substitute3 VARCHAR(50),
    substitute4 VARCHAR(50),
    sideEffect0 VARCHAR(50),
    sideEffect1 VARCHAR(50),
    sideEffect2 VARCHAR(50),
    sideEffect3 VARCHAR(50),
    sideEffect4 VARCHAR(50),
    sideEffect5 VARCHAR(50),
    sideEffect6 VARCHAR(50),
    sideEffect7 VARCHAR(50),
    sideEffect8 VARCHAR(50),
    sideEffect9 VARCHAR(50),
    sideEffect10 VARCHAR(50),
    sideEffect11 VARCHAR(50),
    sideEffect12 VARCHAR(50),
    sideEffect13 VARCHAR(50),
    sideEffect14 VARCHAR(50),
    sideEffect15 VARCHAR(50),
    sideEffect16 VARCHAR(50),
    sideEffect17 VARCHAR(50),
    sideEffect18 VARCHAR(50),
    sideEffect19 VARCHAR(50),
    sideEffect20 VARCHAR(50),
    sideEffect21 VARCHAR(50),
    sideEffect22 VARCHAR(50),
    sideEffect23 VARCHAR(50),
    sideEffect24 VARCHAR(50),
    sideEffect25 VARCHAR(50),
    sideEffect26 VARCHAR(50),
    sideEffect27 VARCHAR(50),
    sideEffect28 VARCHAR(50),
    sideEffect29 VARCHAR(50),
    sideEffect30 VARCHAR(50),
    sideEffect31 VARCHAR(50),
    sideEffect32 VARCHAR(50),
    sideEffect33 VARCHAR(50),
    sideEffect34 VARCHAR(50),
    sideEffect35 VARCHAR(50),
    sideEffect36 VARCHAR(50),
    sideEffect37 VARCHAR(50),
    sideEffect38 VARCHAR(50),
    sideEffect39 VARCHAR(50),
    sideEffect40 VARCHAR(50),
    sideEffect41 VARCHAR(50),
    use0 VARCHAR(50),
    use1 VARCHAR(50),
    use2 VARCHAR(50),
    use3 VARCHAR(50),
    use4 VARCHAR(50),
    Chemical_Class VARCHAR(50),
    Habit_Forming VARCHAR(50),
    Therapeutic_Class VARCHAR(50),
    Action_Class VARCHAR(50)
);



CREATE TABLE Temp_DrugsReview (
    uniqueID INT PRIMARY KEY,
    drugName VARCHAR(50), 
    condition_ VARCHAR(255),
    review TEXT,
    rating INT,
    date_ TEXT,
    usefulCount INT
);



CREATE TABLE Drugs (
    name VARCHAR(100) PRIMARY KEY,
    disease VARCHAR(50),
    side_effect1 VARCHAR(50),
    side_effect2 VARCHAR(50),
    side_effect3 VARCHAR(50),
    rating FLOAT,
    pregnancy_category VARCHAR(10),
    alcohol VARCHAR(10),
    FOREIGN KEY (disease) REFERENCES Diseases(name)
);


CREATE TABLE Combined_Drugs_SE (
    drug_name VARCHAR(100),
    medical_condition VARCHAR(50),
    side_effects VARCHAR(255),
    generic_name VARCHAR(255),
    drug_classes VARCHAR(255),
    brand_names VARCHAR(255),
    activity VARCHAR(255),
    rx_otc VARCHAR(255),
    pregnancy_category VARCHAR(10),
    csa VARCHAR(255),
    alcohol VARCHAR(10),
    related_drugs VARCHAR(255),
    medical_condition_description TEXT,
    rating FLOAT,
    no_of_reviews INT,
    drug_link VARCHAR(255),
    medical_condition_url VARCHAR(255),
    sideEffect0 VARCHAR(50),
    sideEffect1 VARCHAR(50),
    sideEffect2 VARCHAR(50)
);
INSERT INTO Drugs (name, disease, side_effect1, side_effect2, side_effect3, rating, pregnancy_category, alcohol)
SELECT drug_name, medical_condition, sideEffect0, sideEffect1, sideEffect2, rating, pregnancy_category, alcohol
FROM Combined_Drugs_SE 
WHERE medical_condition IN (SELECT name FROM Diseases)




CREATE TABLE Drug_Relations (
    drug1 VARCHAR(100),
    drug2 VARCHAR(100),
    PRIMARY KEY (drug1, drug2),
    FOREIGN KEY (drug1) REFERENCES Drugs(name),
    FOREIGN KEY (drug2) REFERENCES Drugs(name)
);
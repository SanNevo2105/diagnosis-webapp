use team059;

drop procedure special_rating; 

delimiter //
create procedure special_rating(in p_explain tinyint unsigned) 
begin 
	if (p_explain) then
		explain analyze
		SELECT Drugs. name, (0.7*AVG(usefulCount) + 0.3*AVG(Drugs.rating))
		FROM Drugs LEFT JOIN Drugs_Reviews ON Drugs.name = Drugs_Reviews.drugName
		GROUP BY Drugs.name;

	else  
		SELECT Drugs. name, (0.7*AVG(usefulCount) + 0.3*AVG(Drugs.rating))
		FROM Drugs LEFT JOIN Drugs_Reviews ON Drugs.name = Drugs_Reviews.drugName
		GROUP BY Drugs.name;
	end if ;
end //
delimiter ;

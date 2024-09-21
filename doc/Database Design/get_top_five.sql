use team059;

-- drop procedure get_top_five;

delimiter //
create procedure get_top_five(in medical_condition varchar(50)) 
begin
	SELECT drug_name, rating 
    FROM Drugs 
    WHERE Drugs.medical_conditon = medical_condition 
    ORDER BY rating DESC LIMIT 5;
end
delimiter ;
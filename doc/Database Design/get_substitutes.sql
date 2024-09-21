use team059;

drop procedure get_substitutes; 

delimiter //
create procedure get_substitutes(in input_drug varchar(50), in p_explain tinyint unsigned) 
begin 
	if (p_explain) then
		explain analyze
        
		SELECT drug2
		FROM Drug_Relations
		WHERE drug1 = input_drug

		UNION

		SELECT drug1
		FROM Drug_Relations
		WHERE drug2 = input_drug ;
	else  
		SELECT drug2
		FROM Drug_Relations
		WHERE drug1 = input_drug

		UNION

		SELECT drug1
		FROM Drug_Relations
		WHERE drug2 = input_drug ;
	end if ;
end //
delimiter ;
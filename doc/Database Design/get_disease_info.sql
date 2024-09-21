use team059;

-- drop procedure get_disease_info;

delimiter //
create procedure get_disease_info(in input varchar(50)) 
begin
	SELECT * FROM Diseases WHERE input = Dieases.name;
end
delimiter ;
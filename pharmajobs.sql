use datarep;

create table pharmajobs(
    -> JobId int PRIMARY KEY,
    -> JobTitle varchar(250),
    -> Company varchar(250),
    -> County varchar(250),
    -> NoOfVacancy int(11)
    -> );
	
	
create table employees
    -> (EmployeeId  INT AUTO_INCREMENT PRIMARY KEY,
    -> Name VARCHAR(250),
    -> Age INT,
    -> Salary INT);
	
	
 insert into pharmajobs(JobId,JobTitle,Company,County,NoOfVacancy)
    -> VALUES("111","API manufacturer","UCB","Clare","120") 
    -> VALUES("112","Animal Health","Bimeda Ireland","Dublin","150")
    -> VALUES("113","Pharma Manufacturer","Temmler","Kerry","60")
    -> VALUES("114","Infants Nutrional Products","Weyth","Limerick","600")
    -> VALUES("115","Food Supplements","Bioshell","Mayo","40");	
	
	
	
select * from pharmajobs;	
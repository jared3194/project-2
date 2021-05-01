ALTER TABLE flights
ADD PRIMARY KEY (flight_id);

SELECT * FROM scatter;


create table scatter
	as(select dpf.flight_number, 
	   dpf.iata flight_iata,
	   dpf.icao flight_icao,
	   dpf.airport_id departure_airport_id,
	   dpa.airport departure_airport,
	   dpf.terminal departure_terminal,
	   dpf.gate departure_gate,
	   dpf.delay departure_delay,
	   dpf.scheduled departure_scheduled,
	   dpf.estimated departure_estimated,
	   dpf.actual departure_actual,
	   dpf.estimated_runway departure_estimated_runway,
	   dpf.actual_runway departure_actual_runway,
	   --arrivals
-- 	   arf.flight_number, 
-- 	   arf.iata flight_iata,
-- 	   arf.icao flight_icao,
	   arf.airport_id arrival_airport_id,
	   ara.airport arrival_airport,
	   arf.terminal arrival_terminal,
	   arf.gate arrival_gate,
	   arf.delay arrival_delay,
	   arf.scheduled arrival_scheduled,
	   arf.estimated arrival_estimated,
	   arf.actual arrival_actual,
	   arf.estimated_runway arrival_estimated_runway,
	   arf.actual_runway arrival_actual_runway
  from flights dpf, 
  	   flights arf,
	   airports dpa,
	   airports ara
 where dpf.airport_id = dpa.airport_id
   and dpf.flight_type = 'DEPARTURE'  
   and arf.airport_id = ara.airport_id
   and arf.flight_type = 'ARRIVAL'
   and dpf.flight_number = arf.flight_number);
   
   ALTER TABLE scatter
   DROP COLUMN arrival_actual_runway;
   
   CREATE TABLE arratlanta AS
   	 SELECT * FROM scatter 
	 WHERE arrival_airport_id = '19';
	 
SELECT * FROM arratlanta; 
   
 CREATE TABLE arrlax AS
   	 SELECT * FROM scatter 
	 WHERE arrival_airport_id = '194';
	 
 SELECT * FROM arrlax; 
 
 create table scatter2
	as(select dpf.flight_number, 
	   dpf.iata flight_iata,
	   dpf.icao flight_icao,
	   dpf.airport_id departure_airport_id,
	   dpa.airport departure_airport,
	   dpf.terminal departure_terminal,
	   dpf.gate departure_gate,
	   dpf.delay departure_delay,
	   dpf.scheduled departure_scheduled,
	   dpf.estimated departure_estimated,
	   dpf.actual departure_actual,
	   dpf.estimated_runway departure_estimated_runway,
	   dpf.actual_runway departure_actual_runway,
	   --arrivals
-- 	   arf.flight_number, 
-- 	   arf.iata flight_iata,
-- 	   arf.icao flight_icao,
	   arf.airport_id arrival_airport_id,
	   ara.airport arrival_airport,
	   arf.terminal arrival_terminal,
	   arf.gate arrival_gate,
	   arf.delay arrival_delay,
	   arf.scheduled arrival_scheduled,
	   arf.estimated arrival_estimated,
	   arf.actual arrival_actual,
	   arf.estimated_runway arrival_estimated_runway,
	   arf.actual_runway arrival_actual_runway
  from flights dpf, 
  	   flights arf,
	   airports dpa,
	   airports ara
   where dpf.airport_id = dpa.airport_id
   and dpf.flight_type = 'ARRIVAL'  
   and arf.airport_id = ara.airport_id
   and arf.flight_type = 'DEPARTURE'
   and dpf.flight_number = arf.flight_number);
   
    SELECT * FROM arrlaxsum; 
	
ALTER  TABLE scatter2
   DROP COLUMN arrival_estimated_runway;
   
CREATE TABLE arrlax AS
   	 SELECT * FROM scatter 
	 WHERE departure_airport_id = '194';
	 
    SELECT * FROM depatl; 
   
CREATE TABLE arrlaxsum AS
SELECT 
	departure_airport,
	COUNT (departure_airport)
FROM 
	arrlax
GROUP BY
	departure_airport
	

alter table arrlaxsum
add column arrival_airport varchar;

select * from arrlaxsum;

alter table arrlaxsum
rename column departure_count to departure_count_lax;

create table arrivals as
  (select * from arratlsum);
  
insert into arrivals (departure_atl_airport, departure_count_atl, arrival_airport_atl) select * from arratlsum;
insert into arrivals (departure_lax_airport, departure_count_lax, arrival_airport_lax) select * from arrlaxsum;


alter table arratlsum
rename column departure_count_lax to departure_count_atl;


insert into arrivals 
select departure_lax_airport, departure_count_lax, arrival_airport_lax from arrlaxsum;
  

select * from arrivals
  
 create database aviation
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8';
 
--create tables under aviation schema 
 
create table airports (
	airport_id serial not null primary key,
	airport varchar(1000) not null,
	iata varchar(100) not null,
	icao varchar(100) not null,
	timezone varchar(100),
	constraint airports_uk unique (iata, icao) );
 
create table airlines (
	airline_id serial not null primary key,
	airline varchar(1000) not null,
	iata varchar(100) not null,
	icao varchar(100) not null, 
	constraint airlines_uk unique (iata, icao) );	

create table flights (
	flight_id serial not null primary key,
	flight_number varchar(500) not null,
	flight_type varchar(100) not null,
	iata varchar(100) not null,
	icao varchar(100) not null,
	airport_id int not null, 
	terminal varchar(100),
	gate varchar(100),
	baggage varchar(100),
	delay varchar(100),
	scheduled date,--varchar(100),
	estimated date,
	actual date, 
	estimated_runway date,
	actual_runway date
);	 	 
 
create view flight_details
as
select dpf.flight_number, 
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
   and dpf.flight_number = arf.flight_number ;
 
 


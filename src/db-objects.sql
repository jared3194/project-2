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
	airline_id int,
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
 


select ap.airport, fl.* 
  from flights fl left join airports ap on fl.airport_id = ap.airport_id
where ap.iata = 'ATL';

select ap.airport, fl.* 
  from flights fl left join airports ap on fl.airport_id = ap.airport_id
where ap.iata = 'LAX';

select ap.airport, fl.* 
  from flights fl left join airports ap on fl.airport_id = ap.airport_id
where fl.flight_type = 'DEPARTURE';

select ap.airport, fl.* 
  from flights fl left join airports ap on fl.airport_id = ap.airport_id
where fl.flight_type = 'ARRIVAL';
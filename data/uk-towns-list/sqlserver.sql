CREATE TABLE uk_towns (
  id integer,
  place_name varchar(38),
  county varchar(37),
  country varchar(16),
  grid_reference varchar(7),
  easting integer,
  northing integer,
  latitude decimal(8,5),
  longitude decimal(8,5),
  postcode_area varchar(6),
  type varchar(5),
  PRIMARY KEY (id)
)
GO

BULK INSERT uk_towns
FROM 'C:\path\to\uk-towns.csv'
WITH
(
  FIELDTERMINATOR = ',',
  ROWTERMINATOR = '\n',
  FIRSTROW = 2
)

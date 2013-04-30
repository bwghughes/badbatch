CREATE TABLE uk_towns
(
  id integer,
  place_name character varying(38),
  county character varying(37),
  country character varying(16),
  grid_reference character varying(7),
  easting integer,
  northing integer,
  latitude numeric(8,5),
  longitude numeric(8,5),
  postcode_area character varying(6),
  type character varying(5),
  CONSTRAINT uk_towns_pkey PRIMARY KEY (id)
);

COPY uk_towns FROM '/Users/ben/repos/badbatch/data/uk-towns-list' DELIMITERS ',' CSV HEADER;
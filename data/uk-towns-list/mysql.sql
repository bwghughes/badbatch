CREATE TABLE `uk_towns` (
  `id` integer unsigned,
  `place_name` varchar(38),
  `county` varchar(37),
  `country` varchar(16),
  `grid_reference` varchar(7),
  `easting` integer,
  `northing` integer,
  `latitude` decimal(8,5),
  `longitude` decimal(8,5),
  `postcode_area` varchar(6),
  `type` varchar(5),
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

LOAD DATA LOCAL INFILE '/path/to/uk-towns.csv'
INTO TABLE uk_towns
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

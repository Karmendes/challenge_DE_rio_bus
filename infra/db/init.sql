-- Create the schema
CREATE SCHEMA IF NOT EXISTS sc_silver;
CREATE SCHEMA IF NOT EXISTS sc_gold;

-- create the table silver
CREATE TABLE sc_silver.tb_brt_api (
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  codigo VARCHAR(255), -- Adjust data type based on expected code length
  placa VARCHAR,
  linha VARCHAR,
  latitude float,
  longitude float,
  dataHora TIMESTAMP,  -- Use a proper date/time data type
  velocidade float,
  id_migracao_trajeto VARCHAR,
  sentido VARCHAR,
  trajeto VARCHAR,
  hodometro FLOAT,
  direcao VARCHAR,
  dh_extraction TIMESTAMP
);

-- create the gold table
CREATE TABLE sc_gold.tb_brt_api (
  codigo VARCHAR(255), -- Adjust data type based on expected code length
  latitude FLOAT,
  longitude FLOAT,
  velocidade FLOAT
);


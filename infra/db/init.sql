-- Create the schema
CREATE SCHEMA IF NOT EXISTS sc_silver;
CREATE SCHEMA IF NOT EXISTS sc_gold;

-- create the table silver
CREATE TABLE sc_silver.tb_brt_api (
  codigo VARCHAR(2048),
  placa VARCHAR(6),
  linha VARCHAR(6),
  latitude float,
  longitude float,
  dataHora int,
  velocidade float,
  id_migracao_trajeto VARCHAR,
  sentido VARCHAR,
  trajeto VARCHAR,
  hodometro float,
  direcao int,
  dh_extraction datetime
);

-- create the gold
CREATE TABLE sc_silver.tb_brt_api (
  codigo VARCHAR(2048),
  latitude float,
  longitude float,
  velocidade float,
);



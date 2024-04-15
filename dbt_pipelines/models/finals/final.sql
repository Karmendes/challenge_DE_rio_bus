
{{ config(target="sc_gold") }}

with

source as (

    select * from {{source('brt','tb_brt_api')}}

),
renamed as (
    select
    codigo,
    latitude,
    longitude,
    velocidade
    from 
    source
)

select * from renamed
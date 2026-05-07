{{ config(materialized='table') }}

with raw_orders as (

    select * from {{ source('raw_data', 'orders') }}

)

select
    order_id,
    customer_name,
    item_name,
    price

from raw_orders

qualify row_number()
over (
    partition by order_id
    order by order_id
) = 1
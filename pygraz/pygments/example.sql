-- Simple SQL example.
select
    customer_number,
    first_name,
    surname,
    date_of_birth
from
    customer
where
    date_of_birth >= '1990-01-01'
    and rating <= 20


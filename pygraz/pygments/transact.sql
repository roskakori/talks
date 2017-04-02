-- Simple Transact-SQL example.
declare @date_of_birth date = '1990-01-01';

select top 10
    *
from
    [customer]
where
    [date_of_birth] = @date_of_birth
order by
    [customer_number]

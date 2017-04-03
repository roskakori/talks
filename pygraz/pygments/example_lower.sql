select
    CustomerNumber,
    FirstName,
    Surname
from
    Customer
where
    DateOfBirth >= '1990-01-01'

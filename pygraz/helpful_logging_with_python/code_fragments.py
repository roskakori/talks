"""
A couple of code fragments used throughout the slides. Running this module
ensures that the code is syntactically correct, just don't expect it to do
anything meaningful.
"""
import logging

_log = logging.getLogger('example')

actual_value = 0
expected_value = 1


if actual_value != expected_value:
    _log.error('...')


# BAD EXAMPLE, don't use this template
def process_customers_bad(customers_path: str):
    try:
        with open(customers_path, encoding='utf-8') as customers_file:
            for line in customers_file:
                process_customer(line)
    except OSError:
        _log.error('cannot process customer data in "%s"', customers_path)
        raise


def process_customer(line: str):
    pass


class SomeError(Exception):
    pass


def process_customers_good(customers_path: str):
    try:
        with open(customers_path, encoding='utf-8') as customers_file:
            for line in customers_file:
                process_customer(line)
    except OSError as error:
        raise SomeError('cannot process customer data in "%s"',
                        customers_path) from error


def do_something():
    pass


try:
    do_something()
except OSError as error:
    _log.error('...')


name = 'Hugo'
size = 172

# BAD: Format strings for logging
_log.debug(f'{name} has a size of {size}cm')

# GOOD: debug log plain strings
_log.debug('%s has a size of %dcm', name, size)


def some_computed_number():
    # This would normally take a while to compute.
    return 17.3


# BAD: always compute number even if might not be logged
_log.debug('processing %f foos', some_computed_number())


# GOOD: conditional logging of computed information
if _log.isEnabledFor(logging.DEBUG):
    _log.debug('processing %f foos', some_computed_number())

"""
An example of reading a file with and without logging
"""
import logging
import os
import time


_log = logging.getLogger('example')
customers_path = os.path.join(os.path.dirname(__file__), 'customers.txt')

logging.basicConfig(level=logging.DEBUG)


def process_customer(line: str):
    """
    A dummy function that would normally process a line about a customer in a
    meaningful way
    """
    assert line is not None
    # Pretend that processing a customer takes some time
    time.sleep(0.123)


_log.debug('writing dummy customers to "%s"', customers_path)
with open(customers_path, 'w', encoding='utf-8') as customers_file:
    for customer_number in range(1, 70):
        customers_file.write(f'customer_{customer_number}\n')

_log.debug('--- process a file without logging')
with open(customers_path, encoding='utf-8') as customers_file:
    for line in customers_file:
        process_customer(line)


_log.debug('--- process a file with basic logging')
_log.info('processing customers from "%s"', customers_path)
line_number = 0
with open(customers_path, encoding='utf-8') as customers_file:
    for line_number, line in enumerate(customers_file, 1):
        process_customer(line)
_log.info('processed %d customers', line_number)


_log.debug('--- process a file with progress logging')
_LOG_PROGRESS_THRESHOLD_IN_SECONDS = 3

_log.info('processing customers from "%s"', customers_path)
start_time = time.time()
last_log_time = start_time
line_number = 0
with open(customers_path, encoding='utf-8') as customers_file:
    for line_number, line in enumerate(customers_file, 1):
        current_time = time.time()
        if current_time - last_log_time >= _LOG_PROGRESS_THRESHOLD_IN_SECONDS:
            _log.info('processing customer record %d', line_number)
            last_log_time = current_time
        process_customer(line)
end_time = time.time()
_log.info('processed %d customers in %.2f seconds',
          line_number, end_time - start_time)


_log.debug('--- cleanup: removing customers file "%s"', customers_path)
os.remove(customers_path)

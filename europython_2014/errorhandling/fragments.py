"""
Various code fragments used in the slides. Keeping the original here helps
ensuring that the code is valid.
"""
import codecs
import logging

from dataerror import DataError


_log = logging.getLogger('some')


# Dummy exception.
class SomeError(Exception):
    pass


def process_something(height):
    if height <= 0:
        raise ValueError('height must be greater than 0')

    # Actual processing would happen here.
    pass


def process_something_again(height):
    if height <= 0:
        raise ValueError(
            'height is %d ' % height
            + 'but must be greater than 0')


def process_data_file(data_file):
    assert data_file is not None

    line_number = 1
    try:
        # Process all heights read from `data_file`.
        for line_number, line in enumerate(data_file, start=1):
            process_something(int(line))
    except ValueError as error:
        print('cannot process %s, line %d: %s' %
            (data_file.name, line_number, error))


def report_example_error():
    try:
        process_something(-3)
    except ValueError as error:
        print(error)


# Dummy method.
def do_something():
    raise SomeError('something must be something else')


def detect_error_and_raise_exception():
    actual_value = 1
    expected_value = 2

    # Detect an error and raise an Exception.
    if actual_value != expected_value:
        raise SomeError('helpful error message')


def process_input(input_file):
    # Dummy
    pass


def cleanup_with_Finally():
    # Using finally
    inputFile = codecs.open('some.txt', 'r', 'utf-8')
    try:
        process_input(inputFile)
    finally:
        inputFile.close()


def cleanup_with_with():
    with codecs.open('some.txt', 'r', 'utf-8') as inputFile:
        process_input(inputFile)


def cleanup_with_closing():
    def prepare_customer_db():
        import sqlite3
        from contextlib import closing

        with closing(sqlite3.connect(':memory:')) as customerDb:
            with closing(customerDb.cursor()) as customerCursor:
                customerCursor.execute("""
                    create table customers
                        id integer,
                        first_name varchar(60),
                        last_name varchar(60),
                        date_of_birth datetime
                        primary key (id)
                """)

    prepare_customer_db()

    import sqlite3
    from contextlib import closing

    # Print all customers.
    with closing(sqlite3.connect(':memory:')) as customer_db:
        with closing(customer_db.cursor()) as customer_cursor:
            for row in customer_cursor('select * from customers'):
                print(row)


def process_data_file_possibly_raising_data_error(data_file):
    assert data_file is not None

    line_number = 1
    try:
        # Process all heights read from `data_file`.
        for line_number, line in enumerate(data_file, start=1):
            process_something(int(line))
    except ValueError as error:
        raise DataError(error, data_file.name, line_number)


def handle_exception_by_logging():
    # Handle an exception raised by a called routine.
    try:
        do_something()
    except SomeError as error:
        logging.error(u'cannot do something: %s', error)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    try:
        detect_error_and_raise_exception()
    except SomeError:
        pass

    handle_exception_by_logging()

    report_example_error()
